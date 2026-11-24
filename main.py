from fastapi import FastAPI,HTTPException, Path, Query
import json
app=FastAPI()


@app.get("/")
def greet():
  return {"Hello and Welcome to Sheryians AI School"}

def load_data():
  with open("students.json","r", encoding="utf-8") as file:
      data=json.load(file)
      return data

"""Path Parameter"""
# student_id-> This is our path parameter
@app.get("/student/{student_id}")
def get_id(student_id:str):
  student_id:str=Path(...,description="The Id of the student",examples=["S001"])
  data=load_data()
  if student_id not in data:
      raise HTTPException(
        status_code=404,
        detail=f"Student with id {student_id} does not exists"
      ) 
  return data[student_id]


# @app.get('/filter')
# def filter_student(course:str=None):
#   data=load_data()
#   if course is None:
#      return data
#   filtered={}
#   for student_id, info in data.items():
#      if info["course"].lower()==course.lower():
#         filtered[student_id]=info
#   return filtered

"""Qury Parameter"""
@app.get('/filter')
def filter_student(course:str=Query(None,description="show only students in this course",examples="python")):
  data=load_data()
  if course is None:
     return data
  filtered={}
  for student_id, info in data.items():
     if info["course"].lower()==course.lower():
        filtered[student_id]=info
  return filtered


SORT_FIELDS=["marks","age","name"]
SORT_ORDER=["asc","desc"]
@app.get("/sort")
def sort_students(
   sort_by:str=Query(None,description="Sort by marks,name,age",examples=["marks"]),
   order:str=Query("asc",description="asc or desc",examples=["asc","desc"])):
   if sort_by not in SORT_FIELDS:
      raise HTTPException(status_code=404,detail=f"Invalid sort_by '{sort_by}, Choose from {SORT_FIELDS}")
   if order not in SORT_ORDER:
      raise HTTPException(status_code=404,detail=f"Invalid order {order}. Choose from {SORT_ORDER}")
   data=load_data()
   student=[]
   for student_id,info in data.items():
      info["id"]=student_id
      student.append(info)
  #  Step-2 Sort the list by the choosen field
   reverse=(order=="desc")
   sorted_students=sorted(student,key=lambda s: s[sort_by],reverse=reverse)
   return sorted_students

"""
Pagination\
http://127.0.0.1:8000/paginate?page=1&limit=2

page-> which page you want t
limit->how many students(records) on one page

Formula
start=(page-1)*limit
end=start+limit
"""
@app.get("/paginate")
def paginate_student(page:int=Query(1,ge=1,description="Which page you want(start from 1)"),limit:int=Query(2,ge=1,le=100,description="how many students on one page (1 to 100)")):
   data=load_data()
   # Turn the dictionary into a list,putting the ID inside each student
   student=[]
   for student_id,info in data.items():
      info['id']=student_id
      student.append(info)
   start=(page-1)*limit
   end=start+limit
   page_student=student[start:end]
   total_students=len(student)
   return {
      "page":page,
      "limit":limit,
      "total_students":total_students,
      "students":page_student
   }
   