grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted = sorted (students)

avg = [
    sum(grades[0]) / len(grades[0]),
    sum(grades[1]) / len(grades[1]),
    sum(grades[2]) / len(grades[2]),
    sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4])
]

dictionary = {}

dictionary[sorted[0]] = [avg[0]]
dictionary[sorted[1]] = [avg[1]]
dictionary[sorted[2]] = [avg[2]]
dictionary[sorted[3]] = [avg[3]]
dictionary[sorted[4]] = [avg[4]]

print (dict(zip(sorted,avg)))












