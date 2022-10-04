correo = input("Introduce tu correo electronico")


numarroba = correo.count('@')
  # print(numarroba)

longitud = len(correo)
   # print(longitud)

if((numarroba > 0 and numarroba < 2) and (correo.find('@') != 0) and (correo.rfind('@') != longitud-1)):
        print("correo valido")
else:
        print("correo Invalido")
