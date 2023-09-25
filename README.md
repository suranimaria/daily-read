# DailyRead

DailyRead is a web application that automates the process of extracting text from PDFs, parsing them into chapters, and sending them via email. The project is designed to facilitate a daily reading routine by sending a new chapter from a book every day.

## Structure

- **scripts/extract-text.py**: This script extracts text from PDFs, handles the sorting of PDFs based on their numeric part, and saves the output to a text file.
- **scripts/parse-chapters.py**: Processes the extracted text from the previous step and splits it into individual chapters.
- **scripts/send-email.py**: Sends out the appropriate chapter via email based on the days elapsed since a specified start date.
- **index.html**: The main webpage for uploading PDFs to be processed.
- **app.py**: The Flask web application that handles the uploading of PDFs.

## Requirements

- **Python**: 3.9.16
- **os**: Python module for interacting with the operating system.
- **subprocess**: Python module for working with system processes.
- **re**: Python module for regular expressions.
- **sys**: Python module that provides access to system-specific parameters and functions.
- **pdfminer.six** (Install using `pip install pdfminer.six`): Python package for extracting text and metadata from PDF files.
- **Flask** (Install using `conda install flask` or `pip install Flask`): Python package for building web applications.
- **datetime**: Python module for working with dates and times.
- **email-validator** (Install using `pip install email-validator`): Python package for validating email addresses.
- **smtplib**: Python module for sending emails using the Simple Mail Transfer Protocol (SMTP).
- **ssl**: Python module for providing secure sockets (SSL/TLS) communication.

To set up the required Python environment, you can use [Anaconda](https://www.anaconda.com/products/individual) and create a new environment with the specified Python version and packages.

## Setup

1. Ensure you have the necessary Python libraries installed:

`pip install Flask pdfminer.six`

2. Clone the repository:

```
  git clone <repository-url> 
  cd DailyRead
```

3. Change all occurences of `your-path` with the correct path to the DailyRead repository.

4. Run the Flask app:
```
python app.py

```

5. Visit `http://localhost:5000` in your web browser to interact with the application.

## Usage

1. Drag & Drop or select a PDF file in the upload section of the web application.
2. Choose the start date for when you'd like the daily readings to commence.
3. Upload the file.
4. The application will extract text, split it into chapters, and send them daily via email based on the given start date.

## Note

- The email configurations in `scripts/send-email.py` should be modified according to your requirements. Always handle passwords securely, preferably using environment variables or secret management tools.

## Future Enhancements

- Implement a mechanism to schedule the emails automatically every day.
- Add more flexibility for custom email templates and multiple book support.
- Implement security measures for safely storing and accessing email passwords.

## Contributing

If you would like to contribute, please fork the repository and submit a pull request.
