from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import random
from send_email import send_otp_email

app = FastAPI()

# ---------------- DATABASE ----------------
def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- MODELS ----------------
class RegisterUser(BaseModel):
    email: str
    password: str

class VerifyOTP(BaseModel):
    email: str
    otp: str

# ---------------- HOME ----------------
@app.get("/")
def home():
    return {"message": "Auth SMTP Project Running"}

# ---------------- REGISTER ----------------
@app.post("/register")
def register_user(user: RegisterUser):
    conn = get_db()
    cursor = conn.cursor()

    # Check if user exists
    cursor.execute("SELECT * FROM users WHERE email = ?", (user.email,))
    if cursor.fetchone():
        raise HTTPException(status_code=400, detail="User already exists")

    # Generate OTP
    otp = str(random.randint(100000, 999999))

    # Insert user
    cursor.execute("""
        INSERT INTO users (email, password, otp, is_verified)
        VALUES (?, ?, ?, 0)
    """, (user.email, user.password, otp))

    conn.commit()
    conn.close()

    # Send OTP via Email
    send_otp_email(user.email, otp)

    return {
        "message": "OTP sent to your email"
    }

# ---------------- VERIFY OTP ----------------
@app.post("/verify-otp")
def verify_otp(data: VerifyOTP):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND otp=?",
        (data.email, data.otp)
    )
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    cursor.execute(
        "UPDATE users SET is_verified=1 WHERE email=?",
        (data.email,)
    )

    conn.commit()
    conn.close()

    return {
        "message": "OTP verified successfully. You can now login."
    }



