# Keikkalaskutus

The gig‑work invoicing system enables independent workers to create invoices for completed work and receive payment for salaries, fees, and reimbursable expenses. The platform supports both light entrepreneurs and employees, allowing each user to choose their role when creating an invoice.

After registering, the gig worker provides the necessary personal and financial information, including:</br>
    • Personal and address details </br>
    • Tax information (for employees) </br>
    • Bank account details </br>
    • Work category/industry </br>
    • Client information </br>
    • Work details such as date, hours worked, workplace, and travel expenses </br>
Once the required information is submitted, the worker can generate an invoice for the completed task, which is then processed for payment.

<h2>Features</h2>
1. <b>User Registration & Authentication : </b> Gig workers can create an account and manage their profile.</br>
2. <b>Role Selection : </b> Users choose between light entrepreneur or employee when creating an invoice.</br>
3. <b>Invoice Creation : </b> Workers can generate invoices for completed tasks, including:</br>
              ◦ Work dates and hours 
              ◦ Workplace details 
              ◦ Task description and industry 
              ◦ Travel expenses and reimbursements </br>
4. <b>Client Management : </b> Add and store client details for repeated invoicing. </br>
5. <b>Payment Processing : </b> Supports salary, fees, and reimbursable expenses with bank account details.</br>
6. <b>Tax Information Handling : </b> Employees can provide tax card details for correct withholding.</br>
7. <b>Dashboard & Invoice History : </b> View past invoices, statuses, and payment history.

<h2>Tech Stack</h2>
 <b>Languages</b> </br> 
    • Python </br> 
    • JavaScript </br> 
    • HTML5, CSS3 </br> 
<b>Frameworks & Libraries</b> </br> 
    • Django (Templates, Forms, Auth, ORM) </br> 
    • Bootstrap </br> 
<b>Database</b> </br> 
    • SQLite — lightweight relational database used for development and local storage </br> 
<b>Integrations</b> </br> 
    • Brevo — email service used for sending account activation links 

<h2>Installation & Setup</h2>

1. <b> Clone the Repository </b> </br>

    git clone REPO_URL </br>
    cd YOUR_PROJECT_FOLDER </br>

2. <b> Create & Activate Virtual Environment  </b> </br>

    Using venv (VS Code supports this automatically): </br>
    <b>Windows</b> </br>
    python -m venv venv </br>
    venv\Scripts\activate </br>
    Ensure VS Code is using the venv interpreter </br>
    In VS Code: </br>
        1. Press Ctrl+Shift+P </br>
        2. Select Python: Select Interpreter </br>
        3. Choose the one inside your project, something like: C:\Projects\gig-work-invoicing\backend\venv\Scripts\python.exe </br>
        4. If not found, click Enter interpreter path and browse to it. </br>
    
3.  <b>Install Dependencies </b> </br>

    pip install django </br>

4.  <b>Set Up Environment Variables </b> </br>

    Create a .env file in the project root: </br>
    
    EMAIL_HOST=smtp-relay.brevo.com </br>
    EMAIL_HOST_USER=your-brevo-api-key </br>
    EMAIL_HOST_PASSWORD=your-brevo-api-key </br>
    EMAIL_PORT=587 </br>
    
    In VS code settings, enable this setting - use ENV file </br>

5.  <b>Apply Migrations  </b> </br>

    python manage.py migrate </br>

6.  <b>Run the Development Server  </b> </br>

    python manage.py runserver </br>
    
    Your project will be available at: </br>
    http://127.0.0.1:8000 </br>

## My Contribution (Sreevidya Ch)

I implemented the complete user authentication and onboarding flow for the project, including:

- Login with Django’s built‑in authentication system  
- User registration with validation and inactive‑user creation  
- Account activation via Brevo email service  
- Profile completion workflow (contact, bank, and tax details)  
- Saving customer data and updating profile status in the database  
- Forgot Password functionality with email‑based reset flow  
