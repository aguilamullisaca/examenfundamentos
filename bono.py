def bonoJAAM():
  #definir variables
  salario=1000
  #datos de entrada
  puntos=int(input("ingrese sus puntos:"))
  #proceso
  if puntos>=50 and puntos<=100:
    bono=salario+salario*0.10
  elif puntos>=101 and puntos<=150:
    bono=salario+salario*0.40
  elif puntos>=151:
    bono=salario+salario*0.70
  #datos de salida
  print("su bono es de:", bono)
bonoJAAM()