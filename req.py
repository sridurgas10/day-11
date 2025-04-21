import requests
import json
url1="https://api.restful-api.dev/objects"
params={"name":"electronics"}

#retrive all objects using get method
res=requests.get(url1,headers={},params=params)

print("ststus1",res.status_code)
print (res.json())

#retrive list of objects  by id using get method
res=requests.get("https://api.restful-api.dev/objects/6",headers={},params=params)
print("ststus2",res.status_code)
print (res.json())

#retrive single object by id using get method
res=requests.get("https://api.restful-api.dev/objects/7",headers={'name':'name'},params={'name':'name'})
print("ststus3",res.status_code)
print (res.json())


#add object using post method
headers = {"content-type": "application/json"}
payload= json.dumps({"id":13,"name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
})
res=requests.post("https://api.restful-api.dev/objects",data=payload, json={},headers=headers)
print("ststus4",res.status_code)
print (res.json())


#update object using put method
headers = {"content-type": "application/json"}
payload= json.dumps({
 
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   },
   "updatedAt": "2022-12-25T21:08:41.986Z"
})
res=requests.put("https://api.restful-api.dev/objects/ff808181932badb6019656de26622f4f",data=payload,headers=headers)
print("ststus5",res.status_code)
if res.status_code==200:
  print( {"message": "Object with id = 13, has been updated ."})
  print (res.json())
else:
  print("no url found")  


#Partially update object using patch method

headers = {"content-type": "application/json"}
payload= json.dumps({
   "name": "Apple MacBook Pro 16 (Updated Name)"

})

res=requests.patch("https://api.restful-api.dev/objects/ff808181932badb6019656de26622f4f",data=payload,headers=headers)
print("ststus6",res.status_code)
if res.status_code==200:
  print( {"message": "Object with id = 13, has been updated partially."})
  print (res.json())
  
else:
  print("no url found")  


#Delete object using delete method
headers = {"content-type": "application/json"}
payload= json.dumps({"id":14,"name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
})
res=requests.post("https://api.restful-api.dev/objects",data=payload, json={},headers=headers)
print("ststus4",res.status_code)
print (res.json())

res=requests.delete("https://api.restful-api.dev/objects/fff808181932badb6019656e10f022f57")
print("ststus7",res.status_code)
if res.status_code==200:
  print( {"message": "Object with id = 14, has been deleted."})
  print (res.json())
else:
  print("no url found")  
