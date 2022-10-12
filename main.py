
# Practica 2

import numpy as np

print('Este programa es para aplicar las ecuaciones diferenciales. \n')
print('¿Que aplicación te gustaria utilizar?')
print('1) Ley de enfriamiento de Newton')
print('2) Ley de Dinamica poblacional')
opcion = (str(input('Aplicación a elegir: ')))

if opcion == '1':

    print('1) Calcular tiempo especifico')
    print('2) Calcular temperatura especifica')
    print('3) Calcular temperatura inicial')
    inciso = (str(input('Aplicación a elegir: ')))
    if inciso == '1':
        print('Datos de entrada')
        Ta = (float(input('Ingresa la temperatura ambiente (oC): ')))
        Tin = (float(input('Ingresa la temperatura inicial (oC): ')))
        t1 = (float(input('Ingresa el tiempo de la siguiente muestra: ')))
        T1 = (float(input('Ingresa la siguiente muestra de la temperatura: ')))
        n = (float(input('Valor de la temperatura en el tiempo a conocer: ')))

        # Formula para determinar el tiempo
        c = (Tin - Ta)

        k = np.log((T1 - Ta) / c) / t1

        t = np.log((n - Ta) / c) / k

        print('\n')
        print('El tiempo cuando la temperatura vale %s es: ' % n)
        print(t)

    elif inciso == '2':
        print('Datos de entrada')
        Ta = (float(input('Ingresa la temperatura ambiente (oC): ')))
        Tin = (float(input('Ingresa la temperatura inicial (oC): ')))
        T1 = (float(input('Ingresa la siguiente muestra de la temperatura: ')))
        n = (float(input('Hasta que tiempo deseas saber la temperatura: ')))

        # Formula de ley de enfriamiento
        c = (Tin - Ta)

        k = np.log((T1 - Ta) / c)

        T = Ta + c * np.exp(k * n)

        print('\n')
        print('La temperatura en el tiempo %s es: ' % n)
        print(T)

    elif inciso == '3':
        print('Datos de entrada')
        Ta = (float(input('Ingresa la temperatura ambiente (oC): ')))
        t2 = (float(input('Tiempo en la segunda muestra: ')))
        T2 = (float(input('Temperatura en la muestra (oC): ')))
        t3 = (float(input('Tiempo en la tercer muestra: ')))
        T3 = (float(input('Temperatura en la muestra (oC): ')))

        # Formula de ley de enfriamiento
        T0 = Ta + (T2 - Ta / np.exp(np.log(T3-Ta/T2-Ta) / t3 - t2) * t2)

        print('\n')
        print('La temperatura inicial es: ')
        print(T0)
elif opcion == '2':
    print('1) Calcular tiempo especifico')
    print('2) Calcular población especifica')
    print('3) Calcular poblacion inicial')
    incisos = (str(input('Aplicación a elegir: ')))
    if incisos == '1':
        print('Datos de entrada')
        Pin = (float(input('Ingresa la poblacion inicial: ')))
        Tm = (float(input('Tiempo de la siguiente muestra: ')))
        Pm = (float(input('Ingresa la muestra de la poblacion: ')))

        n = (float(input('Valor de la poblacion en el tiempo a conocer: ')))

        # Formula para determinar el tiempo


        k = np.log(Pm / Pin) / Tm

        t = np.log(n / Pin) / k



        print('\n')
        print('El tiempo cuando la poblacion vale %s es: ' % n)
        print(t)

    elif incisos == '2':
        print('Datos de entrada')
        Pin = (float(input('Ingresa la población inicial: ')))
        Tm = (float(input('Tiempo de la siguiente muestra: ')))
        Pm = (float(input('Población en la muestra: ')))
        n = (float(input('Hasta que tiempo deseas saber la población: ')))

        # Formula del crecimiento poblacional
        c = Pin

        k = np.log(Pm / c) / Tm

        P = c * np.exp(k * n)

        print('\n')
        print('La población en el tiempo %s es: ' % n)
        print(P)

    elif incisos == '3':
        print('Datos de entrada')

        t2 = (float(input('Tiempo en la segunda muestra: ')))
        P2 = (float(input('Poblacion en la muestra: ')))
        t3 = (float(input('Tiempo en la tercer muestra: ')))
        P3 = (float(input('Poblacion en la muestra: ')))

        # Formula de ley de enfriamiento
        k = (1/t3-t2)*(np.log(P3/P2))
        P0 = P2 / (np.exp(k * t2))

        print('\n')
        print('La poblacion inicial es: ')
        print(P0)
