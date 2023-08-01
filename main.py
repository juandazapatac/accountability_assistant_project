#Codigo para el cálculo de la utilidad de una empresa a partir de sus registros mensuales de contabilidad

from functools import reduce
from data_importing import import_data

def run():
    data=import_data()
    #Version reduce
    print('La utilidad total es:',str(reduce(lambda x,y:int(x[1])-int(x[2])+int(y[1])-int(y[2]),data)),'COP')
        
if __name__=='__main__':
    run()
    
