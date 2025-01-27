import pytest
import csv
from typing import List
import os


def extract(filename:str): ##create list of dicts from input filename csv
    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        studentdictlist = []
        for row in reader:
            studentdictlist.append(row)
    return studentdictlist

def transform(keysList: List[str],studentdictlist): ## delete rows from input keyList and add an average score key
    for row in studentdictlist:
        for key in keysList:
            del row[key]
        Math = int(row['Math Score'])
        English = int(row['English Score'])
        Science = int(row['Science Score'])
        Art = int(row['Art Score'])
        History = int(row['History Score'])
        avg = (Math + English + Science + Art + History) / 5
        row['Average Score'] = avg

def load (filename: str,studentdictlist): ## save list of dicts with input filename
    with open(filename, "w", newline='') as f:
        dict_writer = csv.DictWriter(f, studentdictlist[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(studentdictlist)
testdata = [([{'id1':'0','id2':'1'}],[{'id1':'0','id2':'1'}])]
@pytest.mark.parametrize('data, expected',testdata)

def test_extract(data, expected):
    tmp_file = 'tmp.csv'
    with open(tmp_file, 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, data[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(data)

    result = extract(tmp_file)
    os.remove(tmp_file)
    assert expected == result



testdata = [([
                [{'Name': 'Student_1', 'Math Score': '55', 'English Score': '47', 'Science Score': '100', 'Number of Siblings': '5', 'Lunch Type': 'Standard', 'Test Preparation': 'None', 'Study Time (hours)': '2.6', 'Favorite Subject': 'Art', 'Art Score': '50', 'History Score': '55', 'Main Teacher': 'Teacher_A'},
                {'Name': 'Student_2', 'Math Score': '87', 'English Score': '58', 'Science Score': '45', 'Number of Siblings': '0', 'Lunch Type': 'Standard', 'Test Preparation': 'None', 'Study Time (hours)': '3.3', 'Favorite Subject': 'History', 'Art Score': '87', 'History Score': '95', 'Main Teacher': 'Teacher_C'}],
                [{'Name': 'Student_1', 'Math Score': '55', 'English Score': '47', 'Science Score': '100', 'Art Score': '50', 'History Score': '55', 'Average Score': 61.4}, {'Name': 'Student_2', 'Math Score': '87', 'English Score': '58', 'Science Score': '45', 'Art Score': '87', 'History Score': '95', 'Average Score': 74.4}],
                ['Number of Siblings','Lunch Type','Test Preparation','Study Time (hours)','Favorite Subject','Main Teacher']
            ])]
@pytest.mark.parametrize('data, expected,removeKeys',testdata)
def test_transform(data,expected,removeKeys):
    result = data
    transform(removeKeys,data)
    assert expected == result



testdata = [([{'id1':'0','id2':'1'}],[{'id1':'0','id2':'1'}])]
@pytest.mark.parametrize('data, expected',testdata)
def test_load(data,expected):
    tmp_File = 'testFile.csv'
    load(tmp_File,data)
    with open(tmp_File, 'r') as readdata:
        reader = csv.DictReader(readdata)
        result = []
        for row in reader:
            result.append(row)
    os.remove(tmp_File)
    assert result == expected
