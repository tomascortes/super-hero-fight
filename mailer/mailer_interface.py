from .mailgun_sender import send_mailgun_email

def ask_for_email() -> str:
    email = input("Please enter your email address: ")
    while "@" not in email:
        email = input("Please enter a valid email address (requires @): ")
    return email

def send_results(body: str) -> str:
    email = ask_for_email()
    return send_mailgun_email(email, body)
