import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# ---------------------------
# USERS TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
)
""")

# ---------------------------
# ROLES TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS roles (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT NOT NULL UNIQUE
)
""")

# ---------------------------
# PERMISSIONS TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS permissions (
    permission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    permission_name TEXT NOT NULL UNIQUE
)
""")

# ---------------------------
# USER ROLES TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_roles (
    user_id INTEGER,
    role_id INTEGER,
    PRIMARY KEY(user_id, role_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(role_id) REFERENCES roles(role_id)
)
""")

# ---------------------------
# ROLE PERMISSIONS TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS role_permissions (
    role_id INTEGER,
    permission_id INTEGER,
    PRIMARY KEY(role_id, permission_id),
    FOREIGN KEY(role_id) REFERENCES roles(role_id),
    FOREIGN KEY(permission_id) REFERENCES permissions(permission_id)
)
""")

# ---------------------------
# BOOKS TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    status TEXT DEFAULT 'Available'
)
""")

# ---------------------------
# BORROWINGS TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS borrowings (
    borrowing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    book_id INTEGER,
    borrow_date DATE,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(book_id) REFERENCES books(book_id)
)
""")

# ---------------------------
# AUDIT LOG TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    action TEXT,
    status TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# ---------------------------
# INSERT SAMPLE DATA
# ---------------------------

roles = [
    ("Student",),
    ("Librarian",),
    ("Admin",)
]

permissions = [
    ("View Books",),
    ("Borrow Books",),
    ("Add Books",),
    ("Delete Books",),
    ("Change Roles",)
]

users = [
    ("Alice", "pass123"),
    ("Bob", "pass456"),
    ("Charlie", "pass789")
]

books = [
    ("Database Systems", "Elmasri"),
    ("Python Basics", "John Smith"),
    ("Operating Systems", "Galvin")
]

cursor.executemany(
    "INSERT OR IGNORE INTO roles(role_name) VALUES(?)",
    roles
)

cursor.executemany(
    "INSERT OR IGNORE INTO permissions(permission_name) VALUES(?)",
    permissions
)

cursor.executemany(
    "INSERT OR IGNORE INTO users(username,password_hash) VALUES(?,?)",
    users
)

cursor.executemany(
    "INSERT OR IGNORE INTO books(title,author) VALUES(?,?)",
    books
)

conn.commit()
conn.close()

print("library.db created successfully!")