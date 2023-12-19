
# Coder AGI Flask Application

## Introduction
This Flask application is designed to interface with OpenAI's API to generate documents based on user prompts. It features a robust API with user authentication, database integration, rate limiting, and asynchronous task handling.

## Features
- **User Authentication**: Secure registration and authentication for API access.
- **OpenAI Document Generation**: Leverage OpenAI's API to generate documents.
- **Database Integration**: SQLite database to store prompts and responses.
- **API Rate Limiting**: Manage API usage to prevent abuse.
- **Swagger UI**: API documentation and testing interface.
- **Error Handling**: Improved error responses for better debugging.
- **Logging**: Detailed logging for monitoring and troubleshooting.
- **Asynchronous Tasks**: Efficient handling of background tasks using Celery.
- **Environment Variable Configuration**: Secure and flexible configuration.

## Installation and Setup
1. Clone the repository or download the provided zip file.
2. Install the required dependencies: `pip install -r requirements.txt`.
3. Set environment variables for configuration (e.g., OpenAI API key).
4. Initialize the database: `python models.py`.
5. Run the application: `flask run` or `python app.py`.

## Usage
- Register a new user via `/register` endpoint.
- Generate documents using `/generate_document` endpoint.
- Access the Swagger UI at `/swagger` for API documentation and testing.

## Configuration
Set the following environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key.

## Troubleshooting and Support
- **Issue**: Error while connecting to the database.
  **Solution**: Ensure SQLite is installed and the database file is not corrupted.

For further support, please reach out to the development team.

