data={
  "S001":{
    "name":"ram"
  },
  "S002":{
    "name":"sita"
  },
  "S003":{
    "name":"gaurab"
  }
}
response =[result.get("name") for result in data.values()]
print(response)