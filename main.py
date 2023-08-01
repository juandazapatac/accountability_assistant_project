#Codigo para el cálculo de la utilidad de una empresa a partir de sus registros mensuales de contabilidad

import csv

def run():
    with open('./contabilidad.csv') as csvfile:
        reader=csv.reader(csvfile)
        header=next(reader)
        #Version 1
        tuplas_contabilidad=[(int(row[1]),int(row[2])) for row in reader]
        suma_ventas=0
        suma_gastos=0
        for i in tuplas_contabilidad:
            suma_ventas+=i[0]
            suma_gastos+=i[1]
        print('La utilidad total es:',str(suma_ventas-suma_gastos),'COP')
        
if __name__=='__main__':
    run()
    
