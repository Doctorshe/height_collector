from email.mime.text import MIMEText
import smtplib

def send_email(email, height, avarage_height, count):
    from_email="pytester3@gmail.com"
    from_password="Gmail123"
    to_email=email

    subject="Height data"
    message="Hey your height is <strong>%s</strong>. <br>The avarage height is <strong>%s</strong> and that is counted out of <strong>%s</strong> people. <br> Thanks." % (height, avarage_height, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)