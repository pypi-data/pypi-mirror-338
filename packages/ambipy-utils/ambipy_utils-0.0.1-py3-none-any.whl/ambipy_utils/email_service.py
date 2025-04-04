import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail


class EmailService:
    SENDGRID_API_KEY: str

    def __init__(
        self,
        sendgrid_api_key: str,
    ):
        self.SENDGRID_API_KEY = sendgrid_api_key

    def send_grid(
        self,
        receivers: list[str],
        subject: str,
        content: str,
        from_email: str,
        from_name: str,
    ):
        sg = sendgrid.SendGridAPIClient(api_key=self.SENDGRID_API_KEY)

        email_from = Email(email=from_email, name=from_name)
        content = Content("text/html", content)
        mail = Mail(email_from, receivers, subject, content)

        mail_json = mail.get()
        return sg.client.mail.send.post(request_body=mail_json)
