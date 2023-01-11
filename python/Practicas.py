numero1= input('Numero 1 \r\n')
numero2= input('Numero 2 \r\n')

numero1= int(numero1)
numero2= int(numero2)

class matematicas:
    def sumar(numA, NumB):
        print('EL RESULTADO ES')
        print(numA + NumB)

    def restar(numA, NumB):
        print('EL RESULTADO DE LA RESTA ES')
        print(numA - NumB)

print(matematicas.restar(numero1, numero2))


