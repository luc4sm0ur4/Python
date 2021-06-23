print("Digite o primeiro valor: ")
N1 = int(input())
print("Digite o segundo valor: ")
N2 = int(input())
print("Digite o terceiro valor: ")
N3 = int(input())
print("\nPrimeiro valor:",N1 ,"\nSegundo valor:",N2 ,"\nTerceiro Valor:",N3 )

maior=menor=meio=0
if N1>=N2 and N1>=N3:   
    maior=N1
    if N2>=N3:
        meio=N2
        menor=N3
    else:
        meio=N3
        menor=N2
if N2>=N1 and N2>=N3:
    maior=N2
    if N1>=N3:
        meio=N1
        menor=N3
    else:
        meio=N3
        menor=N1 
if N3>=N1 and N3>=N2:
    maior=N3
    if N1>=N2:
        meio=N1
        menor=N2
    else:
        meio=N2
        menor=N1
        
print("\nMenor={} \nMeio={} \nMaior={}".format(menor,meio,maior))
