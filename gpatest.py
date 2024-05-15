class WeightedGPA:
    def __init__(self):
        self._sections={}
    def addSection(self,name,percentage,multiple,amount):
        self._section[name]=SectionGPA(name,percentage,multiple,amount)
    def addGrade(self,name,grade):
        self._sections[name].addGrade(grade)
    def addGrades(self,name,listofgrades):
        for element in listofgrades:
            self._section[name].addGrade(element)
    def deleteSection(self,name):
        del self._sections[name]
    def deleteGrades(self,name):
        self._sectionsp[name].deleteAssignments()
    def deleteGrade(self,name,gradeAmount):
        self._sections[name].deleteAssignment(self._sections.deleteAssignment[self._sections[name].getAssignment().getindex(gradeAmount)])
    def CurrentAverageGrade(self):
        total=0
        possible=0
        for element in list(self._section.keys()):
            total+=self._section[element].getCurrentSectionPoints(self)
            possible+=self._section[element].getPercentage()*100
        return total/possible
    def CurrentFinalAverage(self):
        total=0
        for element in list(self._section.keys()):
            total+=self._sections[element].getSectionPoints()
        return total/100
    def CurrentFinalPoints(self):
        total=0
        for element in list(self._section.keys()):
            total+=self._sections[element].getSectionPoints()
        return total
    def whatDoINeed(self,targetsection):
        grade={'A':90,'B':80,'C':70}
        section=self._section[targetsection]
        current=self.CurrentFinalPoints()-section.getSectionPoints()
        percentage=section.getPercentage()
        if self.confirmEmpty(targetsection):
            for element in list(grade.keys()):
                if current>=grade[element]:
                    grade[element]= f'Grade Guaranteed'
                elif current+(percentage*100)<grade[element]:
                    grade[element]= f'Grade Impossible'
                else:
                    needed=section.whatIsNeeded((percentage*100)-(grade[element]-grade))
                    grade[element]=needed
            return grade
        else:
            return False #FIX LATER


    def checkEmpty(self):
        totalempty=0
        for element in list(self._section.keys()):
            totalempty+=self._sections[element].amountEmpty()
        return totalempty
    def confirmEmpty(self,name,amountneeded=1):
        return self._sections[name].amountEmpty()==amountneeded
        
class SectionGPA:
    def __init__(self,sectionname,percentage,multiple=False,amountofassignments=1):
        self._sectionname=sectionname
        self._percentage=percentage/100
        self._assignments=[-1]*amountofassignments
        self._multiple=multiple
        self._amountofassignments=amountofassignments
    def addAssignment(self,assignmentgrade):
        counter=0
        while self._assignments[counter]!=-1:
            counter+=1
        self._assignments[counter]=assignmentgrade
    def getAmountofAssignments(self):
        return self._amountofassignments
    def getPercentage(self):
        return self._percentage
    def getAssignments(self):
        return [x for x in self._assignemnts if x!=-1]
    def getSectionPoints(self):
        return (sum(self.getAssignments())/len(self._assignments))*self._percentage
    def getCurrentSectionAverage(self):
        total=0
        length=0
        for element in self._assignments:
            if element!=-1:
                total+=element
                length+=1
        return total/length
    def getCurrentSectionPoints(self):
        total=0
        length=0
        for element in self._assignments:
            if element!=-1:
                total+=element
                length+=1
        return (total/length)*self._percentage
    def amountEmpty(self):
        currentempty=0
        for element in self._assignments:
            if element==-1:
                currentempty+=1
        return currentempty
    def getAggregateSectionGrades(self):
        return sum(self._assignments)
    def changeAssignment(self,newgrade,index=0):
        self._assignments[index]=newgrade
    def deleteAssignment(self,index=-1):
        if index==-1:
            self._assignments=[-1]*self._amountofassignments
        else:
            self._assignments[index]=-1
        self._assignments.sort()
    def changeAmount(self,newamount):
        self._amountofassignments=newamount
        self.deleteAssignment()
    def whatIsNeeded(self,AmountNeeded):
        needed=(AmountNeeded/self._percentage)*len(self._assignments)-self.getAggregateSectionGrades()
        return needed
    def __str__(self):
        container=f'Section Name:{self._sectionname}\nPercentage:{self._percentage}\nGrades:{self.getAssignments()}\nCurrentAverage:{self.getCurrentSectionAverage()}'
        return container