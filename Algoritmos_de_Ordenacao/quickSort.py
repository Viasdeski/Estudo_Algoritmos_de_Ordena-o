def quickSort(lista):
   quickSortHelper(lista,0,len(lista)-1)

def quickSortHelper(lista,first,last):
   if first<last:

       splitpoint = partition(lista,first,last)

       quickSortHelper(lista,first,splitpoint-1)
       quickSortHelper(lista,splitpoint+1,last)


def partition(lista,first,last):
   pivotvalue = lista[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = lista[leftmark]
           lista[leftmark] = lista[rightmark]
           lista[rightmark] = temp

   temp = lista[first]
   lista[first] = lista[rightmark]
   lista[rightmark] = temp


   return rightmark

lista = input("Insira os números separados por vírgula, os quais deseja ordenar: ")
lista = list(lista)
quickSort(lista)
print(lista)
