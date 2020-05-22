miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# coloca tu código aquí
#
nuevaLista=[]
for i in range(0,len(miLista)):
  if (miLista[i] in nuevaLista)==False:
    nuevaLista.append(miLista[i])
print(nuevaLista)