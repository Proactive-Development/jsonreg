import pytest
import os 
import jsonreg
import shutil
def test_setup():
    try:
        os.mkdir("Pytest_tmp")
    except:
        pytest.skip()
def test_create_key():
    jsonreg.create("Pytest_tmp/key1.json", "Test1", "This is test data")
def test_read_key():
    data,id,name = jsonreg.read("Pytest_tmp/key1.json")
    print(data)
    if data != "This is test data":
        pytest.fail()
def test_find_key():
    jsonreg.find.name("Pytest_tmp", "Test1")
def test_clean():
    shutil.rmtree("Pytest_tmp")