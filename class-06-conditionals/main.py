age = 71
cnh = False

if age >= 18:
  print("Maior de idade")
else:
  print("Menor de idade")

if age >= 18 and cnh:
  print("Pode dirigir")
else:
  print("Não pode dirigir")

if age >= 18 and age <= 70: 
  print("Voto obrigatório")
elif age < 16:
  print("Não pode votar")
else:
  print("Voto facultativo")
  
try:
  print(2/"a")
except ZeroDivisionError:
  print("Não pode dividir por zero!")
except TypeError:
  print("Formato inválido!")
except:
  print("Error!")
finally:
  print("Fim da requisição!")

print("running...")