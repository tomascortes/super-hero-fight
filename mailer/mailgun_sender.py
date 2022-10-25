# external libraries
import requests
import os
# internal libraries
from .constants import MAILGUN_ADRESS, MAILGUN_URL


def send_mailgun_email(email_adress, body) -> bool:
    MAIL_GUN_API_KEY = os.getenv('MAIL_GUN_API_KEY')
    auth = ("api", MAIL_GUN_API_KEY)
    body=body.replace('\n', '<br>')
    try:
        response=requests.post(
            MAILGUN_URL,
            auth=auth,
            data={"from": MAILGUN_ADRESS,
                "to": [email_adress],
                "subject": "Summary simulation Tomás Cortés",
                'html': html_generator(body)})
    except:
        raise Exception("Error connecting to mailgun")
    if response.status_code == 200:
        return True
    else:
        return False


def html_generator(body) -> str:
    return f'''<html><body>
                {body}
                </body></html>'''
