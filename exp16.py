print("251A022,17-03-26")
import re

email=input("ENTER YOUR EMAIL:")
mobile=input("ENTER YOUR NUMBER:")

email_pattern=r'^[\w\.-]+@[\w\.-]+\.[\w\.-]+'
mobile_pattern=r'^[6-9]\d{9}$'

if re.fullmatch(email_pattern,email):
    print("VALID EMAIL ID")
else:
    print("INVALID ID")
if re.fullmatch(mobile_pattern,mobile):
  print("VALID MOBILE NUMBER")
else:
    print("INVALID MOBILE NUMBER")
