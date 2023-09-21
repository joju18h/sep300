from functools import reduce
student_grades = [
    {"name":"Alice", "scores": [80,75,90,85]},
    {"name":"Bob", "scores": [70,65,80,75]},
    {"name":"Charlie", "scores": [90,85,95,80]},
    {"name":"David", "scores": [60,55,70,65]},
    {"name":"Eva", "scores": [85,90,80,95]},
]

average = list(map(lambda x:{"name": x["name"], "avg":sum(x["scores"])/len(x["scores"])}, student_grades))
print(average, "\n")

above_80 = list(filter(lambda x: sum(x["scores"])/len(x["scores"]) > 80, student_grades))
print(above_80, "\n")

overallAvg = reduce(lambda x,y: x+y["avg"], average, 0)/len(student_grades)
print(overallAvg, "\n")


