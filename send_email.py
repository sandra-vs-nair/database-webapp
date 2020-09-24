# -----------------------------------------------------------
# Python code for sending email.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

from email.mime.text import MIMEText
import smtplib

#Function to send email.
def send_email(email,height,average,count):
    
    #Credentials of from-email.
    from_email="youremailid@gmail.com"
    from_password="yourpassword"
    
    #Information of the email to be sent.
    to_email=email
    subject="Average height statistics"
    message="Hello, Greetings from Height Collector.<br/><br/> \
    Your height is <strong>%s</strong>.<br/><br/> \
    The average height statistics is <strong>%s</strong>. <br/><br/> \
    The total number of people participated in this survery was <strong>%s</strong>" \
    %(height,average,count)
    
    #Initializing a MIMEText object.
    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    
    #Sending the email using outgoing smtp mail server for gmail. 
    #Ensure that 'allow less secure apps access' is turned on in your gmail account.
    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
    
    
    
