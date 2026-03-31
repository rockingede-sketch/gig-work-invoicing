from email_validator import validate_email, EmailNotValidError, EmailSyntaxError, EmailUndeliverableError

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

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} ("{self.email}", "{self.firstname}", "{self.lastname}")'
    
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
    
    def sendConfirmation(self)->bool:
        "Check for the template"
        
        return True