def graderounding(grades):
      for i in grades:
    if i<38:
        continue
    if i>38 and (i+2)%5==0:
        grades[grades.index(i)]=(i+2)
    elif i>38 and (i+1)%5==0:
        grades[grades.index(i)]=(i+1)
    return grades
