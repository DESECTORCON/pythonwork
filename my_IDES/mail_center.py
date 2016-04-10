import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from NOTE import getID_password


class mail():

    class securitysys():
        def __set__(self, instance, value):
            self += 1
        def userlogin(user, userp):
            ID, password = getID_password()




    class sender():
        def mailsender(me, my_password,you, subject, Contents):
            you = userID

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = me
            msg['To'] = you

            html = '<html><body><p>%s</p></body></html>' % (Contents)
            part2 = MIMEText(html, 'html')

            msg.attach(part2)

            # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
            s = smtplib.SMTP_SSL('smtp.naver.com', 465)
            # uncomment if interested in the actual smtp conversation
            # s.set_debuglevel(1)
            # do the smtp auth; sends ehlo if it hasn't been sent already
            s.login(me, my_password)

            s.sendmail(me, you, msg.as_string())
            s.quit()


    class getter():
        def mailIdGetter(filename):
            mainV = open(filename, 'r')
            data = mainV.readlines()
            return ''.join(data)

