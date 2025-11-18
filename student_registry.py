class Student:
    
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade
    
    
    @property
    def name(self):
        return self._name
    
    # Updates the students name only if the student name <br/> is 3 characters
    # or more, holds no spaces or special characters,<br/> and is in title format
    @name.setter
    def name (self, newName):
        if len(newName) >= 3 and (' ' not in newName) and (newName.istitle()):
            self._name = newName
        else:
            print("Please enter a name with no spaces with the first word capitalized.")
    

    @property
    def age (self):
        return self._age
    
    # Updates the students age only if the age value is an int <br/>type, 
    # is greater than 11, and is lower than 18
    @age.setter
    def age (self, newAge):
        if(newAge >=11) and (newAge < 18) and isinstance(newAge, int):
            self._age = newAge
    

    @property
    def grade (self):
        return self._grade
    
    # Updates a students grade only if the grade falls within 9th - 12th grade and the
    # value is formatted with "th" <br/>next to the numbered grade
    @grade.setter
    def grade (self, newGrade):
        if(newGrade.endswith("th") and (int(newGrade[:-2])) >= 9 and (int(newGrade[:-2]) <= 12)):
            self._grade = newGrade
        else:
            print("Please enter a grade between 9th and 12th grade.")

    def __str__(self):
        return f"Student 1: Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def advance(self, years_advanced=1):
        current_grade_num = int(self._grade.removesuffix("th")) #<-- get the grade number
        new_grade = current_grade_num + years_advanced
        self.grade = f"{new_grade}th"
        return f"{self.name} has advanced to the {self.grade} grade"

    def study(self, subject):
        return (f"{self.name} is studying {subject}")


# Start of new objects...
student1 = Student("Henry", 12, "10th")

