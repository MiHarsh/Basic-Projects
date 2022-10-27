##import lib

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

##credintials
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('YourMail@gmail.com', 'Your Password')


##message build
msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(MIMEText(text))

##attaching files

with open(one_attachment, 'rb') as f:
    file = MIMEApplication(
        f.read(), name=os.path.basename(one_attachment)
    )
    file['Content-Disposition'] = f'attachment; \
    filename="{os.path.basename(one_attachment)}"'
    msg.attach(file)


to = ["klm@gmail.com", "xyz@gmail.com", "abc@gmail.com"]
smtp.sendmail(from_addr="Your Login Email",
              to_addrs=to, msg=msg.as_string())
              
smtp.quit()