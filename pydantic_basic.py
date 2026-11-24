
# STEP2:
"""
BASEMODEL+TYPE HINTS
we describe a student Once. Python checks every student against it.

"""

from pydantic import BaseModel,Field,EmailStr

class SimpleStudent(BaseModel):
  name:str
  age:int
  marks:int

s=SimpleStudent(name="Aarav Sharma",age="21",marks=20)
print(s.name,s.age,s.marks)


# Step 3:
"""
FIELT() RULES
gt=greater than     lt=less than
ge=greater or equal  le=less or equal
"""
class RuleStudent(BaseModel):
  name:str=Field(...,min_length=2,max_length=50)     #...=required
  age:int=Field(...,gt=0,lt=100)  #1 to 99
  marks:int=Field(...,gt=0,le=100)  #1 to 100
  course:str="Python"   #default value
  phone:str|None=None   #Optional Field can be empty

s=RuleStudent(name="Rohan Verma",age=21,marks=77)

print(s.name)
print(s.age)
print(s.marks)
print(s.course)
print(s.phone)





# STEP4
""" Email Str
Checks the text really looks like an email.
"""

class EmailStudent(BaseModel):
  name:str
  email:EmailStr


s=EmailStudent(name="Kabir Singh",email="kabirsingh@gmail.com")
print(s.name,s.email)



# STEP 5
"""
Final Student Model
1.field_validator -> Our OWN custom rule
"""

class Student(BaseModel):
  id:str=Field(...,emamples=["S001"])
  name:str=Field(...,min_length=2,max_length=50)
  age:int=Field(...,gt=0,le=100)
  course:str=Field(...,max_length=50)
  marks: int=Field(...,ge=0,le=100)
  email:EmailStr

  # Custom Rule: Name must contain only letters and spaces
  def check_name(cls,value):
    