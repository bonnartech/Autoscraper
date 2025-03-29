# Scraper Dashboard Project

This project is a web application built with Django that scrapes data from external sources and displays it on a dashboard. The application extracts, processes, and stores the scraped data in a database, which is then visualized in the dashboard interface.

## Features
- Scrapes data from predefined sources
- Stores scraped data in a database
- Displays data dynamically on a dashboard
- Supports Azure Blob Storage for file storage (using Azurite for local development)
- Provides an API endpoint for accessing scraped data

## Technologies Used
- **Backend**: Django (Python)
- **Database**: SQLite (or PostgreSQL for production)
- **Frontend**: HTML, CSS, JavaScript (Django Templates)
- **Storage**: Azure Blob Storage (or Azurite for local testing)
- **Cloud Services**: Azure (optional for deployment)

## Installation
### Prerequisites
- Python 3.x
- Django
- Azurite (for local Azure Blob Storage emulation)
- Azure SDK (for production deployment)

### Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/scraper-dashboard.git
   cd scraper-dashboard
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Start the local Azure emulator (Azurite):**
   ```sh
   azurite
   ```

6. **Set up environment variables (`.env` file):**
   ```ini
   AZURE_STORAGE_CONNECTION_STRING=connection_string 
   SECRET_KEY=secret_key
   DEBUG=True
   ```

7. **Run the Django development server:**
   ```sh
   python manage.py runserver
   ```

## Usage
- Access the dashboard at `http://127.0.0.1:8000/dashboard/`
- Scraped data will be displayed dynamically
- API endpoint for scraped data: `http://127.0.0.1:8000/api/data/`

## Deployment
To deploy the project to Azure or any cloud provider:
1. Set up a production database (PostgreSQL recommended)
2. Configure `ALLOWED_HOSTS` in `settings.py`
3. Use Azure Storage for file handling
4. Deploy using Azure App Services or a cloud VM

