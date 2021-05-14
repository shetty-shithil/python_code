dict={"name":"ABC","age":20,"gender":"male"}
dict["college"]="XYZ"
print(dict)
dict.pop("gender")
print(dict)
myfamily = {
  "child1" : {
    "name" : "hij",
    "year" : 2004
  },
  "child2" : {
    "name" : "klm",
    "year" : 2007
  },
  "child3" : {
    "name" : "asd",
    "year" : 2011
  }
}
print(myfamily)
a=dict.values()
b=myfamily.values()
print(b)
print(a)
print(dict.get("age"))
print(myfamily.get("child1"))
z=dict.keys()
print(z)
del myfamily
print(myfamily)
