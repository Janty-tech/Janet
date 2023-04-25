import re

def main():
    print(validate(input("IPv4 Address:")))


def valuidate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+$", ip):
        list_of_numbers = ip.split(",")
        for number in list_of_numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    
    else:
        return False