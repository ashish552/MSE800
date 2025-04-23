import numpy as np  
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])
average_score = np.mean(scores, axis=1)
print(f"Average score for each student:{average_score}")
subject_average_score = np.mean(scores, axis=0)
print(f"The average score for each subject:{subject_average_score}")
total_score = np.sum(scores, axis =1)
student_highest_score = np.argmax(total_score)
print(f"The student with the highest score is at row inex: {student_highest_score}")
add_five = scores[:,2]+5
print(add_five)

