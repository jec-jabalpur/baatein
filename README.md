# baatein
Python project for college students

## Setup

- Clone the repository
    ```
    git clone https://github.com/jec-jabalpur/baatein
    ```

- Switch to the project directory
    ```
    cd baatein
    ```

- Create a Virtual Environment and activate it
    ```
    python -m venv venv
    source venv/bin/activate (for Linux)
    venv\Scripts\activate (for Windows)
    ```

- Install all packages
    ```
    pip install -r requirements.txt
    ```

- Set the FLASK_APP environment variable if .flaskenv is not working for you.
    ```
    export FLASK_APP=baatein.py (for Linux)
    set FLASK_APP=baatein.py (for Windows)
    ```

- Run the DB migrations
    ```
    flask db upgrade
    ```

- Run the application
    ```
    flask run
    ```

Open http://localhost:5000 to view the working application.
