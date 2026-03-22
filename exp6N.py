CET={ "251A022","251A001","251A06"}
JEE={ "251AO23","251A002","251A06"}
NEET={"251A028","251A001","251A022"}

print(CET| JEE | NEET)  # total number of students
print("total number of students are",CET|JEE|NEET)
print("total number of students in  all  are",CET & JEE &NEET) #common in all
print("total number of student in only in cet and neet exam",(CET&NEET)-JEE) # student commonin cet and neet and nor prsent in jee
print("total number of student in only in cet and neet exam",(CET|NEET)-JEE) #total student in cet and neet 
print(CET|JEE) #union total number of student in cet and jee
print(CET&JEE)#intersection common student in cet and jee

print((CET|JEE)-(CET&JEE)) #either cet or jee but not both(common wala nahi ayega)
