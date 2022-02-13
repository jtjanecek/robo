import subprocess
import shlex
import os

class RoboPacketSniffer:
    def __init__(self, config: dict):
        logsize = config['pcap']['log_max_mb']
        log_count = config['pcap']['log_backup_count']

        pcap_loc = os.path.join(config['log_location'], 'pcap.pcap')

        if config['pcap']['enabled'] == 'True':
            cmd = f"tcpdump --interface any -s 65535 -n -x 'udp port {config['dmeudp']['port']} or tcp port {config['mas']['port']} or tcp port {config['mls']['port']} or tcp port {config['dmetcp']['port']} or udp port {config['nat']['port']}' -W {log_count} -C {logsize} -w {pcap_loc}"

            in_docker = os.environ.get('IN_DOCKER', False)
            if not in_docker:
            	cmd = f'sudo {cmd}'

            args = shlex.split(cmd)
            p = subprocess.Popen(args)
