import pytest
from student import (
    students,
    add_student,
    remove_student,
    search_student,
    update_student
)


@pytest.fixture(autouse=True)
def clear_students():
    students.clear()


def test_add_student():
    add_student(1, "Aish", 20)
    assert search_student(1)["name"] == "Aish"


def test_add_second_student():
    add_student(2, "Rahul", 21)
    assert search_student(2)["name"] == "Rahul"


def test_search_student():
    add_student(1, "Aish", 20)
    assert search_student(1) == {
        "name": "Aish",
        "age": 20
    }


def test_search_missing_student():
    assert search_student(99) is None


def test_remove_student():
    add_student(1, "Aish", 20)
    assert remove_student(1) is True


def test_remove_missing_student():
    assert remove_student(99) is False


def test_update_student():
    add_student(1, "Aish", 20)
    assert update_student(1, "Aishwarya", 21) is True
    assert search_student(1)["name"] == "Aishwarya"


def test_update_missing_student():
    assert update_student(99, "Aish", 20) is False


def test_student_age():
    add_student(1, "Aish", 20)
    assert search_student(1)["age"] == 20


def test_multiple_students():
    add_student(1, "Aish", 20)
    add_student(2, "Rahul", 21)

    assert len(students) == 2