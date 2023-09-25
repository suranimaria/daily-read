from flask import Flask, render_template, request
import os, subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'split'  # Define the directory where uploaded files will be saved
ALLOWED_EXTENSIONS = {'pdf'}  # Only allow PDF files

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Configure Flask to use the defined upload folder

@app.route('/')
def index():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    # if user does not select file, browser also submit an empty part without filename
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = file.filename
        start_date = request.form.get('start_date')

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Extract text from the uploaded file
        try:
            extract_command = ["python", "scripts/extract_text.py", os.path.join(app.config['UPLOAD_FOLDER'], filename)]
            subprocess.check_call(extract_command)

            # Parse chapters from the extracted text
            parse_command = ["python", "scripts/parse_chapters.py"]
            subprocess.check_call(parse_command)
        except subprocess.CalledProcessError:
            return 'Error in processing the file. Please check the scripts.'

        return 'File successfully uploaded'
    else:
        return 'Invalid file type'

if __name__ == "__main__":
    app.run(debug=True)
