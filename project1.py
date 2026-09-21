marks = []
for subject in range(5):
    var = int(input("enter your marks"))
    marks.append(var)
print(marks)
total_marks = sum(marks)
print(total_marks)
if total_marks >=500:
    print("grade A+")
elif total_marks >=450:
    print("grade A-")
elif total_marks >=400:
    print("grade B+")
elif total_marks >=350:
    print("grade C+")  
else:
    print("fail")
per = total_marks /500*100
print("percentage", per)                      