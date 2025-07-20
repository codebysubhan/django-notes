import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='subhanali1212w@gmail.com',  # Must be verified sender or domain in SendGrid
    to_emails='bsdsf22m030@pucit.edu.pk',
    subject='Testing sending email from python using sendGrid twilio',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)

