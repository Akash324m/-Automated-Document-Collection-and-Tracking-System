#  Automated Document Collection and Tracking System
This project automates the process of collecting documents from users via email, tracking submissions, updating records in an Excel workbook, and providing a web-based interface to monitor the status. It combines Excel macros, email automation, file storage, database tracking, and a Flask-based web interface.


System Architecture :

1. Excel Workbook
Maintains a record of required and received documents.

Contains user-specific data like email addresses, expected files, submission status, etc.

2. Macros (VBA)
Automates the process of:

Extracting user info.

Generating email reminders.

Updating records based on file submissions.

Reads and writes to the Excel workbook.

3. Email System
Sends reminder emails to users using VBA/macros or Python.

Waits for replies containing attachments (documents).

Emails are parsed for attachments which are extracted and stored.

4. Users
Receive reminders.

Reply to emails with required documents attached.

5. Attachments
Documents submitted by users via email.

Saved into a local or cloud-based storage.

Metadata (filename, sender, timestamp) is logged into the database.

6. Database
Stores file tracking metadata:

Who submitted

What files were submitted

When they were submitted

Used as a file system backend for the web dashboard and tracking logic.

7. Python Scripts
Perform the following:

Email parsing using IMAP/Outlook integration.

Attachment extraction and saving.

Updating the database.

Interfacing with Excel (using openpyxl or xlwings) for updates.

Triggering macro updates if needed.

8. Flask Web Application
Framework used: Flask (Python).

Provides:

Dashboard for administrators to monitor who has submitted.

Status indicators (e.g., pending, completed).

Optionally allows file re-download or search.

Hosted either locally or on a server.

9. Webpage
User-facing interface to:

View real-time status.

Monitor pending/completed uploads.

(Optional) Allow upload via web if email is not feasible.

Workflow
Initiation

Admin prepares Excel workbook with user info.

Macros trigger email reminders.

User Submission

Users receive email → reply with required attachments.

Attachment Handling

Python script checks mailbox.

Downloads attachments.

Updates the database.

Files are stored in a structured directory (by user/date/type).

Tracking

Database updated with submission metadata.

Python updates Excel workbook for visual/logical tracking.

Visualization

Flask app displays current submission status.

Webpage accessible to admin/stakeholders.

Tech Stack
Component	Tool / Language
Backend	Python
Web Framework	Flask
Database	SQLite / PostgreSQL / Filesystem
Email	Outlook / Gmail API / IMAP
Excel	Excel + VBA Macros
Hosting	Localhost / Heroku / PythonAnywhere
UI	HTML + CSS + JS (basic Flask template)

Modules and Functions
Module	Responsibility
email_handler.py	Connect to inbox, fetch emails, extract attachments
file_saver.py	Save attachments to filesystem, create folders
db_updater.py	Insert/update records in the database
excel_updater.py	Update Excel sheet using openpyxl or trigger macros
webapp.py	Flask routes to display dashboard
vba_macro.bas	Script for generating emails and updating workbook

Future Enhancements
Add user authentication to webpage.

Allow document upload via webpage.

Add version control for submitted files.

Integrate SMS/WhatsApp reminders.

Host Flask app securely with SSL and login protection.

Conclusion
This project streamlines the document collection process and improves visibility and accountability through automation. It reduces manual follow-ups and errors, and can be scaled for various departments or organizations.