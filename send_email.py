import smtplib
from email.mime.text import MIMEText

def send_otp_email(receiver_email, otp):
    sender_email = "hiremathvaishnavi2003@gmail.com"
    app_password = "zingfabutjmmftmz"

    subject = "OTP Verification"
    body = f"""
Hello,

Your OTP for verification is: {otp}

Do not share this OTP with anyone.

Regards,
Auth SMTP Project
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    server.quit()
