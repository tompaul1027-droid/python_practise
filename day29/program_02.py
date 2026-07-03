myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child3"]["year"])
print(myfamily.values())
myfamily["child2"]["year"]=2012
print(myfamily)
myfamily["child1"]["school"]="GPS"
print(myfamily)
del myfamily["child1"]["school"]
print(myfamily)