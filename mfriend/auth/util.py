import hashlib
import os
import hmac

def hash_new_password(password: str) -> tuple[bytes, bytes]:
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.
    """
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, pw_hash

def is_correct_password(salt: str, pw_hash: str, password: str) -> bool:
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.
    """
    salt_bytes = bytes.fromhex(salt)
    pw_hash_bytes = bytes.fromhex(pw_hash)
    return hmac.compare_digest(
        pw_hash_bytes,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt_bytes, 100000)
    )