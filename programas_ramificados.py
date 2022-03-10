# num_1 = int(input('Escoge un entero: '))
# num_2 = int(input('Escoge otro entero: '))

# if num_1 > num_2:
#     print('El primer numero es mayor que el segundo')
# elif num_1 < num_2:
#     print('El segundo numero es mayor que el primero')
# else:
#     print('Los dos numeros son iguales')


usr_1 = input('Nombre del usuario 1: ')
usr_2 = input('Nombre del usuario 2: ')

edad_us_1 = int(input(f'Que edad tienes {usr_1}? '))
edad_us_2 = int(input(f'Que edad tienes {usr_2}? '))

if edad_us_1 > edad_us_2:
    print(f'Hey! {usr_1} es mayor que tú {usr_2}')
elif edad_us_1 < edad_us_2:
    print(f'Hey! {usr_2} es mayor que tú {usr_1}')
else:
    print('Hey, ustedes tienen la misma edad!')

