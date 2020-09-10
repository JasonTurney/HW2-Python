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
  return float(gradepoint)

def run():
  gradepoint1 = str(input("Enter your course 1 letter grade: "))
  credit1 = float(input("Enter your course 1 credit: "))
  gradepoint1 = getGradePoint(gradepoint1)
  print(f"Grade point for course 1 is: {gradepoint1}")
  gradepoint2 = str(input("Enter your course 2 letter grade: "))
  credit2 = float(input("Enter your course 2 credit: "))
  gradepoint2 = getGradePoint(gradepoint2)
  print(f"Grade point for course 2 is: {gradepoint2}")
  gradepoint3 = str(input("Enter your course 3 letter grade: "))
  credit3 = float(input("Enter your course 3 credit: "))
  gradepoint3 = getGradePoint(gradepoint3)
  print(f"Grade point for course 3 is: {gradepoint3}")
  GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 
  print(f"Your GPA is: {GPA}")  

if __name__ == "__main__":
  run()