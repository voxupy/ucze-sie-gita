student_scores ={
    "Harry":81,
    "Ron":79,
    "Hermiona":99,
    "Draco":74,
    "Neville":62,
}


student_grades ={}


for student in student_scores:
    value = student_scores[student]
    if value >= 91:
        student_grades[student] = "Outstanding"
    elif 81 <= value < 91:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= value < 81:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

