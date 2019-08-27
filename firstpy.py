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