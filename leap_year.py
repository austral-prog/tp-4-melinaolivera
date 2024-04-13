def leap_year():
    print("TO DO")
año= int(input('ingrese un año: '))
numero1= (año % 4 == 0)
if (numero1 and not año % 100== 0) or (año % 400 ==0) :
    print (f'El año {año} es bisiesto')

else:
    print (f'El año {año} no es bisiesto')
