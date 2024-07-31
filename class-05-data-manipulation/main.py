# strings 
name = "Emanuel Quintino"
user = 'Platão'
phrase = '"O maior erro que você pode cometer na vida é ter medo de cometer erros" - Platão'

text = """
  [1] - Falar com atendente
  [2] - Promoções
  [3] - Reclamações
"""

print(name)
print(user)
print(phrase)
print(text)

print(name.upper())
print(text.upper())
print(text.lower())
print("joão".capitalize())
print(name.split())
print(name.split(" "))
print(name.split("a"))
print(text.count("vida"))

print(name.replace("i", "_"))
print(name[0])
print(name[-1])
print(name[1:5])
print(name[::-1])

print(len(name))
print(name.index("E"))
print(phrase.index("maior"))
print("Platão" in text)

print(list(name))
print(type(list(name)))
name2 = list(name)
name2.reverse()
print(name2)

# arrays
nums1 = [2, 3, 4]
nums2 = [6, 7, 8]
array_names = ["Ana", "João", "Letícia"]
new_array_names = array_names.copy()

print(nums1 + nums2)
print(4 in nums1)
print(max(nums1))
print(min(nums2))

array_names[0] = "Ana Clara"
array_names.append("Natália")
array_names.append(["João", "Carlos"])
array_names.extend(["João", "Carlos"])
array_names.insert(1, "Cristian")
new_array_names.pop()
array_names.pop()

print(array_names.count("Ana Clara"))
array_names.remove("Pedro")
array_names.clear()

print(array_names.index("Pedro"))
array_names.sort()
array_names.reverse()

print(array_names)
print(new_array_names)
print(array_names[1:])
print(array_names[-2:])

print(len(array_names))

# dictionary

person1 = {
  "name": "Emanuel",
  "age": 30
}

print(type(person1))
print(person1["name"])
print(person1["age"])
person1["id"] = 1
print(len(person1))

print(person1)
print(person1.keys())
print(person1.values())
print(person1.items())

# date