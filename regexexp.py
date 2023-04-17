import re

email = input("whats your email? ").strip()

if re.search(r"^.+@.+\.com$", email):
    print("valid")
else:
    print("invalid")