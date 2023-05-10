import ssl  # Adds a layer of security
import smtplib

from datetime import date
from configparser import ConfigParser
from email.message import EmailMessage
from smtplib import SMTPAuthenticationError


def send_email(subject: str, body: str) -> bool:
    """
    Function to send email to multiple receivers.

    Args:
        subject (str): Title of email
        body (str): Body of email

    Returns:
        bool: Returns true if it was sent.
    """
    config = ConfigParser()
    config.read("EmailSend\config.ini")

    email_sender = config['MAIN_BOT_USER']['email']
    email_password = config['MAIN_BOT_USER']['password']
    email_receiver = [config['EMAILS'][name] for name in config['EMAILS']]

    email = EmailMessage()
    email['From'] = email_sender
    email['To'] = email_receiver
    email['Subject'] = subject
    email.set_content(body)

    # Security layer
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(user=email_sender, password=email_password)
            smtp.sendmail(
                from_addr=email_sender,
                to_addrs=email_receiver,
                msg=email.as_string()
                )
            
        print(f"Email sent at {date.today()}.")
        return True
    
    except SMTPAuthenticationError as err:
        print(\
f"""
{'-'*50}
Incorrect email or password.
Remember that the password is from the two factor
authentication and not the account password.

Error: 
{err}
{'-'*50}
"""
        )
        
    
    


if __name__ == "__main__":
    send_email(
        subject=f"Testing bot {date.today()}.",
        body="""
        First line goes here.

        Second line.

        Third line.
        """
    )