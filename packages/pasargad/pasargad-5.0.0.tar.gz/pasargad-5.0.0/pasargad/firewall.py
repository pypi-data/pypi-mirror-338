import subprocess

class Firewall:
    @staticmethod
    def block_ip(ip, permanent=False):
        try:
            cmd = ['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP']
            subprocess.run(cmd, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to block IP {ip}: {e}")
            return False

    @staticmethod
    def unblock_ip(ip):
        try:
            cmd = ['iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP']
            subprocess.run(cmd, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to unblock IP {ip}: {e}")
            return False

    @staticmethod
    def rate_limit_ip(ip, rate_limit):
        try:
            cmd = [
                'iptables', '-A', 'INPUT', '-s', ip,
                '-m', 'limit', '--limit', f"{rate_limit}/second",
                '--limit-burst', f"{rate_limit*2}", '-j', 'ACCEPT'
            ]
            subprocess.run(cmd, check=True)
            cmd = ['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP']
            subprocess.run(cmd, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to rate-limit IP {ip}: {e}")
            return False