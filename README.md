📧 Email OTP Authentication System (FastAPI) :
This project is a secure user authentication system built using FastAPI, SQLite, and SMTP.It allows users to register using their email and verifies their identity using a One-Time Password (OTP) sent via email.

🚀 Features

User Registration

OTP Generation & Verification

Email OTP Sending using SMTP

Secure Authentication Flow

SQLite Database Integration

FastAPI Backend

Swagger UI for API Testing

🛠️ Technologies Used :

Python

FastAPI

SQLite

SMTP (Gmail)

Pydantic

Git & GitHub :
📁 Project Structure
email-auth-project/
│
├── main.py
├── database.py
├── send_email.py
├── requirements.txt
├── README.md
├── .gitignore
└── users.db
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/VaishnaviHiremath12/email-auth-project.git
cd email-auth-project

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create Database
python database.py

4️⃣ Run the Application
uvicorn main:app --reload

5️⃣ Open Swagger UI
http://127.0.0.1:8000/docs

📌 API Endpoints
🔹 Register User

POST /register

{
  "email": "yourmail@gmail.com",
  "password": "12345"
}


➡️ Sends OTP to email

🔹 Verify OTP

POST /verify-otp

{
  "email": "yourmail@gmail.com",
  "otp": "123456"
}


➡️ Verifies user account

📧 Email Configuration

Gmail SMTP is used

App Password is required (not Gmail password)

Enable 2-Step Verification in Google Account

Generate App Password for Mail

🔐 Security Features

OTP-based authentication

Duplicate user prevention

Email verification

Secure SMTP login

Clean API structure

📌 Project Outcome

✔ Secure authentication system
✔ Real-world backend implementation
✔ Email verification using SMTP
✔ Resume-ready project
✔ GitHub portfolio project
