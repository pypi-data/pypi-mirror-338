import threading
import time
import scapy.all as scapy
from .ratelimiter import RateLimiter
from .detector import TrafficDetector
from .firewall import Firewall
from .logger import log_event
from .storage import TrafficStorage
from .analyzer import TrafficAnalyzer
from .challenge import ChallengeResponse

class Pasargad:
    def __init__(self, threshold=2000, interval=10, block_duration=14400, rate_limit=500, 
                 ports=None, interfaces=None, max_memory=30000, strict_mode=False):
        self.threshold = threshold
        self.interval = interval
        self.block_duration = block_duration
        self.rate_limit = rate_limit
        self.ports = ports or [80, 443]
        self.interfaces = interfaces or [None]
        self.max_memory = max_memory
        self.strict_mode = strict_mode
        self.ratelimiter = RateLimiter(self.rate_limit, self.interval)
        self.detector = TrafficDetector(self.threshold, self.interval)
        self.firewall = Firewall()
        self.storage = TrafficStorage()
        self.analyzer = TrafficAnalyzer(self.interval)
        self.challenge = ChallengeResponse()
        self.blocked_ips = {}
        self.lock = threading.Lock()
        self.running = False

    def monitor_traffic(self):
        print(f"Pasargad v4.0.0 Ultra Protection activated on {self.interfaces}")
        self.running = True
        for iface in self.interfaces:
            sniff_thread = threading.Thread(
                target=scapy.sniff,
                kwargs={'prn': self.process_packet, 'store': 0, 'iface': iface}
            )
            sniff_thread.daemon = True
            sniff_thread.start()

        cleanup_thread = threading.Thread(target=self.cleanup_loop)
        cleanup_thread.daemon = True
        cleanup_thread.start()

        while self.running:
            time.sleep(1)

    def process_packet(self, packet):
        if not (packet.haslayer("IP") or packet.haslayer("IPv6")):
            return

        src_ip = packet["IP"].src if packet.haslayer("IP") else packet["IPv6"].src
        current_time = time.time()
        protocol = "TCP" if packet.haslayer("TCP") else "UDP" if packet.haslayer("UDP") else "Other"
        port = (packet["TCP"].dport if protocol == "TCP" else 
                packet["UDP"].dport if protocol == "UDP" else None)
        flags = packet["TCP"].flags if protocol == "TCP" else None

        if self.ports and port not in self.ports:
            return

        with self.lock:
            if src_ip in self.blocked_ips:
                return

            if self.ratelimiter.is_limited(src_ip):
                return

            self.detector.add_request(src_ip)
            self.storage.save({"ip": src_ip, "timestamp": current_time, "protocol": protocol, "port": port, "flags": str(flags)})
            self.analyzer.add_data(src_ip, current_time, protocol, port, flags)

            is_attack, attack_type = self.detector.detect_anomaly(src_ip)
            if is_attack:
                if attack_type == "Flood":
                    self.firewall.block_ip(src_ip)
                    self.blocked_ips[src_ip] = (current_time, attack_type)
                else:
                    self.firewall.rate_limit_ip(src_ip, self.rate_limit)
                    log_event(f"IP {src_ip} rate-limited due to {attack_type}")

            anomalies = self.analyzer.analyze()
            if anomalies and src_ip in anomalies:
                self.firewall.block_ip(src_ip)
                self.blocked_ips[src_ip] = (current_time, "Anomaly")
                log_event(f"IP {src_ip} blocked due to anomaly detection")

    def cleanup_loop(self):
        while self.running:
            self.ratelimiter.cleanup()
            self.detector.cleanup()
            current_time = time.time()
            for ip, (block_time, _) in list(self.blocked_ips.items()):
                if current_time - block_time > self.block_duration:
                    self.firewall.unblock_ip(ip)
                    del self.blocked_ips[ip]
            time.sleep(5)

    def stop(self):
        self.running = False