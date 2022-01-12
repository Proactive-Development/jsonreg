import pytest
import os 
import jsonreg
def test_setup():
    os.mkdir("tmp")
def test_create_key():
    jsonreg.create("tmp/key1.json", "Test1", "This is test data")
def test_read_key():
    jsonreg.read("tmp/key1.json")
def test_find_key():
    jsonreg.find.name("tmp", "Test1")