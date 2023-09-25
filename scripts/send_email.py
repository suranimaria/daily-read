import smtplib
import ssl
import re
import os
import sys
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main(date_str: str):
    """Main function to process and send the chapter email."""

    # Starting reference date
    start_date = date(2022, 5, 14)
    
    # Convert given string date to a datetime object
    curr_date = date.fromisoformat(date_str)
    
    # Calculate days passed since the starting date
    book_idx = (curr_date - start_date).days

    # SMTP configurations
    smtp_server = "smtp.gmail.com"
    port = 465  # SSL
    password = 'Marcel123!'
    sender_email = 'marceltd.calina@gmail.com'
    receiver_email = 'surani_maria@yahoo.com'
    
    # Set up email headers
    message = MIMEMultipart('alternative')
    message['Subject'] = "Today's Chapter"
    message["From"] = 'Daily Wake-Up Reading'
    message["To"] = receiver_email
    
    # List of books (expandable in the future)
    books = ['maurelius']

    for book in books:
        chapters = os.listdir(f'your-path/DailyRead/chapters/{book}')
        total_chapters = len(chapters)

        if book_idx < total_chapters:
            chapter_path = f'your-path/DailyRead/chapters/{book}/{book_idx}.txt'
            with open(chapter_path, 'r') as chapter_file:
                chapter_content = chapter_file.read()

            # Extract chapter title and format text
            chapter_title = re.match(r'[A-Za-z ]+\+', chapter_content).group()[:-1]
            chapter_content = process_text(chapter_content)

            # Convert text to HTML
            html_content = generate_html(chapter_title, chapter_content)

            # Attach and send the email
            email_body = MIMEText(html_content, 'html')
            message.attach(email_body)

            context = ssl._create_unverified_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.set_debuglevel(1)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())

            break
        
        # Deduct the total chapters in this book and move on to the next book
        book_idx -= total_chapters

def process_text(text: str) -> str:
    """Clean and format the chapter text."""
    text = re.sub(r'^[A-Za-z ]+\+', '', text)
    text = re.sub(r'[\f\n]+', '\n', text)
    text = re.sub(r'-\n', '', text)
    text = re.sub(r'(?<=[A-Za-z,;0-9\(\)\"\' ])[\f\n](?=[A-Za-z,;0-9\(\)\"\' ])', ' ', text)
    text = re.sub(r'(?<=[-])[\f\n](?=[A-Za-z-,;0-9\(\)])', '', text)
    return re.sub("\n", r'<br />', text)

def generate_html(title: str, content: str) -> str:
    """Generate an HTML representation of the chapter."""
    return f"""\
    <html>
    <body style="width: 100%; min-height: 1000px; background-color: #030303; color: #dbdbdb; font-size: 14px;">
        <div style="width: 90%; margin: auto; margin-top: 50px">
            <h3>{title}</h3>
            <p>{content}</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    given_date = sys.argv[1]
    main(given_date)
