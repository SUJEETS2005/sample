import numpy as np

def generate_college_data(students=100, seed=42):
    np.random.seed(seed)
    maths = np.random.randint(35, 100, students)
    physics = np.random.randint(35, 100, students)
    programming = np.random.randint(35, 100, students)
    attendance = np.random.randint(60, 100, students)
    internal_marks = np.random.randint(20, 50, students)
    data = np.column_stack((maths, physics, programming, attendance, internal_marks))
    return data

college_data = generate_college_data(10)

print("College Dataset:\n", college_data)
print("Shape:", college_data.shape)