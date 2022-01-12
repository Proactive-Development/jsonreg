import pytest
import os 
import jsonreg
import shutil
def test_setup():
    try:
        os.mkdir("Pytest_tmp")
    except:
        pass
    os.chdir("Pytest_tmp")
    with open(".gitignore","w") as f:
        f.write("*")
    f.close()
    os.chdir("..")
def test_create_key():
    jsonreg.create("Pytest_tmp/key1.json", "Test1", "This is test data")
def test_read_key():
    data,id,name = jsonreg.read("Pytest_tmp/key1.json")
    print(data)
    if data != "This is test data":
        pytest.fail()
def test_find_key():
    jsonreg.findfrom.name("Pytest_tmp", "Test1")