#!/usr/bin/python3

class laboratorioPhyton1:
  
  def pedirCaracter (self, mensaje):
    caracter = input(mensaje)
    print(" ")
    return caracter
  
  def pedirValor (self, mensaje): 
    valorValido = False
    while (valorValido == False):
      try: 
        alturaPiramide = int(input(mensaje))
        if (alturaPiramide <= 0):
          print(" ")
          print("Por favor ingrese un número mayor a 0.")
          print(" ")
          self.pedirValor
        else:
          valorValido = True
      except:
        print (" ")
        print ("Por favor ingrese un valor válido.")
        print(" ")
    return alturaPiramide
  
  def construccionPiramide (self, caracter, altura):
   print ("\n")
   for x in range (altura, 0, -1):
      for i in range (0, x, 1):
        print (caracter, end =" ")
      print (" ")
   print ("\n")
      


  def controlador (self):
    caracter = self.pedirCaracter("Por favor ingrese el caracter a utilizar para la construcción de la pirámide: ")
    altura = self.pedirValor("Por favor ingrese un valor númerico para determinar la altura de la pirámide: ")
    self.construccionPiramide(caracter, altura)

miInstancia = laboratorioPhyton1()
miInstancia.controlador()


