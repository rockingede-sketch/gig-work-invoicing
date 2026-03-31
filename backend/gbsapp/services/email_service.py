from email_validator import validate_email, EmailNotValidError, EmailSyntaxError, EmailUndeliverableError
import os
from email.mime.text import MIMEText

class EmailService:
    """
        Service class for handling all email operations
        in the Gig Billing System.
        """
    def __init__(self,email:str,firstname:str,lastname:str):
        """
        Initiates a service for a recipient. 

        Parameters:
            email (string): Email address of the recipient
            firstname (string): First name of the recipient
            lastame (string): Last name of the recipient
        
        Raises:
            ValueError: If any required field is missing or blank

        Returns:
           None
        """
        #Check values are specified
        if not email or not email.strip():
            raise ValueError("Email address is required.")
        if not firstname or not firstname.strip():
            raise ValueError("First name is required.")
        if not lastname or not lastname.strip():
            raise ValueError("Last name is required.")
        
        #Check the email address format, will raise EmailSyntaxError. We don't need to check dns lookup right now. Use the verify class method for this.
        try:
            emailinfo = validate_email(email, check_deliverability=False) 
        except EmailSyntaxError as e:
            raise ValueError(f"Email address is not correctly formated ({email}).")
        
        self.email = emailinfo.normalized
        self.firstname = firstname.strip()
        self.lastname = lastname.strip()

    """
    Returns a string reprentation of the EmailService Object

    Parameters:
        None

    Returns:
        string: Prints class name, email, firstname, lastname in the EmailService object
    """

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} ("{self.email}", "{self.firstname}", "{self.lastname}")'
    
    """
    Returns a string of the created EmailService Object

    Parameters:
        None

    Returns:
        string: Prints class name, email, firstname, lastname in the EmailService object
    """
    def __str__(self) -> str:
        return f'{self.__class__.__name__} ("{self.email}", "{self.firstname}", "{self.lastname}")'
    
    """
    Performs a DNS lookup on the email address 

    Parameters:
        None

    Returns:
        bool: True if the email passes DNS verification, False otherwise
    """
    def verifyEmail(self)->bool:
        try:
            emailinfo = validate_email(self.email, check_deliverability=True)
        except (EmailSyntaxError, EmailUndeliverableError):
            self.verified = False
            return False
        
        self.verified = True
        return self.verified
    """
    Sends a confirmation email to the recipient using HTML and plain text templates.
    Templates are loaded from email_templates/confirmation/.

    Parameters:
        None

    Returns:
        bool: True if the email was sent successfully, False otherwise
    """
    def sendConfirmation(self)->bool:
        "Check for the template"
        try:
            template_dir = os.path.join(os.path.dirname(__file__), "../email_templates/confirmation")

            with open(os.path.join(template_dir, "confirmation.txt")) as f:
                text_body = f.read().format(
                    first_name=self.firstname,
                    last_name=self.lastname,
                    email=self.email,
            )

            with open(os.path.join(template_dir, "confirmation.html")) as f:
                html_body = f.read().format(
                    first_name=self.firstname,
                    last_name=self.lastname,
                    email=self.email,
            )
                
            msg = MIMEText(text_body, "plain")
            msg["Subject"] = "Booking Confirmation"
            msg["From"] = os.environ.get("EMAIL_FROM")
            msg["To"] = self.strRecipient

            with smtplib.SMTP(os.environ.get("EMAIL_HOST"), int(os.environ.get("EMAIL_PORT", 587))) as server:
                server.starttls()
                server.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASSWORD"))
                server.sendmail(msg["From"], [msg["To"]], msg.as_string())

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Email template not found: {e}") from e
        except Exception:
                return False

        return True