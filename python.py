#Adivinhação de número:
numeroAdivinhacao = 10
chute = int(input("jogador, tente adivinhar o número: "))

while chute != numeroAdivinhacao:
  if chute < numeroAdivinhacao:
    print("Errou! O número é maior")
  elif chute > numeroAdivinhacao:
    print("Errou! O número é menor")
  chute = int(input("Tente novamente: "))

print("Parabéns!!! Você acertou!")