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
def loadClass(filename,filedirectory):
    filename=f'{filename}'
    gpa=WeightedGPA()
    filewriter=open(os.path.join(filedirectory,filename),'r')
    results=filewriter.readlines()
    gpa.addMassData(results)
    return gpa
def saveClass(filedirectory,filename,data):
    if '.txt' not in filename:
        filename+='.txt'
    pathing=os.path.join(filedirectory,filename)
    filewriter=open(pathing,'w')
    for element in data:
        filewriter.write(','.join(element)+'\n')
    filewriter.close()

notfinished=True
directorypathing=pathing_creator(f'stored')
allfiles=directory.pullAllDirectoryFiles(directorypathing)
while(notfinished):
    print(f'Welcome to the GPA calculator. This is to assist in calculating GPAs in specific classes that use the weighted GPA system (with percentages)]\n')
    if len(allfiles)==0:
        print(f'You currently have no saved course files within the program.\n')
        print(f'Please start by creating a course file\n')
        choice=1
    else:
        choice=input(f'Please choose from the following options:\n1: create class file\n2: load class file\n')
    if int(choice)==2 and len(allfiles)==0:
        print(f'Error: There are no files to load from, please either choose to create a class file or close the program\n')
    else:
        notfinished=False
if int(choice)==2:
    counter=0
    for file in allfiles:
        counter+=1
        print(f'{counter}) {file}\n')
    choice=int(input(f'Please choose a file above to load\n'))-1
    title=loadClass(allfiles[choice],directorypathing)
elif int(choice)==1:
    title=input(f'Please enter the identifier you want for this course\n').strip()+f'.txt'

gpa=loadClass(f'{title}') if int(choice)==2 else WeightedGPA()

notfinished=True
while notfinished:
    choice=input(f'Please choose an option below:\n1)Add Criteria\n2)Add Grade\n3)See Current Final Grade\n4)Check what I need on final assignment/exam for a certain grade\n5)see all grades\n6)Save and exit program\n')
    realchoice=int(choice)
    if realchoice==1:
        section=input(f'Please input the name of this section:\n')
        percentage=input(f'Please input the percentage this section has over the final grades (format by example: %15)\n')
        gpa.addCriteria(section,int(percentage.strip().replace('%',''))/100)
        print(f'Criteria Added!')
    elif realchoice==2:
        print(f'Sections Entered:\n')
        counter=0
        for element in gpa.pullSections():
            counter+=1
            print(f'{counter}) {element}\n')
        section=int(input(f'Please choose a section above that the grade would fall into\n'))-1
        section=gpa.pullSections()[section]
        grade=input(f'Please input the grade earned on this assignment/exam\n')
        gpa.addGrades(section,int(grade))
    elif realchoice==3:
        print(f'Your final grade in this class so far is {gpa.getFinalGrade()}\nNOTE: accuracy of the final grade is dependent on whether all the grades have been entered or not\n')
    elif realchoice==4:
        final=input(f'What section does the final assignment/exam belong to?\n')
        gpa.whatDoINeed(final)
    elif realchoice==5:
        print(gpa)
    elif realchoice==6:
        saveClass(directorypathing,title,gpa.convertData())
        notfinished=False
print(f'Save Completed! GoodBye')
