import numpy as np
import pandas as pd
from collections import defaultdict
import time

class TrafficDetector:
    def __init__(self, threshold, interval):
        self.threshold = threshold
        self.interval = interval
        self.ip_requests = defaultdict(list)
        self.baseline = None

    def update_baseline(self):
        if not self.ip_requests:
            return
        request_counts = [len(reqs) for reqs in self.ip_requests.values()]
        if request_counts:
            self.baseline = np.mean(request_counts) + 2 * np.std(request_counts)

    def detect_anomaly(self, ip):
        current_time = time.time()
        self.ip_requests[ip] = [t for t in self.ip_requests[ip] if current_time - t < self.interval]
        request_count = len(self.ip_requests[ip])
        if self.baseline and request_count > self.baseline * 1.5:
            return True, "Anomaly"
        if request_count > self.threshold:
            return True, "Flood"
        return False, None

    def add_request(self, ip):
        self.ip_requests[ip].append(time.time())

    def cleanup(self):
        current_time = time.time()
        for ip in list(self.ip_requests.keys()):
            self.ip_requests[ip] = [t for t in self.ip_requests[ip] if current_time - t < self.interval]
            if not self.ip_requests[ip]:
                del self.ip_requests[ip]