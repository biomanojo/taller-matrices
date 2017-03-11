#!/usr/bin/env python
# -*- coding: utf-8
import random

class Matriz(object):

    def __init__(self,filas=None,columnas=None):
        if filas:
            self.filas=filas
        else:
            self.filas=int(raw_input("ingrese numero de filas"))
        if columnas:
            self.columnas=columnas
        else:
            self.columnas=int(raw_input("ingrese numero de columnas"))
    def crearMatriz(self):
        self.matriz=[]
        for f in range(self.filas):
            self.matriz.append([0]*self.columnas)


    def imprimirMatriz(self):
         print self.matriz


    def llenarMatriz(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                #self.matriz[f][c] = int(raw_input("Ingrese %d, %d: " %(f,c) ))
                self.matriz[f][c] = random.randint(1,10)
                #matrizB[c][f] = random.randint(5, 15)

    def datam(self):
        return self.matriz

    def validar(self,columnaA,filaB):
        if columnaA != filaB:
            print"no tiene solucion "
            exit()

    def validarsuma(self, columnaA, filaB,columnaB,filaA):
        if (columnaA != columnaB) or (filaA != filaB):
            print"no se puede hacer "
            exit()

    def validarestaMatriz(self, filaA,columnaA, filaB,columnaB):
        if (columnaA != columnaB) or (filaA != filaB):
            print"no se puede hacer "
            exit()

    def multiMatriz(self,matrizA,matrizB,filaB):
        for f in range(self.filas):
            for c in range(self.columnas):
                for k in range(filaB):
                    self.matriz[f][c]+=matrizA[f][k]*matrizB[k][c]

    def sumaMatriz(self,matrizA,matrizB):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c]= matrizA[f][c]+matrizB[f][c]

    def restaMatriz(self,matrizA,matrizB):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c]= matrizA[f][c]-matrizB[f][c]

    def multi_vMatriz(self,matrizA,valor):

        for f in range(self.filas):
            for c in range(self.columnas):
                #for k in range(filaB):
                self.matriz[f][c]=valor*matrizA[f][c]



    def simeMatriz(self):
        band = 'verdadero'
        for f in range(self.filas):
            for c in range(self.columnas):
                if( self.matriz[f][c]!=self.matriz[c][f]):
                    band='falso'
                    break
        if (band == "verdadero") :
             print"es simetrica"
        else:
            print"no es simetrica"

    def trasMatriz(self,matriz1):
            for f in range(self.filas):
                for c in range(self.columnas):
                    self.matriz[f][c] = matriz1[c][f]

            #for f in range(self.columnas):
               #print(self.matriz[f])

    def identidadMatriz(self):
        for f in range(self.filas):
            self.matriz[f][f]=1

    def coMatriz(self, m):
        self.result = []
        for f in m:
            self.result.append(f[:])
        return self.result

    def combiMatriz(self, m, i, j, e):
        n = len(m)
        for c in range(n):
            m[j][c] = m[j][c] + e * m[i][c]

    def cambiofilasMatriz(self, m, i, j):
        m[i], m[j] = m[j], m[i]

    def multifilamatriz(self, m, f, e):
        n = len(m)
        for c in range(n):
            m[f][c] = m[f][c] * e

    def primeMatriz(self, m, i):
        result = i
        while result < len(m) and m[result][i] == 0:
            result = result + 1
        return result

    def determinante(self, matr):
        m = self.coMatriz(matr)
        n = len(m)
        determ = 1
        for i in range(n):
            j = self.primeMatriz(m, i)
            if j == n:
                return 0
            if i != j:
                determ = -1 * determ
                self.cambiofilasMatriz(m, i, j)
            determ = determ * m[i][i]
            self.multifilamatriz(m, i, 1. / m[i][i])
            for k in range(i + 1, n):
                self.combiMatriz(m, i, k, -m[k][i])
        print int(determ)

    def cuadrada(self):
        if self.filas == self.columnas:
            return True
        else:
            return False

    def inversaMatriz(self,matrizA):
        self.determinante(determ)
        print int(determ)
        #for f in range(self.filas):
           # for c in range(self.columnas):
            # for k in range(filaB):
               # self.matriz[f][c] = determ * matrizA[f][c]

    def multipotMatriz(self, matriz1, matriz2, fila):
        res = []
        for f in range(fila):
            res.append([0] * fila)

        for i, row in enumerate(res):
            for j in range(0, len(row)):
                for k in range(0, len(row)):
                    res[i][j] += matriz1[i][k] * matriz2[k][j]
        return res

    def potenciaMatriz(self, pow):
        powerhash = {}
        if pow in powerhash.keys():
            return powerhash[pow]
        if pow == 1:
            return self.matriz
        if pow == 2:
            powerhash[pow] = self.multipotMatriz(self.matriz, self.matriz, self.filas)
            return powerhash[pow]
        if pow % 2 == 0:
            powerhash[pow] = self.multipotMatriz(self.potenciaMatriz(pow / 2), self.potenciaMatriz(pow / 2), self.filas)
        else:
            powerhash[pow / 2 + 1] = self.multipotMatriz(self.potenciaMatriz(pow / 2), self.matriz, self.filas)
            powerhash[pow] = self.multipotMatriz(self.potenciaMatriz(pow / 2), powerhash[pow / 2 + 1], self.filas)
        return powerhash[pow]
