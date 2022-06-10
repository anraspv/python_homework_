from HW6.hw6_task02 import Teacher, Student, HomeworkResult, DeadlineError
import pytest


lazy_student = Student('Roman', 'Petrov')
good_student = Student('Lev', 'Ivanov')

oop_hw = Teacher.create_homework('Learn OOP', 5)
docs_hw = Teacher.create_homework('Read docs', 5)


@pytest.fixture()
def reset_results_fixture():
    yield
    Teacher.reset_results()


@pytest.fixture()
def fill_the_dict_fixture():
    Teacher.check_homework(good_student.do_homework(oop_hw, 'content1'))
    Teacher.check_homework(lazy_student.do_homework(docs_hw, 'content2'))
    yield


def test_type_error():
    with pytest.raises(TypeError):
        HomeworkResult(good_student, "fff", "Solution")


def test_deadline_error():
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(Teacher.create_homework('NVM', 0), 'done, baby')


@pytest.mark.parametrize('hw_result', (good_student.do_homework(oop_hw, 'I have done this hw'),
                                       lazy_student.do_homework(docs_hw, 'done with no pleasure')))
def test_check_hw_positive(hw_result, reset_results_fixture):
    assert Teacher.check_homework(hw_result) is True


@pytest.mark.parametrize('hw_result', (good_student.do_homework(oop_hw, 'ahh'),
                                       lazy_student.do_homework(oop_hw, 'bee')))
def test_check_hw_negative(hw_result, reset_results_fixture):
    assert Teacher.check_homework(hw_result) is False



