
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [api_key, setApiKey] = useState('');
  const [prompt, setPrompt] = useState('');
  const [document, setDocument] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/generate_document', { api_key, prompt });
      setDocument(response.data.document);
    } catch (err) {
      setError(err.response?.data?.error || 'Error generating document');
    }
  };

  return (
    <div>
      <h1>Legal Document Generator</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text"
          value={api_key}
          onChange={(e) => setApiKey(e.target.value)}
          placeholder="Enter your OpenAI API key"
        />
        <textarea 
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your case details"
        />
        <button type="submit">Generate Document</button>
      </form>
      {document && <div><h2>Generated Document</h2><p>{document}</p></div>}
      {error && <p>Error: {error}</p>}
    </div>
  );
}

export default App;
