import sqlite3

def create_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        otp TEXT,
        is_verified INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database and users table created successfully")

# Run the function
create_database()
