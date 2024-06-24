// src/App.jsx
import React, { useState } from 'react';

function App() {
  const [url, setUrl] = useState('');
  const [depth, setDepth] = useState(1);
  const [loading, setLoading] = useState(false);
  const [sitemap, setSitemap] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const response = await fetch('http://127.0.0.1:5000/crawl', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url, depth }),
    });

    if (response.ok) {
      const data = await response.json();
      setSitemap(data.sitemap);
    }

    setLoading(false);
  };

  return (
    <div className=" container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-4 text-center">Web Crawler</h1>
      <form onSubmit={handleSubmit} className="mb-4 flex items-center justify-center">
        <input
          type="text"
          id="url"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter URL"
          className="border rounded-l px-4 py-2 w-full sm:w-auto focus:outline-none focus:border-blue-500"
        />
        <input
          type="number"
          id="depth"
          value={depth}
          onChange={(e) => setDepth(parseInt(e.target.value))}
          placeholder="Depth"
          min="1"
          className="border rounded-r px-4 py-2 w-20 ml-2 focus:outline-none focus:border-blue-500"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 ml-2 rounded focus:outline-none hover:bg-blue-600"
        >
          {loading ? 'Crawling...' : 'Crawl'}
        </button>
      </form>

      {loading && <p className="text-gray-600 text-center">Crawling in progress...</p>}

      <div>
        <h2 className="text-2xl font-bold mb-2 text-center">Sitemap</h2>
        <div className="border rounded p-4">
          <pre className="overflow-auto">{JSON.stringify(sitemap, null, 2)}</pre>
        </div>
      </div>
    </div>
  );
}

export default App;
