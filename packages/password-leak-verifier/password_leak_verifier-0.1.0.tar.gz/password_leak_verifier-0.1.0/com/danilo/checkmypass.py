import getpass
import hashlib
import requests

def fetch_api_ready(hash_five_digits):
    url = 'https://api.pwnedpasswords.com/range/' + hash_five_digits
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'error fetching, status {response.status_code}')
    return response

def parse_response(response):
    return response.text

def hash_password(original_pwd):
    return hashlib.sha1(original_pwd.encode('utf-8')).hexdigest().upper()

def validate_hash(response, password_to_match):
    hashes = (hash_line.split(":") for hash_line in response.splitlines())
    for hash, count in hashes:
        if hash == password_to_match:
            return f'Your password was leaked {count} times'
    return 'Your password is SAFE!'


def pwned_api_check(password:str):
    hashed_password = hash_password(password)
    suffix, tail = hashed_password[:5], hashed_password[5:]
    response = fetch_api_ready(suffix)
    return validate_hash(parse_response(response), tail)



def execute_pwd_check_unsafe(argv):
    return [pwned_api_check(pwd) for pwd in argv]

def execute_pwd_check_safe():
    while True:
        pwd = getpass.getpass('Enter you password : ')
        print(pwned_api_check(pwd))
        if not pwd:
            return False

def execute_pwd_check_from_file(filename):
    with(open(filename)) as file:
        for line in file.readlines():
            print(pwned_api_check(line.strip()))

if __name__ == '__main__':
    execute_pwd_check_safe()