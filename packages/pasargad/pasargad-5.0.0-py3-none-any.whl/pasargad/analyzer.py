import numpy as np
import pandas as pd

class TrafficAnalyzer:
    def __init__(self, interval):
        self.interval = interval
        self.data = []

    def add_data(self, ip, timestamp, protocol, port, flags):
        self.data.append({"ip": ip, "timestamp": timestamp, "protocol": protocol, "port": port, "flags": flags})

    def analyze(self):
        if not self.data:
            return None
        df = pd.DataFrame(self.data)
        current_time = max(df['timestamp'])
        recent = df[df['timestamp'] >= current_time - self.interval]
        if recent.empty:
            return None
        ip_counts = recent.groupby('ip').size()
        mean = ip_counts.mean()
        std = ip_counts.std()
        threshold = mean + 3 * std
        anomalies = ip_counts[ip_counts > threshold].index.tolist()
        return anomalies