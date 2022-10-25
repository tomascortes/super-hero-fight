from .mailgun_sender import send_mailgun_email

def ask_for_email() -> str:
    email = input("Please enter your email address: ")
    while "@" not in email:
        email = input("Please enter a valid email address (requires @): ")
    return email

def send_results(body: str) -> str:
    confirmation = input("Do you want to send the results to your email? (y/n): ")
    if confirmation != "y":
        return False
    email = ask_for_email()
    return send_mailgun_email(email, body)
