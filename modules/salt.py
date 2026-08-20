import hashlib
import secrets


def generate_salt(length=16):
    """
    Generate a cryptographically secure random salt.
    """
    return secrets.token_hex(length // 2)


def generate_salted_hash(password, algorithm="sha256"):

    salt = generate_salt()

    data = (password + salt).encode("utf-8")

    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }

    hashed = algorithms[algorithm](data).hexdigest()

    return salt, hashed