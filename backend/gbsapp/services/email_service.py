from email_validator import validate_email, EmailNotValidError, EmailSyntaxError, EmailUndeliverableError
import os,smtplib
from email.mime.text import MIMEText

#Used for testing this class, directly load the env. variables
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(__file__).parent.parent.parent / "email_settings.env")
#print(Path(__file__).parent.parent.parent / "email_settings.env")

class EmailService:
    """
        Service class for handling all email operations
        in the Gig Billing System.

        Create the email service with the recipient immediately
        The email address will be verified on sending email or it can be manually verified. Verification is only carried out once by the sending methods. however when the verify() method is called, it always attempts to verify.

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
        self.verified = False

    """
    Returns a string reprentation of the EmailService Object

    Parameters:
        None

    Returns:
        string: Prints class name, email, firstname, lastname in the EmailService object
    """

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} ("{self.email}", "{self.firstname}", "{self.lastname}. DNS Verified: {str(self.verified)}")'
    
    """
    Returns a string of the created EmailService Object

    Parameters:
        None

    Returns:
        string: Prints class name, email, firstname, lastname in the EmailService object
    """
    def __str__(self) -> str:
        return f'{self.__class__.__name__} ("{self.email}", "{self.firstname}", "{self.lastname}. DNS Verified: {str(self.verified)}")'
    
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
    def sendConfirmationRequest(self)->bool:
        #Verify the DNS of the recipient email address
        if not self.verified:
            self.verifyEmail()
            if not self.verified: return False
        
        "Check for the template"
        try:
            template_dir = os.path.join(os.path.dirname(__file__), "../email_templates/confirmation")

            with open(os.path.join(template_dir, "confirmation.txt")) as f:
                text_body = f.read().format(
                    first_name=self.firstname,
                    last_name=self.lastname,
                    email=self.email,
            )

            #with open(os.path.join(template_dir, "confirmation.html")) as f:
            #    html_body = f.read().format(
            #        first_name=self.firstname,
            #        last_name=self.lastname,
            #        email=self.email,
            #)
                
            return self.sendMail(subject='GigBookingSystem Confirmation',
                      msgbody=text_body,
                      recipient=self.email)

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Email template not found: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Error occurred: {e}")
            return False

    
    @classmethod
    def sendMail(cls,subject,msgbody,recipient)->bool:

        msg = MIMEText(msgbody, "plain")

        if os.environ.get("EMAIL_FROM") is None:
            raise RuntimeError('EMAIL_FROM Env. Variables not set')

        msg["Subject"] =    str(subject)
        msg["From"] =       str(os.environ.get("EMAIL_FROM"))
        msg["To"] =         str(recipient)
        
        smtp = {}
        smtp["host"] = str(os.environ.get("EMAIL_HOST"))
        smtp['port'] = str(os.environ.get("EMAIL_PORT"))
        smtp['user'] = str(os.environ.get("EMAIL_USER"))
        smtp['pass'] = str(os.environ.get("EMAIL_PASS"))

        try:
            with smtplib.SMTP(smtp["host"], int(smtp['port'])) as server:
                if smtp["host"] != "localhost":
                    server.starttls()
                    server.login(smtp['user'], smtp['pass'])
                server.sendmail(msg["From"] , [msg["To"]], msg.as_string())
            return True

        except Exception as e:
            raise RuntimeError(f"Error occurred: {e}")
            return False
