family=["Me","Dad","Mom","Brother","Sister"]
New_family =[]
for x in family:
    New_family.append(x)
print(New_family)

family=["Me","Dad","Mom","Brother","Sister"]
New_family = [x for x in family]
print(New_family)

family=["Me","Dad","Mom","Brother","Sister"]
New_family = [x for x in family if x != "Brother"]
print(New_family)

family=["Me","Dad","Mom","Brother","Sister"]
New_family = [x for x in family if x == "Brother"]
print(New_family)
