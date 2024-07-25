animes = ["Dragon Ball", "Naruto", "Jojo", "Death Note"]
            # =>  0           1         2          3 
            # <= -4          -3        -2         -1

print(animes)
print(type(animes)) # list
print(animes[0])
print(animes[3])
print(animes[-1])

list = ["A", 123, True, ["B", "C"]]

print(list[0])
print(list[3])
print(list[-1])
print(list[-1][1])

list[2] = False
list[-1][0] = "D"
print(list)
print(len(list)) # length

# tuple
tuple = ("A", 123, True)
print(type(tuple))
print(tuple[1])

# tuple[1] = 798 # error: tuple is immutable

print(tuple)

# dict

dict = {
  "name": "Emanuel",
  "age": 31,
  "is_admin": True
}

print(dict)
print(type(dict))

print(dict["name"])
print(dict["age"])
print(dict["is_admin"])
