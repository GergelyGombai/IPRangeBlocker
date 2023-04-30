from colorama import Fore
from os import system

system("if hash whois &> /dev/null; then echo 'Whois is installed'; else echo 'Whois not installed'; exit 100; fi")

asn = input(str(Fore.GREEN+"Enter ASN: "))



grepcomm = "grep -Eo '([0-9.]+){4}/[0-9]+'"

system(f"whois -h whois.radb.net -- '-i origin {asn}' | {grepcomm} >> ranges.lst")


rangesf = open("ranges.lst", 'r')
ranges = rangesf.readlines()

for range in ranges:
    range = range.strip()
    system(f"iptables -A INPUT -s {range} -j DROP")
    print(Fore.RED+"Blocked " + range)

system("rm ranges.lst")

print(Fore.GREEN+"Done")
