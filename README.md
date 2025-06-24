**System Architecture**
1. Excel Workbook
Serves as the primary record-keeping tool.

Stores user-specific information such as email addresses, expected documents, and submission status.

2. Macros (VBA)
Automates:

Extracting user details from the Excel workbook.

Sending reminder emails.

Updating the workbook upon file submission.

Reading and writing data within Excel.

3. Email System
Sends automated reminders via VBA or Python.

Monitors inbox for replies with attachments.

Extracts and stores attachments from incoming emails.

4. Users
Receive automated reminders.

Submit required documents by replying to the email with attachments.

5. Attachments
User-submitted documents are stored in an organized directory.

Metadata such as sender, file name, and timestamp is logged for tracking.

6. Database
Logs metadata related to file submissions:

Submitter identity

Document details

Submission time

Supports the web dashboard and document tracking.

7. Python Scripts
Handle backend automation, including:

Email parsing (via IMAP or Outlook integration)

File extraction and storage

Database updates

Excel manipulation (using openpyxl or xlwings)

Optional macro triggering

8. Flask Web Application
Built using Flask (Python framework).

Provides an admin dashboard with features like:

Submission tracking and status indicators (e.g., pending, complete)

File search and download (optional)

Hosted locally or on cloud platforms

9. Webpage
A user-friendly interface for stakeholders to:

View submission statuses in real time

Monitor outstanding and completed uploads

**Workflow**

Initiation
   ↓
Admin prepares the Excel workbook with user data.
   ↓
Macros generate and send email reminders.
   ↓
User Submission
   ↓
Users reply with required document attachments.
   ↓
Attachment Handling
   ↓
Python script scans the inbox and downloads attachments.
   ↓
Database and File System Update
   ↓
Submission metadata logged; files organized by user/date/type.
   ↓
Tracking
   ↓
Python updates Excel workbook with current status.
   ↓
Visualization
   ↓
Flask app displays data on the admin dashboard.
   ↓
Stakeholders access the webpage for status updates.


**Tech Stack**
| Component     | Technology                              |
| ------------- | --------------------------------------- |
| Backend       | Python                                  |
| Web Framework | Flask                                   |
| Database      | SQLite / PostgreSQL / FileSystem        |
| Email         | Outlook / Gmail API / IMAP              |
| Excel         | Excel + VBA Macros                      |
| Hosting       | Localhost / Heroku / PythonAnywhere     |
| Frontend UI   | HTML, CSS, JavaScript (Flask Templates) |


**Modules and Responsibilities**
| Module             | Description                                             |
| ------------------ | ------------------------------------------------------- |
| `email_handler.py` | Connects to inbox, fetches emails, extracts attachments |
| `file_saver.py`    | Organizes and saves attachments into directories        |
| `db_updater.py`    | Inserts and updates records in the database             |
| `excel_updater.py` | Updates the Excel workbook or triggers macros           |
| `webapp.py`        | Handles Flask routes and dashboard logic                |
| `vba_macro.bas`    | VBA script for sending emails and updating Excel        |

**Future Enhancements**
Implement secure user authentication for the web portal

Enable document uploads directly through the webpage

Introduce version control for submitted files

Add support for SMS or WhatsApp-based reminders

Secure Flask app with HTTPS and login access
