print("Hello World!")

elhanan=10
sary=20
gad=elhanan+sary

print(gad)

def prueba(num):
	return num*gad

print(prueba(12))

# Function to know wich students have enough credits and GPA to graduate

def graduation_reqs(credits, gpa):
  if credits >= 120 and gpa >= 2:
    return "You meet the requirements to graduate!"
  else:
    return "Sorry, you have failed"
  
print(graduation_reqs(120,3))


# Function to know which number is greater
def greater_than(x,y):
  if x>y:
    return x
  if y>x:
    return y
  if x==y:
    return "These numbers are the same"

# Function to know wich students have enough credits and GPA to graduate

def graduation_reqs(credits, gpa):
  if credits >= 120 and gpa >= 2:
    return "You meet the requirements to graduate!"
  else:
    return "Sorry, you have failed"
  
print(graduation_reqs(120,3))
#Function with multiple rules and multiple outputs

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet any requirement."
  
print(graduation_reqs(3,130))
print(graduation_reqs(3,100))
print(graduation_reqs(1,130))
print(graduation_reqs(1,100))
#Function to convert grades into letters
#Uses def, if, elif, else, return, print

def grade_converter(gpa):
  if gpa >= 4:
    grade = "A"
  elif gpa >= 3:
    grade = "B"
  elif gpa >= 2:
    grade = "C"
  elif gpa >= 1:
    grade = "D"
  elif gpa >= 0:
    grade = "F"
  
  return grade
  
print(
  grade_converter(3.1),"\n",
  grade_converter(2.1),"\n",
  grade_converter(1.1),"\n",
  grade_converter(0.1),"\n",
  grade_converter(6.1),"\n",
  grade_converter(3.1)
)
#Function to except an error from a code

def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:
    print ("Can't divide by zero!")
  
divides(10,0)
#Function for filtering applicants to collage

def applicant_selector(gpa,ps_score,ec_count):
  if gpa>=3 and ps_score>=90 and ec_count>=3:
    return "This applicant should be accepted."
  if gpa>=3 and ps_score>=90 and not ec_count>=3:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."
  

print(
  applicant_selector(3,90,3),"\n",
  applicant_selector(3,90,2),"\n",
  applicant_selector(2,90,3)
)
#Definition of funcrions for different types of shipping
#Ground Transportation
def ground_trans(weight):
  if weight > 10:
    return weight * 4.75 + 20
  elif weight > 6:
    return weight * 4 + 20
  elif weight > 2:
    return weight * 3 + 20
  else:
    return weight * 1.5 + 20
  
#Premium Ground Transportation
premium_trans=125

#Drone Transportation
def drone_trans(weight):
  if weight > 10:
    return weight * 14.25
  elif weight > 6:
    return weight * 12
  elif weight > 2:
    return weight * 9
  else:
    return weight * 4.5

#Function to determine which shipping method is the cheapest
def cheapest(heavy):
  if ground_trans(heavy) < premium_trans and ground_trans(heavy) < drone_trans(heavy):
    return "Ground Transportation is the Cheapest", ground_trans(heavy), "Its your cost."
  if premium_trans < ground_trans(heavy) and premium_trans < drone_trans(heavy):
    return "Premium Transportation is the Cheapest", premium_trans, "its your cost."
  else:
    return "Drone Transportation is the Cheapest", drone_trans(heavy),"its your cost."
  
#Another way to determitante the cheapest shipping method
def cheapest2(heavy):
  ground_cost= ground_trans(heavy)
  premium_cost=premium_trans
  drone_cost=drone_trans(heavy)
  
  if ground_cost < premium_cost and ground_cost < drone_cost:
    return "Ground Transportation is the cheapest", ground_cost, "its your cost"
  
  

print(cheapest(10))
print(cheapest2(20))



#Creating lists
#Uses lists, zip, print
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus","poetry","history"]
grades = [98,97,85,88]

subjects.append("computer science")
grades.append(100)

gradebook =list(zip(subjects, grades))
gradebook.append(("visual arts", 93))

full_gradebook = last_semester_gradebook + gradebook

print(gradebook)
print(full_gradebook)