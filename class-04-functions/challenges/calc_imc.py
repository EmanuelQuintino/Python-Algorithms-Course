# Defina uma função que receba como parâmetros altura e peso e retorne o IMC

def calc_imc(height, weight):
  imc = weight / (height * height)
  return imc

height = float(input("Digite sua altura(m): "))
weight = float(input("Digite seu peso(kg): "))
imc = calc_imc(height, weight) 

print(f"Seu IMC é {imc:.2f}")
