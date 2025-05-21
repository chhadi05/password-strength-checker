import hashlib
import requests

def get_sha1_hash(password):
    """Returns the SHA1 hash of the password in uppercase."""
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1

def check_password_breach(password):
    """Checks how many times a password has been seen in breaches."""
    sha1_password = get_sha1_hash(password)
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise RuntimeError(f"Error fetching data: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
        return None

    # Check if suffix is in the list of returned hashes
    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return int(count)

    return 0  # Not found in breaches

