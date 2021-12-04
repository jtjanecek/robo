import subprocess
import shlex

class RoboPacketSniffer:
    def __init__(self, config: dict):

        cmd = "tcpdump --interface any -s 65535 -n -x 'udp port 51000 or tcp port 10075 or tcp port 10078 or tcp port 10079 or udp port 10070' -W 10 -C 30 -w /logs/pcap.pcap"
        args = shlex.split(cmd)
        p = subprocess.Popen(args)
