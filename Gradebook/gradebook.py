# Little project to practice simple Lists uses on Python3

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# list creation

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]], [subjects[2], grades[2]],[subjects[3], grades[3]]]
print(gradebook)

# new list append 

new_values = ["computer science", 100]
gradebook.append(new_values)
gradebook.append(["visual arts", 93])

gradebook[-1][-1] += 5
gradebook[2].remove(85)
gradebook[2].append("Pass")

full_gradebook = gradebook + last_semester_gradebook 

print(full_gradebook)