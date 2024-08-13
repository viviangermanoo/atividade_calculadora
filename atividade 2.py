def calculadora(num1, num2, operacao):
  print("Insira aqui um número:")
  input(num1)
  print("Insira aqui outro número:")
  input(num2)
  print("Insira aqui um número equivalente a operação que deseja realizar, sendo:")
  print("1 - Adição")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  int(input())
def alguma_funcao(num1, num2, operacao):
  if operacao == 1:
        return num1 + num2  
  elif operacao == 2:
        return num1 - num2  
  elif operacao == 3:
        return num1 * num2  
  elif operacao == 4:
        return num1/num2
    if num2 == 0:
        return "Erro: Divisão por zero"  
    return num1 / num2 
  else:
        return 0 