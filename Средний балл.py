grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

from operator import itemgetter
sorted_students = sorted(students, key=itemgetter(0))
print(('Студенты:'), sorted_students)

average = {}
for i in range(0, len(grades)):
    average[i] = sum(grades[i]) / len(grades[i])

dict_average_score = {}
for i in range(0, len(grades)):
 key = sorted_students[i]
 value = average[i]
 dict_average_score[key] = value
print(('Средний балл:'), dict_average_score)
