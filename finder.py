import re
import json
from urllib.request import urlopen
from urllib.error import URLError


def get_ips(file):
    with open(file, 'r') as f:
        ips = f.readlines()
        print(len(ips), "IP successfully loaded")
        for i in ips:
            response = urlopen('http://ipwho.is/'+i)
            ipwhois = json.load(response)
            data = ipwhois

            if 'connection' not in data:
                continue
            if "Amazon" in data['connection']['isp'] or "Microsoft" in data['connection']['isp'] or "GoDaddy" in data['connection']['isp']:
                print('LIVE: {0} | IP: {1} | ISP: {2} | ORG: {3}'.format(
                    ipwhois['success'], ipwhois['ip'], ipwhois['connection']['isp'], ipwhois['connection']['org']))

                continue
        print("==================================")
        return print("> finished")


# main function
if __name__ == "__main__":
    get_ips('ip.txt')

# end of file
# ===============================================================
