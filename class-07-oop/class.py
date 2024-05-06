# OOP

class Car:
  def __init__(self, brand, model, year, fipe, offer):
    self.brand = brand
    self.model = model
    self.year = year
    self.offer = offer
    self.fipe = fipe
  
  def info(self):
    return (self.brand, self.model, self.year)
  
  def sale(self):
    if self.offer >= self.fipe:
      return "Carro vendido!"
    else:
      return "Sai pra lá caloteiro!"

myCar1 = Car("Toyota", "SW4", "2024", "345000", "350000")
myCar2 = Car("Chevrolet", "Celta", "2006", "16500", "15000")

print(myCar1.brand)
print(myCar1.model)
print(myCar1.year)

print(myCar2.brand)
print(myCar2.info())
print(myCar2.sale())

