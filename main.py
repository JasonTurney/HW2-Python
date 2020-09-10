# Author: Jason Turney jnt5211@psu.edu

def getGradePoint(grade):
  if grade == "A":
    gradepoint = 4.0
  elif grade == "A-":
    gradepoint = 3.67
  elif grade == "B+":
    gradepoint = 3.33
  elif grade == "B":
    gradepoint = 3.0
  elif grade == "B-":
    gradepoint = 2.67
  elif grade == "C+":
    gradepoint = 2.33
  elif grade == "C":
    gradepoint = 2.0
  elif grade == "D":
    gradepoint = 1.0
  else:
    gradepoint = 0
  return gradepoint

def run():
  gradepoint1 = str(input("Enter your course 1 letter grade: "))
  credit1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint(gradepoint1)}")
  gradepoint1 = str(input("Enter your course 2 letter grade: "))
  credit1 = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {getGradePoint(gradepoint2)}")
  gradepoint1 = str(input("Enter your course 3 letter grade: "))
  credit1 = float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {getGradePoint(gradepoint3)}")
  GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 

if __name__ == "__main__":
  run()