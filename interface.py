from directoryviewer import directory
from GPA import WeightedGPA
import os,sys
class UserInterface:
    def __init__(self,pathing):
        self._directoryfiles=directory.pullAllDirectoryFiles(pathing)
        self._directorypath=pathing
        self._gpa= WeightedGPA()
        self._targetfile=''
    def recheckDirectory(self):
        self._directoryfiles=directory.pullAllDirectoryFiles(self._directorypath)
    def intro(self):
        print(f'Welcome to the GPA calculator. This is to assist in calculating GPAs in specific classes that use the weighted GPA system (with percentages)]\n')
    def fileMenu(self):
        self.showFiles()
        choice=int(input(f'Please choose from the following options:\n1: create class file\n2: load class file\n3: Delete Class File\n'))
        if choice==1:
            self.createCourse()
        elif choice==2:
            if self.isEmptyDir():
                self.crashMessage(f'NONEFOUND')
                return False
            filename=self.selectFile()
            self.loadCourse(filename)
        elif choice==3:
            if self.isEmptyDir():
                self.crashMessage(f'NONEFOUND')
                return False
            filename=self.selectFile()
            self.deleteCourse(filename)
            return self.fileMenu()
        else:
            self.crashMessage('INVALID')
            return False
        return True
    def isEmptyDir(self):
        return len(self._directoryfiles)==0
    def showFiles(self):
        if self.isEmptyDir():
            print(f'No Course files have been created yet!')
        else:
            counter=0
            for file in self._directoryfiles:
                print(f'{counter}) {file}')
    def selectFile(self):
        self.showFiles()
        choice=int(input(f'Please choose one of the file(s) above:\n'))-1
        return self._directoryfiles[choice]
    def finalGrade(self):
        print(f'Current Final Grade for the Course:\n{self._gpa.getFinalGrade()}\nNOTE: final grade calculated based on currently inputted grades and sections and may not reflect actual final grade if data is either incomplete or inaccurate\n')
    def whatDoINeed(self):
        return
    def viewAllGrades(self):
        print(str(self._gpa))
    def mainMenu(self):
        notfinished=True
        while notfinished:
            choice=int(input(f'Please choose an option below:\n1)Add Criteria or grade\n2)Remove criteria or grade\n3)See Current Final Grade\n4)Check what I need on final assignment/exam for a certain grade\n5)see all grades\n6)Save and Return to Main Menu\n7)Save and Exit Program\n'))
            if choice==1:
                self.subAddMenu()
            elif choice==2:
                self.subRemoveMenu()
            elif choice==3:
                self.finalGrade()
            elif choice==4:
                self.whatDoINeed()
            elif choice==5:
                self.viewAllGrades()
            elif choice==6:
                self.saveCourse()
                if self.fileMenu():
                    self.mainMenu()
                    return
                else:
                    self.crashMessage('INVALID')
            elif choice==7:
                self.saveCourse()
                return
            else:
                self.crashMessage('INVALID')
    def subAddMenu(self):
        notfinished=False
        while notfinished:
            choice=int(input(f'Please choose one of the following options:\n1) Add Section\n2) Add Grade\n3) Return To Main Menu\n'))
            if choice>3 or choice<1:
                self.crashMessage(f'INVALID')
            elif choice==1:
                self.addCriteria()
            elif choice==2:
                self.addGrades()
            elif choice==3:
                self.mainMenu()
            else:
                self.crashMessage('INVALID')
    def subRemoveMenu(self):
        return
    def addCriteria(self):
        choice=input(f'Please input the name of the section you want to add:\n')
        percentage=int(input(f'Please enter the percentage of the course (example: %50 or 50)\n'))
        self._gpa.addCriteria(choice,percentage)
    def removeCriteria(self):
        counter=0
        for element in self._gpa.pullSections():
            counter+=1
            print(f'{counter}) {element}')
        choice=int(input(f'Please choose a criteria to remove (This will remove all grades for that criteria as well)\n'))-1
        if choice>=counter or choice<=-1:
            self.crashMessage('INVALID')
            return False
        else:
            self._gpa.removeCriteria(self._gpa.pullSections()[choice])
            return True
    def addGrades(self):
        counter=0
        for element in self._gpa.pullSections():
            counter+=1
            print(f'{counter}) {element}')
        choice=int(input(f'Please choose a section to add a grade for above:\n'))-1
        grade=input(f'Please enter either a singular grade earned or multiple grades with comma as the separator\n')
        if choice>=counter or choice<=-1:
            self.crashMessage('INVALID')
            return False
        elif ',' in grade:
            self._gpa.addBatchGrades(self._gpa.pullSections()[choice],map(int,grade.strip().split(',')))
        else:
            self._gpa.addGrades(self._gpa.pullSections()[choice],int(grade))
        return True
    def loadCourse(self,filename):
        if '.txt' not in filename:
            filename+='.txt'
        self._targetfile=filename
        self.gpa=WeightedGPA()
        filewriter=open(os.path.join(self._directorypath,filename),'r')
        results=filewriter.readlines()
        self._gpa.addMassData(results)
    def deleteCourse(self,filename):
        directory.deleteFilefromDirectory(self._directorypath,filename)
        self.recheckDirectory()
        print(f'XXXXXXXXXXXXXXXXXXX\nFile Deleted Successfully!\nXXXXXXXXXXXXXXXXXXX')
        return True
    def createCourse(self):
        coursename=input(f'Please enter the name of the course:\n')
        self._targetfile=f'{coursename}.txt'
    def saveCourse(self):
        filewriter=open(os.path.join(self._directorypath,self._targetfile),'w')
        massdata=self._gpa.convertData()
        for element in massdata:
            filewriter.write(','.join(element)+'\n')
        filewriter.close()
        self.recheckDirectory()
        print(f'XXXXXXXXXXXXXXXXXXX\nFile Saved Successfully!\nXXXXXXXXXXXXXXXXXXX')
    def crashMessage(self,reason):
        return
    def loadInterface(self,message):
        self.intro()
        if self.fileMenu():
            self.mainMenu()

