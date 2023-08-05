#Codigo para el cálculo de la utilidad de una empresa a partir de sus registros mensuales de contabilidad

from functools import reduce
from data_importing import import_data

def run():
    data=import_data()
    #Version reduce
    ventas=[row[1] for row in data]
    gastos=[row[2] for row in data]
    print(reduce(lambda x,y:int(x)+int(y),ventas)-reduce(lambda x,y:int(x)+int(y),gastos))
        
if __name__=='__main__':
    run()
    
