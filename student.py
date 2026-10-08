students = {}


def add_student(student_id, name, age):
    students[student_id] = {
        "name": name,
        "age": age
    }


def remove_student(student_id):
    if student_id in students:
        del students[student_id]
        return True
    return False


def search_student(student_id):
    return students.get(student_id)


def update_student(student_id, name, age):
    if student_id in students:
        students[student_id] = {
            "name": name,
            "age": age
        }
        return True
    return False