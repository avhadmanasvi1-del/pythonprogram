#student enrollment manager
print("251A001", "SOLEHA")
CET = {"251A001", "251A002", "251A006"}
JEE = {'251A001', '251A050', '251A049', '251A006'}
NEET = {'251A022', '251A024', '251A002'}

print(CET | JEE | NEET)  # total no. of students
print("Total students appeared in the exams:", CET | JEE | NEET)
print("Total students appeared in all exams:", CET & JEE & NEET)
print("Total students appeared only in cet and neet exams:", (CET & NEET) - JEE)
print("Total students appeared only in cet and neet exams:", (CET | NEET) - JEE)
print(CET | JEE)  # total students appeared in cet and jee #either cet or jee but not both
print(CET & JEE)  # students appeared in both cet and jee
print((CET | JEE) - (CET & JEE))  # either cet or jee but not both
