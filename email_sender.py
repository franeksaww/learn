import smtplib
import getpass
import time

def send_email(subject, text):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(sender, pasword)
        mesage = 'Subject: {}\n\n{}'.format(subject, text)
        server.sendmail(sender, reciver, mesage)
        server.quit()
        print('Success email send!')
    except Exception:
        print('Email fail to send')

sender = input('Type your email: ')
time.sleep(1)
print('hasło')
pasword = getpass.getpass('Enter your password: ')
time.sleep(1)
reciver = input('Destination adress: ')
subject = input('Subject: ')
text = input('Text: ')
send_email(subject, text)


