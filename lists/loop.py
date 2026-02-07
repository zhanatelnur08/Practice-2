family = ["Me", "Dad", "Mom", "Brother", "Sister"]
for x in family:
  print(x)

family = ["Me", "Dad", "Mom", "Brother", "Sister"]
for x in family:
  if x == "Brother":
    break
  print(x)

family = ["Me", "Dad", "Mom", "Brother", "Sister"]
i = 0
while i < len(family):
  print(family[i])
  i = i + 1

family = ["Me", "Dad", "Mom", "Brother", "Sister"]
i = 0
while i < len(family):
  if family[i] == "Brother":
    break
  print(family[i])
  i = i + 1

  