
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import openai
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Document, User, Base
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Rate Limiter setup
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Database setup
engine = create_engine('sqlite:///coder_agi.db')
Session = sessionmaker(bind=engine)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    session = Session()
    user_exists = session.query(User).filter(User.username == username).first()
    if user_exists:
        return jsonify({'error': 'User already exists'}), 409

    user = User(username=username)
    user.set_password(password)
    session.add(user)
    session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/generate_document', methods=['POST'])
@limiter.limit("10 per minute")
def generate_document():
    data = request.json
    api_key = data['api_key']
    prompt = data['prompt']
    model = data.get('model', 'gpt-3.5-turbo')

    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1024
        )
        response_text = response.choices[0].text

        # Save to database
        session = Session()
        document = Document(prompt=prompt, response=response_text)
        session.add(document)
        session.commit()

        return jsonify({"document": response_text, "id": document.id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Application is running!"

if __name__ == '__main__':
    app.run()

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Coder AGI API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

celery = make_celery(app)

@app.route('/async_task', methods=['POST'])
def async_task():
    # Example of an asynchronous task
    pass

import os

openai.api_key = os.getenv('OPENAI_API_KEY')
