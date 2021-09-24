import pytest
# Import the features implemented
from main import *

#Test Code
"""
Write a test for each feature below
"""

def test_feature1():
    assert feature1("Teacher")=='T'
def test_feature2():
    assert feature2("Teacher")=='e'
def test_feature3():
    assert first_half("testtest")=="test"
def test_feature4():
    assert feature4("1111") == "11"
