import math 
class WeightedGPA:
        def __init__(self):
                self._classgpa={}
                self._grades={}
        def addMassData(self,massdata): #[classification,title,grade/percentage]
            for element in massdata:
                if element[0]=='section':
                    self.addCriteria(element[1],element[2])
                else:
                    self.addGrades(element[1],element[2])
        def addCriteria(self,title,percentage):
            self._classgpa[title]=percentage
        def removeCriteria(self,title):
            del self._classgpa[title]
            del self._grades[title]
        def removeGrades(self,title,grade=-1):
            if grade==-1:
                del self._grades[title]
            else:
                self._grades.remove(grade)
        def addGrades(self,title,grade):
            if self._grades.get(title):
                self._grades[title].append(grade)
            else:
                self._grades[title]=[grade]
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
            total=0
            for element in self._classgpa:
                if not self._grades.get(element):
                    total+=1
            return total
        def whatDoINeed(self,title):
            empty=self.checkAmountNotGrades()
            if empty>1:
                print(f'Can only calculate possible final grades if only one requirement is not yet filled. Please check your inputted grades again\n')
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
                    grades=self._grades[element]
                    average=self.calculateSection(element)
                    container+=f'{section}:\n\tGrades Earned:{grades}\n'
                    container+=f'\tAverage:{average/self._classgpa[element]}\n'
            container+=f'Current Weighted Final grade:{self.getFinalGrade()}'
            return container  




            
