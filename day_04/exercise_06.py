def get_student_average(students):
    total_grades = 0
    total_count = 0
    student_averages = []
    
    for student in students:
        average = sum(student["grades"]) / len(student["grades"])
        student_averages.append({
            "name": student["name"],
            "average": round(average, 2)
        })
        total_grades += sum(student["grades"])
        total_count += len(student["grades"])
    
    class_average = round(total_grades / total_count, 2)
    
    return {
        "class_average": class_average,
        "students": student_averages
    }

# Ejemplo de uso
print(get_student_average([
    {
        "name": "Pedro",
        "grades": [90, 87, 88, 90]
    },
    {
        "name": "Jose",
        "grades": [99, 71, 88, 96]
    },
    {
        "name": "Maria",
        "grades": [92, 81, 80, 96]
    }
]))
