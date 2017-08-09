import base64

import httplib2
import os

from apiclient import discovery
from googleapiclient import errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
CLIENT_SECRET_FILE = 'client_secret.json'


def get_credentials():
    run_dir = os.getcwd()
    credential_dir = os.path.join(run_dir, 'credential')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'gmail-user-auth.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(os.path.join(credential_dir, CLIENT_SECRET_FILE),
                                              SCOPES)
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def send_email(service, emails):
    sender = "me"
    subject = "Teste do Gmail API"
    message = create_email(sender, emails, subject)
    try:
        message = (service.users().messages().send(userId=sender, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

def create_email(sender, to, subject):
    message = MIMEMultipart('related')
    message['from'] = sender
    message['to'] = to
    message['subject'] = subject

    body = MIMEMultipart('alternative')
    message.attach(body)

    html = "<h1>HELLO WORLD</h1>"

    format_html = MIMEText(html, 'html')

    body.attach(format_html)

    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    send_email(service, "peticormei@gmail.com")



if __name__ == '__main__':
    main()