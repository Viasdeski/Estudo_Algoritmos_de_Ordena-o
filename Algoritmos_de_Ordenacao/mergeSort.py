def mergeSort(lista):

    if len(lista) > 1:
        mid = len(lista)//2
        lefthalf = lista[:mid]
        righthalf = lista[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lista[k]=lefthalf[i]
                i=i+1
            else:
                lista[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            lista[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            lista[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",lista)

lista = input("Insira os números separados por vírgula, os quais deseja ordenar: ")
lista = list(lista)
mergeSort(lista)
print(lista)
