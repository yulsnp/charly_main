alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifrado="TAWF ZWUZG TJGZWJ, DG DGYJSKLW!"
for clave in range(1, len(alfabeto)):
    mensaje=""
    for letra in cifrado.upper():
        if letra in alfabeto:
             indice= alfabeto.find(letra)
             indice-=clave
             if indice <0:
                 indice += 26
             mensaje += alfabeto[indice]
             print(mensaje)
        else:
             mensaje+=letra
print(f"clave:{clave} - {mensaje}")                  