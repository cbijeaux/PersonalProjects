import math 
class WeightedGPA:
        def __init__(self):
                self._classgpa={}
                self._grades={}
                self._percentage=0
        def addMassData(self,massdata): #[classification,title,grade/percentage]
            for element in massdata:
                element=element.split(',')
                if element[0]=='section':
                    self.addCriteria(element[1],int(element[2]),False)
                elif '|' in element[2]:
                    grades=element[2].split('|')
                    map(int,element[2].split('|'))
                    self.addBatchGrades(element[1],grades,False)
                else:
                    self.addGrades(element[1],int(element[2]),False)
        def checkPercentage(self,newpercentage):
            if self._percentage+newpercentage>100:
                return False
            else:
                return True
        def addCriteria(self,title,percentage,message=True):
            if self.checkPercentage(percentage):
                self._classgpa[title]=percentage
                self._percentage+=percentage
                if message:
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
        def addGrades(self,title,grade,message=True):
            if self._grades.get(title):
                self._grades[title].append(int(grade))
                if message:
                    print(f'Grade of {grade} Added to {title}')
            else:
                self._grades[title]=[int(grade)]
                if message:
                    print(f'Grade of {grade} added to {title}')
        def pullGrades(self,title):
            if self._grades.get(title):
                return self._grades[title]
            else:
                return f'No Grades Yet Entered'
        def addBatchGrades(self,title,batchofgrades,message=True): 
            for grade in batchofgrades:
                self.addGrades(title,grade,message)
        def calculateCurrentGrade(self):
            total=0
            for element in list(self._grades):
                if self._grades.get(element):
                    total+=(sum(self._grades[element])/len(self._grades[element]))*(self._classgpa[element]/100)
            return total
        def getFinalGrade(self):
            return self.calculateCurrentGrade()
        def calculateSection(self,title):
            return (sum(self._grades[title])/len(self._grades[title]))*self._classgpa[title]
        def calculateAverage(self,title):
            return sum(self._grades[title])/len(self._grades[title])
        def pullSections(self):
            return list(self._classgpa.keys())
        def calculateGroupGradeRequired(self,title):
            grades={"A":90,"B":80,"C":70}
            container=f'The result for possible final grade depending on the final {title} grade:\n'
            percentage=self._classgpa[title]
            currentgrade=self.calculateCurrentGrade()
            numberoftotalgrades=len(self._grades[title])+1
            totalgradesofcurrentsection=sum(self._grades[title])
            gradeswithoutsection=currentgrade-self.calculateSection(title)
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
                    finalrequired=math.ceil((left/percentage)*100)
                    container+=f'{element} Grade requires {finalrequired} in {title}\n'
            print(container)
        def checkAmountNotGrades(self):
            emptysections=[]
            for element in self._classgpa:
                if not self._grades.get(element):
                    emptysections.append(element)
            return emptysections
        def whatDoINeed(self,title):
            empty=self.checkAmountNotGrades()
            if len(empty)>1 or (title not in empty and len(empty)==1):
                print(f'Can only calculate possible final grades if:\n1) There is only one section with an empty grade (and the user targets that section)\n2)There no empty sections other than the final one needed to be calcuated (assuming that there is another grade for that section that needs to be entered)\n. Please check your inputted grades again\n')
            else:
                if self._grades.get(title) and len(self._grades[title])>1:
                    self.calculateGroupGradeRequired(title)
                else: 
                    self.calculateInidivualGradeRequired(title)
        def convertData(self):
            container=[]
            for element in list(self._classgpa):
                container.append([f'section',element,str(self._classgpa[element])])
            for element in list(self._grades):
                container.append([f'grade',element,'|'.join(map(str,self._grades[element]))])
            return container
        def __str__(self):
            container=''
            for element in self.pullSections():
                    section=element
                    sectionpercentage=self._classgpa[element]
                    try:
                        grades=self._grades[element]
                        average=self.calculateSection(element)
                        container+=f'{section}:\n\tGrades Earned:{grades}\n'
                        container+=f'\tAverage:{self.calculateAverage(element)}\n'
                    except:
                        grades=f'None Entered'
                        average=f'Could Not be Calculated'
                        container+=f'{element} [%{sectionpercentage}]:\n\tGrades Earned:{grades}\n'
                        container+=f'\tAverage:{average}\n'
            container+=f'Current Weighted Final grade:{self.getFinalGrade()}'
            return container  




            
