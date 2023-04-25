class student:
    def __init__(self, name, estates, course):
        if not name:
            raise ValueError("please provide your name")
        if estates not in ["Tena", "outh b", "umoja 1", "umoja 2", "kare"]:
            raise ValueError("invalid estate") 
        self.name = name
        self.course = course
        self.estates = estates

    def __str__(self):
        return f"{self.name} is from {self.estates} and is doing {self.course}"

def main():
    student = get_student()
    print(f"{student[0]} is from {student[1]} and is doing{student[2]}")


    def get_student():
        name = input("what is your name? ").strip()
        estates = input("which estate do you come from? ").strip()  
        course =  input("which course do yo do? ").strip()
        student = student(name, estates, course)
        return student 
    

if __name__ =="__main":
  main()