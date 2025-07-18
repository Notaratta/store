import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery import shared_task
import os

def send_email(to_email, subject, html_content):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = os.environ.get('GMAIL_USER')
    smtp_pass = os.environ.get('GMAIL_PASS')
    
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)

@shared_task
def send_order_confirmation_email(to_email, status, plan_name, ):
    subject = 'Your Order Confirmation'
    html_content = f'''
    <h2>Order Confirmation</h2>
    <p>Thank you for your purchase! Here is your receipt:</p>
    <ul>
        <li><b>Account Email:</b> {to_email}</li>
        <li><b>Status:</b> {status}</li>
        <li><b>Plan Name:</b> {plan_name}</li>
    </ul>
    <p>If you have any questions, reply to this email.</p>
    '''
    send_email(to_email, subject, html_content) 