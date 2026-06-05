import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_alert(product_name, current_price, target_price, url):
    subject = f"Price Drop Alert: {product_name}"
    body = f"""
    Good news! The price has dropped!

    Product      : {product_name}
    Current Price: Rs.{current_price}
    Your Target  : Rs.{target_price}
    Buy Now      : {url}
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_SENDER")
    msg["To"] = os.getenv("EMAIL_RECEIVER")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("EMAIL_SENDER"), os.getenv("EMAIL_PASSWORD"))
            server.send_message(msg)
            print(f"Email alert sent for {product_name}!")
    except Exception as e:
        print(f"Failed to send email: {e}")