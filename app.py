# File: app.py

from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/<filename>', methods=['GET'])
def get_file_content(filename='file1.txt'):
    try:
        start_line = request.args.get('start_line', type=int)
        end_line = request.args.get('end_line', type=int)
        file_path = os.path.join('files', filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            if start_line is not None and end_line is not None:
                content = ''.join(lines[start_line-1:end_line])
            else:
                content = ''.join(lines)
                
        return render_template('file_content.html', content=content)
    
    except FileNotFoundError:
        error_message = f"File '{filename}' not found."
        return render_template('error.html', error_message=error_message), 404
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error_message=error_message), 500

if __name__ == '__main__':
    app.run(debug=True)

