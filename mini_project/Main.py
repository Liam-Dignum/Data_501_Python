import csv
from typing import List


def extract(filename:str): ##create list of dicts from input filename csv
    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        studentdictlist = list()
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
#keys1 = ('Name','Math Score','English Score','Science Score','Number of Siblings','Lunch Type','Test Preparation','Study Time (hours)','Favorite Subject','Art Score','History Score','Main Teacher')

## create list of dicts from file and print contents

studentdictlist = extract('student_test_scores.csv')
print(studentdictlist)

## declare keys to be deleted, remove keys from list of dicts and add an avg score, print new list of dicts

removeKeys = ('Number of Siblings','Lunch Type','Test Preparation','Study Time (hours)','Favorite Subject','Main Teacher')
transform(removeKeys,studentdictlist)
print(studentdictlist)

## save transformed list of dicts to a new file

load('average_student_scores.csv',studentdictlist)