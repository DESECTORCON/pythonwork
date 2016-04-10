import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class mail():

    class sender():
        def mailsender(userID, subject, Contents):
            me = "choeminjun@naver.com"
            my_password = r"minjun5627"
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
            s.login('choeminjun@naver.com', 'minjun5627')

            s.sendmail(me, you, msg.as_string())
            s.quit()

    class getter():
        def mailIdGetter():
            mainV = open('email', 'r')
            data = mainV.readlines()
            return ''.join(data)