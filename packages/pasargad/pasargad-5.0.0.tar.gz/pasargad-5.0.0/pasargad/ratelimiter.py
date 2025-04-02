import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, rate_limit, interval):
        self.rate_limit = rate_limit
        self.interval = interval
        self.ip_rates = defaultdict(list)

    def is_limited(self, ip):
        current_time = time.time()
        self.ip_rates[ip] = [t for t in self.ip_rates[ip] if current_time - t < self.interval]
        if len(self.ip_rates[ip]) >= self.rate_limit:
            return True
        self.ip_rates[ip].append(current_time)
        return False

    def cleanup(self):
        current_time = time.time()
        for ip in list(self.ip_rates.keys()):
            self.ip_rates[ip] = [t for t in self.ip_rates[ip] if current_time - t < self.interval]
            if not self.ip_rates[ip]:
                del self.ip_rates[ip]
