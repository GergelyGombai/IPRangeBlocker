from colorama import Fore
from os import system

system("if hash whois &> /dev/null; then echo 'Whois is installed'; else echo 'Whois not installed'; exit 100; fi")

ip = input(str(Fore.GREEN+"Enter IP: "))

awkascomm = """awk '$1=="origin:" { print $2}'"""

system(f"whois {ip} | {awkascomm} >> as.tmp")

asf = open("as.tmp", 'r')
asn = asf.read()



grepcomm = "grep -Eo '([0-9.]+){4}/[0-9]+'"

system(f"whois -h whois.radb.net -- '-i origin {asn}' | {grepcomm} >> ranges.lst")


rangesf = open("ranges.lst", 'r')
ranges = rangesf.readlines()

print(ranges)
for range in ranges:
    print("1")
    range = range.strip()
    system(f"iptables -A INPUT -s {range} -j DROP")
    print(Fore.RED+"Blocked " + range)

system("rm ranges.lst")
system("rm as.tmp")

print(Fore.GREEN+"Done")
