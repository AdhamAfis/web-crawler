# Web Crawler Project

## Overview

This project is a web crawler application built using Flask for the backend and React with Vite for the frontend. The crawler fetches and parses web pages, extracts links, and recursively follows these links to a specified depth, creating a sitemap of the domain. This project was inspired by the [web-crawler-with-depth](https://github.com/Hiurge/web-crawler-with-depth) repository by Hiurge.

## Features

- **Recursive Web Crawling**: Crawls a given URL to a specified depth, following links within the same domain.
- **Flask Backend**: Handles the crawling logic and provides an API endpoint for starting the crawl.
- **React Frontend**: Simple user interface for inputting the URL and depth, and displaying the resulting sitemap.
- **CORS Enabled**: Allows cross-origin requests between the frontend and backend.
- **Error Handling**: Gracefully handles invalid requests and network errors.

## Technologies Used

- **Backend**: Flask, BeautifulSoup, requests, tldextract
- **Frontend**: React, Vite
- **Networking**: Flask-CORS

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/AdhamAfis/web-crawler.git
    cd web-crawle
    ```

2. **Backend Setup**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Frontend Setup**
    ```bash
    cd frontend
    npm install
    ```

### Running the Application

1. **Start the Backend**
    ```bash
    cd backend
    flask run
    ```

2. **Start the Frontend**
    ```bash
    cd frontend
    npm run dev
    ```

3. **Access the Application**
    Open your browser and navigate to `http://localhost:5173`.

## API Endpoint

### POST /crawl

Starts the crawling process.

- **URL**: `/crawl`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "url": "https://example.com",
      "depth": 2
    }
    ```
- **Response**:
    ```json
    {
      "domain": "https://example.com",
      "crawl_depth": 2,
      "sitemap": { ... }
    }
    ```

## Project Structure

- **backend**: Contains the Flask application and crawling logic.
- **frontend**: Contains the React application for the user interface.

## Code Explanation

### Backend (`backend/app.py`)

- **Flask Setup**: Initializes the Flask application and enables CORS.
- **Crawling Functions**: Includes `get_soup`, `get_raw_links`, `clean_links`, `crawl_page`, and `crawl_recursive` functions for fetching and parsing web pages.
- **API Endpoint**: Defines the `/crawl` endpoint for starting the crawl process.

### Frontend (`frontend/src/App.jsx`)

- **React Setup**: Basic setup with state management using hooks.
- **Form Handling**: Handles URL and depth input, and submits the data to the backend.
- **Sitemap Display**: Displays the resulting sitemap in a formatted JSON view.

## Inspiration

This project was inspired by the [web-crawler-with-depth](https://github.com/Hiurge/web-crawler-with-depth) repository by Hiurge. Their implementation provided a solid foundation and ideas for developing this crawler.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
