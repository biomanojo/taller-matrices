#!/usr/bin/env python
# -*- coding: utf-8
import matriz

def main():

    while True:
        print """
        seleccione una opcion:
        a Multiplicar Matriz
        b Sumar Matriz
        c Restar Matriz
        d Multiplicar la Matriz por un Numero
        e Matriz Simetrica
        f Matriz Identica
        g Matriz Traspuesta
        h Matriz Determinante
        i Matriz Potencia
            """

        opcion=raw_input("Ingrese Una Opcion : ")
        if opcion == "a":
            print "______MULTIPLICACION______"
            print" ______MATRIZ A______"
            matrizA=matriz.Matriz()
            matrizA.crearMatriz()
            #matrizA.imprimirMatriz()
            matrizA.llenarMatriz()
            matrizA.imprimirMatriz()

            print"_________MATRIZ B________"
            matrizB = matriz.Matriz()
            matrizB.crearMatriz()
           # matrizB.imprimirMatriz()
            matrizB.llenarMatriz()
            matrizB.imprimirMatriz()


            print"___RESULTADO DE LA MULTIPLICACION________"


            matrizB.validar(matrizA.columnas,matrizB.filas)
            matrizc = matriz.Matriz(matrizA.filas,matrizB.columnas)
            matrizc.crearMatriz()
            #matrizc.imprimirMatriz()
            matrizc.multiMatriz(matrizA.datam(),matrizB.datam(),matrizB.filas)
            matrizc.imprimirMatriz()

            opcion = raw_input("enter para ir a menu : ")
        elif opcion == "b":

            print "____SUMA MATRIZ___"
            print" ______MATRIZ A______"

            matrizA=matriz.Matriz()
            matrizA.crearMatriz()
            #matrizA.imprimirMatriz()
            matrizA.llenarMatriz()
            matrizA.imprimirMatriz()

            print"_________MATRIZ B________"
            matrizB = matriz.Matriz()
            matrizB.crearMatriz()
           # matrizB.imprimirMatriz()
            matrizB.llenarMatriz()
            matrizB.imprimirMatriz()

            print" _____SUMA_______"
            matrizB.validarsuma(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)
            matrizA.validarsuma(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)

            matrizc = matriz.Matriz(matrizA.filas,matrizB.columnas)
            matrizc.crearMatriz()
            #matrizc.imprimirMatriz()
            matrizc.sumaMatriz(matrizA.datam(),matrizB.datam())
            matrizc.imprimirMatriz()

            opcion = raw_input("enter para ir a menu : ")
        elif opcion == "c":

            print" _____RESTA_______"
            print" ______MATRIZ A______"
            matrizA = matriz.Matriz()
            matrizA.crearMatriz()
            # matrizA.imprimirMatriz()
            matrizA.llenarMatriz()
            matrizA.imprimirMatriz()

            print"_________MATRIZ B________"
            matrizB = matriz.Matriz()
            matrizB.crearMatriz()
            # matrizB.imprimirMatriz()
            matrizB.llenarMatriz()
            matrizB.imprimirMatriz()
            print"_______RESTA_______"

            matrizA.validarestaMatriz(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)
            matrizB.validarestaMatriz(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)

            matrizc = matriz.Matriz(matrizA.filas, matrizB.columnas)
            matrizc.crearMatriz()
            #matrizc.imprimirMatriz()
            matrizc.restaMatriz(matrizA.datam(), matrizB.datam())
            matrizc.imprimirMatriz()

            #opcion = raw_input("enter para ir a menu : ")
        elif opcion == "d":

            print" ______MULTIPLICACION POR VALOR______"

            print" ______MATRIZ A______"
            matrizA = matriz.Matriz()
            matrizA.crearMatriz()
            # matrizA.imprimirMatriz()
            matrizA.llenarMatriz()
            matrizA.imprimirMatriz()

            valor = int(raw_input("ingrese valor"))
            matrizd = matriz.Matriz(matrizA.filas, matrizA.columnas)
            matrizd.crearMatriz()
            matrizd.multi_vMatriz(matrizA.datam(), valor)
            matrizd.imprimirMatriz()

            #opcion = raw_input("enter para ir a menu : ")
        elif opcion == "e":

            print"__________MATRIZ SIMETRICA____"
            print" ______MATRIZ A______"
            matrize = matriz.Matriz()
            matrize.crearMatriz()
            # matrizA.imprimirMatriz()
            matrize.llenarMatriz()
            matrize.simeMatriz()
            matrize.imprimirMatriz()

            #opcion = raw_input("enter para ir a menu : ")
        elif opcion == "f":

            print"______IDENTIDAD________"
            matrize = matriz.Matriz()
            matrize.crearMatriz()
            # matrizA.imprimirMatriz()
            # matrize.llenarMatriz()
            matrize.identidadMatriz()
            matrize.imprimirMatriz()

        #opcion = raw_input("enter para ir a menu : ")
        if opcion == "g":
            print"______TRASPUESTA________"

            print" ______MATRIZ A______"

            matrizA = matriz.Matriz()
            matrizA.crearMatriz()
            matrizA.llenarMatriz()
            matrizA.imprimirMatriz()

            matrizd = matriz.Matriz(matrizA.columnas, matrizA.filas)
            matrizd.crearMatriz()
            matrizd.trasMatriz(matrizA.datam())
            matrizd.imprimirMatriz()

            #opcion = raw_input("enter para ir a menu : ")
        elif opcion == "h":

            print"______DETERMINANTE________"

            print" ______MATRIZ A______"
            matrizA = matriz.Matriz()
            matrizA.crearMatriz()
            # matrizA.imprimirMatriz()
            matrizA.llenarMatriz()
            matrizA.determinante(matrizA.datam())

        elif opcion == "i":

            print"______POTENCIA________"

            print" ______MATRIZ A______"
            matrizA = matriz.Matriz()
            matrizA.crearMatriz()
            matrizA.llenarMatriz()
            matrizA.imprimirMatriz()
            pot = int(raw_input("Ingrese potencia"))
            print matrizA.potenciaMatriz(pot)

if __name__=='__main__':
    main()


