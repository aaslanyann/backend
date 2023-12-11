# Neom Backend App

This is a web backend application built using Python, Flask, and PostgreSQL.



## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.11.1 or higher)
- PostgreSQL (version 15.5 or higher)

## Configuration
1. Clone the repository:

    ```bash
    git clone https://git.codemotion.ninja/ada-project/back-end.git
    cd back-end
    ```


2. Create Configuration Files:

    - **.env:** 
        Create a file named `.env` in the root of your project. Copy the contents from the provided `.env.example` or `.env.dev.example` or `.env.tst.example` file and replace the placeholder values with your environment details.

 



## Getting Started

1. Install dependencies and run the application:

    ```bash
    # Check if Python is installed
    python --version || echo "Python is not installed. Please install Python and run the script again."

    # Install virtual environment (if not installed)
    python -m pip install virtualenv

    # Create virtual environment
    python -m venv venv

    # Activate virtual environment (for Windows)
    venv\Scripts\activate

    # Activate virtual environment for Unix-like systems
    # source venv/bin/activate

    # Install required dependencies
    pip install -r requirements.txt

    # Run the application
   
    python app.py 
    ```

2. Open your web browser and go to `http://localhost:5000` to view the app.


### Migrations

1. Importing your models in `migrations/env.py` to allow flask migrations to detect changes 


2. Creating and Applying Migrations

    ```bash
    #set up the database
    flask db init   
   
   
   #generate an initial migration
   flask db migrate -m "Initial migration"

   
   #apply the migration
   flask db upgrade
    ```






## Run With Docker

### Prerequisites

Before running the application with docker, make sure you have the following installed:

- Docker (version 20.10.8 or higher)

- Docker-compose (version 1.29.2, or higher)

### Get Start

1. Build and run.
    ```
   #dev 
   docker-compose -f docker-compose.dev.yml up   
   
   #prod
   docker-compose -f docker-compose.prod.yml up
    ```
   

   