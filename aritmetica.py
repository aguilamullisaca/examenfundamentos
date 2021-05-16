def aritmeticaJAAM():
  #definir variables
  resultado=0
  #datos de entrada
  cantidad1=int(input("ingrese primer digito:"))
  cantidad2=int(input("ingrese segundo digito:"))
  simbolo=input("ingrese signo:")
  #proceso
  if simbolo=="+":
    resultado=cantidad1+cantidad2
  elif simbolo=="-":
    resultado=cantidad1-cantidad2
  elif simbolo=="*":
    resultado=cantidad1*cantidad2
  elif simbolo=="/":
    resultado=cantidad1/cantidad2
  #datos de salida
  print("su respuesta es:", resultado)
aritmeticaJAAM()