import hashlib


def generate_hash(password, algorithm="sha256"):
    password_bytes = password.encode("utf-8")

    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }

    if algorithm not in algorithms:
        raise ValueError("Unsupported hashing algorithm.")

    return algorithms[algorithm](password_bytes).hexdigest()


def save_hash(password, algorithm, hashed_password):
    with open("hashes/sample_hashes.txt", "a") as file:
        file.write(f"Password : {password}\n")
        file.write(f"Algorithm: {algorithm.upper()}\n")
        file.write(f"Hash     : {hashed_password}\n")
        file.write("-" * 60 + "\n")