# Use um input para receber o valor de graus celsius do usuário 
# Defina uma função que receba o valor como parâmetro e converta para fahrenheit
# Imprima a mensagem personaliza dizendo "X graus celsius é igual a Y graus fahrenheit" 

def celsius_to_fahrenheit(celsius):
  fahrenheit = celsius * 1.8 + 32
  return fahrenheit

celsius = float(input("Digite um valor em graus celsius (C°): "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius} graus celsius é igual a {fahrenheit} graus fahrenheit")
