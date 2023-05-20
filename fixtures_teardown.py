import os
import pytest


# Создадим успешный тест
def test_one(file_object):
    assert file_object.readline() == "123"


# Создадим провальный тест
def test_two(file_object):
    assert file_object.readline() == "1234"


# Применим teardown в фикстуре при помощи request.addfinalizer
@pytest.fixture()
def file_object(request, string_fixture):
    tmp_name = "{}.txt".format(string_fixture)

    f = open(tmp_name, "w+")
    print("\nCreating a file: {}".format(tmp_name))

    f.write("123")
    f.seek(0)

    def teardown():
        print("\nRemoving a file: {}".format(tmp_name))
        os.remove(tmp_name)

    request.addfinalizer(teardown)

    return f


# Применим teardown в фикстуре при помощи yield
@pytest.fixture()
def file_object(string_fixture):
    tmp_name = "{}.txt".format(string_fixture)

    f = open(tmp_name, "w+")
    print("\nCreating a file: {}".format(tmp_name))

    f.write("123")
    f.seek(-1)

    yield f

    os.remove(tmp_name)
    print("\nRemoving a file: {}".format(tmp_name))


# Совершим ошибку передав в метод f.seek отрицательное число и перенесем teardown выше,
# чтобы несмотря на ошибку текстовые файлы удалялись
@pytest.fixture()
def file_object(request, string_fixture):
    tmp_name = "{}.txt".format(string_fixture)

    f = open(tmp_name, "w+")
    print("\nCreating a file: {}".format(tmp_name))

    def teardown():
        print("\nRemoving a file: {}".format(tmp_name))
        os.remove(tmp_name)

    request.addfinalizer(teardown)

    f.write("123")
    f.seek(-1)

    return f
