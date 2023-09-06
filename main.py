# write your code here
person = {
    "name" : "Layla",
    "age" : 15,
    "hobbies" : ["Digital art", "Crocheting", "Sewing", "Baking", "Coding", "Painting", "Writing"]
}
print (person["name"])
print (person["age"])
person["age"] = 13
person["country"] = "Kuwait"
print(person)
print(len(person))
person["hobbies"].append("Swimming")
def check_hobbies(person):
    if len(person["hobbies"])>3:
      print("WOW YOU ARE AMAZING")
    else:
       print("Nice")
  
check_hobbies()