import sys
import requests
import hashlib


def req_api(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    r = requests.get(url)
    if r.status_code != 200:
        raise RuntimeError('check the API and try again!!!!')
    else:
        return r


def final(head, tail):
    head = (line.split(':') for line in head.text.splitlines())
    for i, count in head:
        if i == tail:
            return count
    return 0


def api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1_password[:5], sha1_password[5:]
    res = req_api(head)
    return final(res, tail)


def main(args):
    for password in args:
        count = api_check(password)
        if count:
            print(f'{password} is hacked {count} times so should change the passoerd!!')
        else:
            print(f'{password} is safe carry on!!!')
    return 'DONE!!!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
