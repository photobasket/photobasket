import smtplib

def send_email(receiver, subject, body):
        gmail_user = "photonet297@gmail.com"
        gmail_pwd = "photonet1234"
        gmail_from = 'photonet297@gmail.com'
        gmail_to = [receiver]

        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (gmail_from, ", ".join(gmail_to), subject, body)
        try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(gmail_from, gmail_to, message)
                server.close()
                print 'successfully sent the mail'
        except:
                print "failed to send mail"
