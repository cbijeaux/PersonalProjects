import math 
class WeightedGPA:
        def __init__(self):
                self._classgpa={}
                self._grades={}
                self._percentage=0
        def addMassData(self,massdata): #[classification,title,grade/percentage]
            for element in massdata:
                if element[0]=='section':
                    self.addCriteria(element[1],element[2])
                else:
                    self.addGrades(element[1],element[2])
        def checkPercentage(self,newpercentage):
            if self._percentage+newpercentage>100:
                return False
            else:
                return True
        def addCriteria(self,title,percentage):
            if self.checkPercentage(percentage):
                self._classgpa[title]=percentage
                self._percentage+=percentage
                print(f'{title} worth {percentage} of the final grade added!')
            else:
                print(f'Total percentage cannot exceed %100. Please double check the criteria percentage before inputting it. Section not entered in Course')
        def removeCriteria(self,title):
            print(f'{title} removed alongside grades from that section')
            self._percentage-=self._classgpa[title]
            del self._classgpa[title]
            del self._grades[title]
        def removeGrades(self,title,grade=-1):
            if grade==-1:
                del self._grades[title]
                print(f'All grades removed from {title}')
            else:
                targetgrade=self._grades[title][grade]
                self._grades.remove(grade)
                print(f'Grade of {targetgrade} removed from {title}')
        def addGrades(self,title,grade):
            if self._grades.get(title):
                self._grades[title].append(grade)
                print(f'Grade Added to {title}')
            else:
                self._grades[title]=[grade]
                print(f'All Grades added to {title}')
        def pullGrades(self,title):
            return self._grades[title]
        def addBatchGrades(self,title,batchofgrades): 
            for grade in batchofgrades:
                self.addGrades(title,grade)
        def calculateCurrentGrade(self):
            total=0
            for element in list(self._grades):
                if self._grades.get(element):
                    total+=(sum(self._grades[element])/len(self._grades[element]))*self._classgpa[element]
            return total
        def getFinalGrade(self):
            return self.calculateCurrentGrade()
        def calcualteSection(self,title):
            return (sum(self._grades[title])/len(self._grades))*self._classgpa[title]
        def pullSections(self):
            return list(self._classgpa.keys())
        def calculateGroupGradeRequired(self,title):
            grades={"A":90,"B":80,"C":70}
            container=f'The result for possible final grade depending on the final {title} grade:\n'
            percentage=self._classgpa[title]
            currentgrade=self.calculateCurrentGrade()
            numberoftotalgrades=len(self._grades[title])+1
            totalgradesofcurrentsection=sum(self._grades[title])
            gradeswithoutsection=currentgrade-self.calcualteSection(title)
            minresult=gradeswithoutsection+(percentage*(totalgradesofcurrentsection/(numberoftotalgrades)))
            maxresult=gradeswithoutsection+(percentage*((totalgradesofcurrentsection+100)/(numberoftotalgrades)))
            for element in list(grades):
                if minresult>grades[element]:
                    container+=f'{element} grade guaranteed\n'
                elif maxresult<grades[element]:
                    container+=f'{element} grade not possible\n'
                else:
                    sectionneeded=(((grades[element]-gradeswithoutsection)/percentage)*(numberoftotalgrades))-totalgradesofcurrentsection
                    sectionneeded=math.ceil(sectionneeded)
                    container+=f'{element} Grade requires a grade of at least {sectionneeded} on the final {title}\n'
            print(container)
        def calculateInidivualGradeRequired(self,title):
            grades={"A":90,"B":80,"C":70}
            container=f'The result for possible final grade(s) depending on the {title} grade:\n'
            current=self.calculateCurrentGrade()
            percentage=self._classgpa[title]
            for element in list(grades):
                left=grades[element]-current
                if 100*percentage<left:
                    container+=f'{element} grade not possible\n'
                elif current<=0:
                    container+=f'{element} grade guaranteed\n'
                else:
                    finalrequired=math.ceil(left/percentage)
                    container+=f'{element} Grade requires {finalrequired} in {title}\n'
            print(container)
        def checkAmountNotGrades(self):
            emptysections=[]
            for element in self._clsasgpa:
                if not self._grades.get(element):
                    emptysections.append(element)
            return emptysections
        def whatDoINeed(self,title):
            empty=self.checkAmountNotGrades()
            if len(empty)>1 or (title not in empty and len(empty)==1):
                print(f'Can only calculate possible final grades if:\n1) There is only one section with an empty grade (and the user targets that section)\n2)There no empty sections other than the final one needed to be calcuated (assuming that there is another grade for that section that needs to be entered)\n. Please check your inputted grades again\n')
            else:
                if len(self._grades[title])>1:
                    self.calculateGroupGradeRequired(title)
                else: 
                    self.calculateInidivualGradeRequired(title)
        def convertData(self):
            container=[]
            for element in list(self._classgpa):
                container.append([f'section',element,str(self._classgpa[element])])
            for element in list(self._grades):
                container.append([f'grade',element,','.join(map(str,self._grades[element]))])
            return container
        def __str__(self):
            container=''

            for element in self.pullSections():
                    section=self._classgpa[element]
                    try:
                        grades=self._grades[element]
                    except:
                        grades=f'None Entered'
                    average=self.calculateSection(element)
                    container+=f'{section}:\n\tGrades Earned:{grades}\n'
                    container+=f'\tAverage:{average/self._classgpa[element]}\n'
            container+=f'Current Weighted Final grade:{self.getFinalGrade()}'
            return container  




            
