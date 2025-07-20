import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='subhanali1212w@gmail.com',  # Must be verified sender or domain in SendGrid
    to_emails='bsdsf22m030@pucit.edu.pk',
    subject='Testing sending email from python using sendGrid twilio',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

try:
    sg = SendGridAPIClient('API_GOES_HERE')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)

