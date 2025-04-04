import os.path
import base64
import mimetypes
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


class PyAlert:
    """
    A class to send email notifications using the Gmail API.
    """

    def __init__(self, credential, token):
        """
        Initialize the PyAlert class by setting up Google API credentials.

        Parameters:
            credential (str): Path to the client credentials JSON file.
            token (str): Path to the token file to store user credentials.
        """
        self.creds = self.get_credentials(credential, token)
        self.service = build('gmail', 'v1', credentials=self.creds)
        self.sender = "your-email@gmail.com"  # Replace with your Gmail address
        self.subject = "PyAlert Notification"

    def update_sender(self, sender):
        """Update the sender email address."""
        self.sender = sender

    def update_subject(self, subject):
        """Update the email subject line."""
        self.subject = subject

    def get_credentials(self, credential, token, scopes=["https://www.googleapis.com/auth/gmail.send"]):
        """
        Authenticate and retrieve Google API credentials.

        Parameters:
            credential (str): Path to the client credentials JSON file.
            token (str): Path to the token file to store user credentials.

        Returns:
            Credentials: Validated Google API credentials.
        """
        creds = None

        # Ensure credentials.json exists
        if not os.path.exists(credential):
            raise FileNotFoundError(f"Credential file '{credential}' not found. Please provide a valid path.")

        # Try to load existing token
        try:
            if os.path.exists(token):
                creds = Credentials.from_authorized_user_file(token, scopes)
        except Exception as e:
            print(f"Warning: Token file '{token}' is invalid or corrupted. Re-authenticating... ({e})")
            creds = None  # Force re-authentication

        # If credentials are missing or expired, refresh or request login
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credential, scopes)
                creds = flow.run_local_server(port=0)

            # Save new credentials
            with open(token, 'w') as token_file:
                token_file.write(creds.to_json())

        return creds

    def create_message(self, to, subject, message_text, file_path=None):
        """
        Create an email message with an optional file attachment.

        Parameters:
            to (str): Recipient's email address.
            subject (str): Email subject.
            message_text (str): Email body.
            file_path (str, optional): Path to the file to attach.

        Returns:
            dict: A dictionary containing the encoded email message.
        """
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = self.sender
        message['subject'] = subject

        # Default message text
        email_body = message_text

        # Attach file if provided and valid
        if file_path:
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)

                # Ensure file is within the 5MB limit
                if file_size > 5 * 1024 * 1024:
                    email_body += f"\n\n[NOTE: The file '{os.path.basename(file_path)}' was not attached because it exceeds the 5MB limit.]"
                else:
                    with open(file_path, 'rb') as attachment:
                        mime_type, _ = mimetypes.guess_type(file_path)
                        mime_main, mime_sub = (mime_type or "application/octet-stream").split("/", 1)
                        mime_part = MIMEBase(mime_main, mime_sub)
                        mime_part.set_payload(attachment.read())

                        # Correct base64 encoding
                        encoders.encode_base64(mime_part)

                        mime_part.add_header(
                            'Content-Disposition',
                            f'attachment; filename="{os.path.basename(file_path)}"'
                        )
                        message.attach(mime_part)
            else:
                email_body += f"\n\n[NOTE: The file '{file_path}' was not attached because it was not found.]"

        # Attach the email body
        message.attach(MIMEText(email_body, 'plain'))

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw_message}

    def send_email(self, recipient, message, file_path=None):
        """
        Send an email using the Gmail API with an optional attachment.

        Parameters:
            recipient (str): Recipient's email address.
            message (str): Email body.
            file_path (str, optional): Path to the file to attach.

        Returns:
            dict: Response from the Gmail API or error message.
        """
        try:
            message_payload = self.create_message(recipient, self.subject, message, file_path)
            if message_payload:
                sent_message = self.service.users().messages().send(userId="me", body=message_payload).execute()
                print(f"✅ Email sent successfully to {recipient}")
                return sent_message
            else:
                print("❌ Failed to create email message.")
                return {"error": "Failed to create email message."}
        except Exception as e:
            error_msg = f"❌ Error sending email to {recipient}: {e}"
            print(error_msg)
            return {"error": error_msg}

    def push_notification(self, target, message, file_path=None):
        """
        Send an email notification with an optional file attachment.

        Parameters:
            target (str): Recipient's email address.
            message (str): Notification message.
            file_path (str, optional): Path to the file to attach.

        Returns:
            dict: Response from the Gmail API or error message.
        """
        return self.send_email(target, message, file_path)