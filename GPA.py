import math 
class GPA:
        def __init__(self):
                self._totalgrade=0
                self._classgpa={}
                self._grades={}
        def addCriteria(self,title,percentage):
            self._classgpa[title]=percentage
        def addGrades(self,title,grade):
            if self._grades.get(title):
                self._grades[title].append(grade)
            else:
                self._grades[title]=[grade]
        def addBatchGrades(self,title,batchofgrades):
            self._grades[title]=batchofgrades  
        def calculateCurrentGrade(self):
            total=0
            for element in list(self._grades):
                if self._grades.get(element):
                    total+=(sum(self._grades[element])/len(self._grades[element]))*self._classgpa[element]
            return total
        def getFinalGrades(self):
            print(self.calculateCurrentGrade())
        def calcualteSection(self,title):
            return (sum(self._grades[title])/len(self._grades))*self._classgpa[title]
        def calculateGroupGradeRequired(self,title):
            grades={"C":70,"B":80,"A":90}
            container=''
            currentsectionaverage=self.calcualteSection(title)
            currentgrade=self.calculateCurrentGrade()
            for element in list(grades):
                needed=grades[element]-(currentgrade-currentsectionaverage)
                if needed<0:
                    container+=f'{element} grade guaranteed\n'
                elif needed>self._classgpa[title]*100:
                    container+=f'{element} grade not possible\n'
                else: 
                    
        def calculateInidivualGradeRequired(self,title):
            grades={"C":70,"B":80,"A":90}
            container=''
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

            
gpa=GPA()
gpa.addCriteria(f'examone',.15)
gpa.addCriteria(f'examtwo',.15)
gpa.addCriteria(f'homework',.15)
gpa.addCriteria(f'quiz',.15)
gpa.addCriteria(f'project',.40)
gpa.addBatchGrades(f'homework',[100,90])
gpa.addBatchGrades(f'quiz',[100,80])
gpa.addGrades(f'examone',81)
gpa.addGrades(f'examtwo',74)
gpa.addGrades(f'project',40)
gpa.getFinalGrades()
gpa.whatDoINeed(f'homework')



            