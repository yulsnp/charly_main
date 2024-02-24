alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifrado= " TAWF ZWUZG TJGLZWJ, DG DGYJSKLW! =) "
for clave in range(0,len(alfabeto)):
    mensaje=""
    for letra in cifrado.upper():
        if letra in alfabeto:
             indice= alfabeto.find(letra)
             indice-=clave
             if indice <0:
                 indice += 26
             mensaje += alfabeto[indice]
    else:
      print(mensaje) 
                  