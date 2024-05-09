import os,sys
import csv
from GPA import WeightedGPA
from directoryviewer import directory
def pathing_creator(folder):
    if getattr(sys,'frozen',False):
        path=os.path.dirname(os.path.realpath(sys.executable))  
    elif __file__:
        path=os.path.dirname(__file__)
    return os.path.join(path,folder)
def loadClass(filedirectory,allfiles):
    counter=0
    for file in allfiles:
        counter+=1
        print(f'{counter}) {file}\n')
    choice=int(input(f'Please choose a file above to load\n'))-1
    filename=allfiles[choice]
    gpa=WeightedGPA()
    filewriter=open(os.path.join(filedirectory,filename),'r')
    results=filewriter.readlines()
    gpa.addMassData(results)
    return gpa
def deleteClass(filedirectory,allfiles):
    counter=0
    for file in allfiles:
        counter+=1
        print(f'{counter}) {file}\n')
    answer=int(input(f'Please choose a file above to delete')-1
    directory.deleteFilefromDirectory(filedirectory,allfiles[answer])
    del allfiles[answer]
def saveClass(filedirectory,filename,data):
    if '.txt' not in filename:
        filename+='.txt'
    pathing=os.path.join(filedirectory,filename)
    filewriter=open(pathing,'w')
    for element in data:
        filewriter.write(','.join(element)+'\n')
    filewriter.close()
def addGrades(gpaclass):
    print(f'Sections Entered:\n')
    counter=0
    for element in gpa.pullSections():
        counter+=1
        print(f'{counter}) {element}\n')
    sectionindex=int(input(f'Please choose a section above that the grade would fall into\n'))-1
    section=gpa.pullSections()[sectionindex]
    grades=input(f'you can Either input a single grade, or input multiple grades with a comma in bewteen each grade:\n')
    grades=grades.strip()
    if ',' in grades:
        grades=grades.split(',)
        gpaclass.addBatchGrades(section,map(int,grades))
    else:
        grades=int(grades)
        gpaclass.addGrade(section,grades)
def addCriteria(gpaclass):
    section=input(f'Please enter the name of the section:\n')
    percentage=input(f'Please enter the percentage of the section on the final grade (example: %15 or 15):\n')
    gpaclass.addCriteria(section,percentage/100)
def mainMenu(allfiles,directorypathing):
    global gpa
    if len(allfiles)==0:
        print(f'You currently have no saved course files within the program.\n')
        print(f'Please start by creating a course file\n')
        choice=1
    else:
        choice=input(f'Please choose from the following options:\n1: create class file\n2: load class file\n3:Delete Class File')
    if int(choice)==2 and len(allfiles)==0 or int(choice)==3 and len(allfiles)==0:
        print(f'Error: There are no files to load from or remove, please either choose to create a class file or close the program\n')
        mainMenu(allfiles,directorypathing)
    elif int(choice)==3:
        deleteClass(directorypathing,allfiles)
        mainMenu(allfiles,directorypathing)
    if int(choice)==2:
        gpa=loadClass(directorypathing,allfiles)
    elif int(choice)==1:
        title=input(f'Please enter the identifier you want for this course\n').strip()+f'.txt'
        gpa=WeightedGPA()
                                
notfinished=True
directorypathing=pathing_creator(f'stored')
allfiles=directory.pullAllDirectoryFiles(directorypathing)
print(f'Welcome to the GPA calculator. This is to assist in calculating GPAs in specific classes that use the weighted GPA system (with percentages)]\n')
mainMenu(allfiles,directorypathing)
while notfinished:
    choice=input(f'Please choose an option below:\n1)Add Criteria or grade\n2)See Current Final Grade\n3)Check what I need on final assignment/exam for a certain grade\n4)see all grades\n5)Save and Return to Main Menu\n6)Save and Exit Program\n')
    realchoice=int(choice)
    if realchoice==1:
        choice=input(f'please choose an options below: 1)Add Criteria\n2) Add Grade\n')
        if choice=='1':
            addCriteria(gpa)
        else:
            addGrades(gpa)
    elif realchoice==2:
        print(f'Your final grade in this class so far is {gpa.getFinalGrade()}\nNOTE: accuracy of the final grade is dependent on whether all the grades have been entered or not\n')
    elif realchoice==3:
        final=input(f'What section does the final assignment/exam belong to?\n')
        gpa.whatDoINeed(final)
    elif realchoice==4:
        print(gpa)
    elif realchoice==5:
        saveClass(directorypathing,title,gpa.convertData())
        print(f'Save Completed! Returning to Main Menu)'
        mainMenu(allfiles,directorypathing)
    elif realchoice==6:
        saveClass(directorypathing,title,gpa.convertData())
        notfinished=False
print(f'Save Completed! GoodBye')
