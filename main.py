#Codigo para el cálculo de la utilidad de una empresa a partir de sus registros mensuales de contabilidad

import csv
from functools import reduce

def run():
    with open('./contabilidad.csv') as csvfile:
        reader=csv.reader(csvfile)
        header=next(reader)
        #Version reduce
        print('La utilidad total es:',str(reduce(lambda x,y:int(x[1])-int(x[2])+int(y[1])-int(y[2]),reader)),'COP')
        
if __name__=='__main__':
    run()
    
