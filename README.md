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
        Create a file named `.env`, `.env.dev`, `.env.tst` in the root of your project. Copy the contents from the provided `.env.example`, `.env.dev.example`, `.env.tst.example` file and replace the placeholder values with your environment details.

 



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
   
    python app.py --env=<dev | prod | tst>
    ```

2. Open your web browser and go to `http://localhost:5000` to view the app.

