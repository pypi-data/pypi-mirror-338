import json
import os

class TrafficStorage:
    def __init__(self, filename="traffic_data.jsonl"):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "a") as f:
            f.write(json.dumps(data) + "\n")

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return [json.loads(line) for line in f]