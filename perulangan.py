from array import *
array1 = array('i',[10,20,30,40,50])

# Perkalian
print('__________________________________________________')
perkalian = array1[1] * array1[2]
print('Hasil perkalian antara',array1[1],'dan',array1[2],'adalah',perkalian)
print('___________________________________________________')

#looping pangkat 2
for x in array1:
    #print(x**2)
    result=x**2
    #print(result)
    print('bilangan awal',x,'Hasil Perpangkatan',result)
    
