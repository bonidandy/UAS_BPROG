# Bonifasius Dandy Krisnanda
#20210801002

#function
def hitung ():
    a = 6
    b = 5
    c = a+b
    # print("hasil dari a + b :",c)
    print(c)
hitung()


# merupakan fungsi rekursif untuk menemukan faktorial bilangan bulat
def faktorial(x):

    if x == 1:
        return 1
    else:
        return (x * faktorial(x-1))

angka = 9
print ("faktorial dari ", angka , "adalah", faktorial(angka))