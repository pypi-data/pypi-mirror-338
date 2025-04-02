import random
import string

class ChallengeResponse:
    def __init__(self):
        self.tokens = {}

    def generate_token(self, ip):
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        self.tokens[ip] = token
        return token

    def verify_token(self, ip, token):
        if ip in self.tokens and self.tokens[ip] == token:
            del self.tokens[ip]
            return True
        return False