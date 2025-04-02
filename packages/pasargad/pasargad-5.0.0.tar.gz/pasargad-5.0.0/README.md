# Pasargad v5.0.0 - Ultra-Strong DDoS and Attack Protection Library

Pasargad is a powerful Python library designed to protect your network from DDoS attacks and other malicious activities. Version 5.0.0 introduces advanced features like machine learning-based detection, multi-layer protection, intelligent filtering, and optimized performance.

## Features

- **Advanced Machine Learning Detection**: Uses Isolation Forest and DBSCAN to detect abnormal traffic patterns.
- **Multi-Layer Protection**: Defends against Layer 3/4 (SYN Flood, UDP Flood) and Layer 7 (HTTP Flood, Slowloris) attacks.
- **Intelligent Filtering**: Dynamic Rate Limiting, Throttling, and CAPTCHA challenges to distinguish real users from bots.
- **GeoIP Filtering**: Restrict traffic based on geographic location using MaxMind GeoIP database.
- **Signature-Based Detection**: Identify known attack patterns like SYN Flood and UDP Flood.
- **Optimized Performance**: Uses Redis for temporary storage and limits memory usage for scalability.
- **Advanced Logging and Reporting**: Real-time reports with Elasticsearch integration for detailed analytics.

## Installation

1. **Install the library from PyPI**:
   ```bash
   pip install pasargad==5.0.0