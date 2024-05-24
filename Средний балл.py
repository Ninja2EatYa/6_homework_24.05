grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
from operator import itemgetter
sorted_students = sorted(students, key=itemgetter(0))
print(('Студенты:'), sorted_students)

average1 = sum(grades[0]) / len(grades[0])
average2 = sum(grades[1]) / len(grades[1])
average3 = sum(grades[2]) / len(grades[2])
average4 = sum(grades[3]) / len(grades[3])
average5 = sum(grades[4]) / len(grades[4])
average = list[average1, average2, average3, average4, average5]
dict_average_score = {sorted_students[0]: average1, sorted_students[1]: average2,sorted_students[2]: average3,sorted_students[3]: average4,sorted_students[4]: average5}
print(('Средний балл:'), dict_average_score)
