from directoryviewer import directory
from GPA import WeightedGPA
import os
class UserInterface:
    def __init__(self,pathing):
        self._directoryfiles=directory.pullAllDirectoryFiles(pathing)
        self._directorypath=pathing
        self._gpa= WeightedGPA()
        self._targetfile=''
        self._crashmessages={
            'NONEFOUNDFILE2':'You are unable to load any files as the directory is empty.',
            'NONEFOUNDFILE3': 'You are unable to delete any files as the directory is empty.',
            'INVALIDMAINCHOICE': 'Please choose from the following options presented only', 
            'INVALIDFILECHOICE' : 'Please choose from the following options presented only',
            'INVALIDSUBCHOICE':'Please choose from the following options presented only'}
    def endProgram(self):
        exit()
    def pressToContinue(self):
        input(f'press enter to continue\n')
    def recheckDirectory(self):
        self._directoryfiles=directory.pullAllDirectoryFiles(self._directorypath)
    def intro(self):
        print(f'Welcome to the GPA calculator. This is to assist in calculating GPAs in specific classes that use the weighted GPA system (with percentages)]\n')
    def fileMenu(self):
        if self.isEmptyDir():
            print(f'Directory Contains no courses')
        else:
            amount=len(self._directoryfiles)
            print(f'{amount} course(s) found in directory')
        choice=self.sanitizeInput(input(f'Please choose from the following options:\n1: create class file\n2: load class file\n3: Delete Class File\n'),'MAIN')
        if choice==1:
            self.createCourse()
        elif choice==2:
            if self.isEmptyDir():
                self.crashMessage(f'NONEFOUNDFILE2')
            else:
                filename=self.selectFile()
            self.loadCourse(filename)
        elif choice==3:
            if self.isEmptyDir():
                self.crashMessage(f'NONEFOUNDFILE3')
            else:
                filename=self.selectFile()
            self.deleteCourse(filename)
            return self.fileMenu()
        else:
            self.crashMessage('INVALIDFILECHOICE')
        self.mainMenu()
    def isEmptyDir(self):
        return len(self._directoryfiles)==0
    def showFiles(self):
            counter=0
            for file in self._directoryfiles:
                counter+=1
                print(f'{counter}) {file}')
    def selectFile(self):
        self.showFiles()
        choice=self.sanitizeInput(input(f'Please choose one of the file(s) above:\n'),'FILE')-1
        try:
            return self._directoryfiles[choice]
        except:
            self.crashMessage('INVALIDFILECHOICE')
    def finalGrade(self):
        print(f'Current Final Grade for the Course:\n{self._gpa.getFinalGrade()}\nNOTE: final grade calculated based on currently inputted grades and sections and may not reflect actual final grade if data is either incomplete or inaccurate\n')
        self.pressToContinue()
    def whatDoINeed(self):
        self.showSections()
        choice=self.sanitizeInput(input(f'Please choose the section where the final grade belongs to:\n'),'SUB')-1
        try:
            choice=self._gpa.pullSections()[choice]
            self._gpa.whatDoINeed(choice)
        except:
            self.crashMessage(f'INVALIDSUBCHOICE')
        self.pressToContinue()
    def viewAllGrades(self):
        print(str(self._gpa))
        self.pressToContinue()
    def mainMenu(self):
        choice=self.sanitizeInput(input(f'Please choose an option below:\n1)Add Criteria or grade\n2)Remove criteria or grade\n3)See Current Final Grade\n4)Check what I need on final assignment/exam for a certain grade\n5)see all grades\n6)Save Course\n7)Save Course and Return to File Menu\n8)Save and Exit Program\n'),'MAIN')
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
            self.mainMenu()
        elif choice==7:
            self.saveCourse()
            self.fileMenu()
        elif choice==8:
            self.saveCourse()
            self.endProgram()
        else:
            self.crashMessage('INVALIDMAINCHOICE')
    def sanitizeInput(self,input,menu):
        try:
            choice=int(input)
            return choice
        except:
            self.crashMessage(f'INVALID{menu}CHOICE')
    def subAddMenu(self):
        choice=self.sanitizeInput(input(f'Please choose one of the following options:\n1) Add Section\n2) Add Grade\n3) Return To Main Menu\n'),'SUB')
        if choice==1:
            self.addCriteria()
        elif choice==2:
            self.addGrades()
        elif choice==3:
            self.mainMenu()
        else:
            self.crashMessage('INVALIDSUBCHOICE')
        self.subAddMenu()
    def subRemoveMenu(self):
        choice=self.sanitizeInput(input(f'Please choose from an option below:\n1) Remove Grades\n2) Remove Criteria\n3) Return to Main Menu'),'SUB')
        if choice==1:
            self.removeGrades()
        elif choice==2:
            self.removeCriteria()
        elif choice==3:
            self.mainMenu()
        else:
            self.crashMessage('INVALIDSUBCHOICE')
        self.subRemoveMenu()
    def addCriteria(self):
        choice=input(f'Please input the name of the section you want to add:\n')
        percentage=int(input(f'Please enter the percentage of the course (example: %50 or 50)\n'))
        self._gpa.addCriteria(choice,percentage)
        self.pressToContinue()
        self.subAddMenu()
    def showSections(self):
        counter=0
        for element in self._gpa.pullSections():
            counter+=1
            print(f'{counter}) {element}')
    def removeCriteria(self):
        self.showSections()
        choice=self.sanitizeInput(input(f'Please choose a criteria to remove (This will remove all grades for that criteria as well)\n'),'SUB')-1
        try: 
            choice=self._gpa.pullSections()[choice]
            self._gpa.removeCriteria(choice)
            self.pressToContinue()
            self.subRemoveMenu()
        except:
            self.crashMessage('INVALIDSUBCHOICE')
            return False
    def removeGrades(self):
        self.showSections()
        choiceone=self.sanitizeInput(input(f'Please choose one of the sections above to remove grade(s) from:\n'),'SUB')
        grades=self._gpa.pullGrades(self._gpa.pullSections[choiceone])
        print(grades)
        choice=self.sanitizeInput(input(f'Please choose a choice below:\n1) Remove one grade\n2) Remove All Grades\n3) Return To Main Menu'),'SUB')
        if choice==1:
            print(grades)
            choice=int(input(f'Please enter the grade that needs to be removed\n'))
            try:
                index=grades.idex(choice)
                self._gpa.removeGrades(self._gpa.pullSections[choiceone],index)
            except:
                self.crashMessage('INVALIDSUBCHOICE')
        elif choice==2:
            self._gpa.removeGrades(self._gpa.pullSections[choiceone])
        elif choice==3:
            self.mainMenu()
        else:
            self.crashMessage('INVALIDSUBCHOICE')
        self.pressToContinue()
        self.subRemoveMenu()
    def addGrades(self):
        counter=0
        for element in self._gpa.pullSections():
            counter+=1
            print(f'{counter}) {element}')
        choice=self.sanitizeInput(input(f'Please choose a section to add a grade for above:\n'),'SUB')-1
        grade=input(f'Please enter either a singular grade earned or multiple grades with comma as the separator\n')
        if choice>=counter or choice<=-1:
            self.crashMessage('INVALIDSUBCHOICE')
        elif ',' in grade:
            self._gpa.addBatchGrades(self._gpa.pullSections()[choice],map(int,grade.strip().split(',')))
        else:
            self._gpa.addGrades(self._gpa.pullSections()[choice],int(grade))
        self.pressToContinue()
    def loadCourse(self,filename):
        if '.txt' not in filename:
            filename+='.txt'
        self._targetfile=filename
        self.gpa=WeightedGPA()
        filewriter=open(os.path.join(self._directorypath,filename),'r')
        results=filewriter.readlines()
        self._gpa.addMassData(results)
        print(f'File Loaded Successfully!')
        self.mainMenu()
    def deleteCourse(self,filename):
        directory.deleteFilefromDirectory(self._directorypath,filename)
        self.recheckDirectory()
        print(f'XXXXXXXXXXXXXXXXXXX\nFile Deleted Successfully!\nXXXXXXXXXXXXXXXXXXX')
        self.fileMenu()
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
        print(self._crashmessages[reason])
        if 'SUB' in reason:
            print(f'Returning to Main Menu')
            self.pressToContinue()
            self.mainMenu()
        elif 'MAIN' in reason:
            print(f'Returing to Main Menu')
            self.pressToContinue()
            self.mainMenu()
        elif 'FILE' in reason:
            print(f'Returning to File Menu')
            self.pressToContinue()
            self.fileMenu()
    def loadInterface(self):
        self.intro()
        self.fileMenu()

