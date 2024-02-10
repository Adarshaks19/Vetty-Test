# File Content Viewer

This Flask application allows users to view the contents of text files in HTML format. It provides a single GET route that reads the content of a specified file and renders it properly in an HTML page.

## Features
- Supports reading contents from multiple text files.
- Preserves any markup present in the text files.
- Allows specifying start and end line numbers to display a specific portion of the file.
- Handles exceptions gracefully and displays error details in case of any issues.

## Deployment
1. Clone this repository.
2. Set up a Python virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the Flask app:
    ```bash
    python app.py
    ```
6. Access the application in your browser at `http://localhost:5000/<filename>?start_line=<start_line>&end_line=<end_line>`

## Usage
- `<filename>`: Optional variable part of the URL, defaults to 'file1.txt' if not specified.
- `start_line`: Optional URL query parameter to specify the start line number.
- `end_line`: Optional URL query parameter to specify the end line number.

## Error Handling
- If the specified file is not found, a 404 error page is displayed.
- For any other exceptions, a 500 error page is displayed with details of the error.

## Files
- `app.py`: Flask application code.
- `templates/`: Directory containing HTML templates.
    - `file_content.html`: Template for displaying file content.
    - `error.html`: Template for displaying error messages.
- `requirements.txt`: List of dependencies.

## Author
- Adarsh Kumar Singh

Feel free to customize and extend this application as needed.
