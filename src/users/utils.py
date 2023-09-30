import bcrypt


def password_hashing(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def password_verification(password: str, stored_password: bytes):
    return bcrypt.checkpw(password.encode('utf-8'), stored_password)
