#Main

from functools import reduce
from data_importing import import_data

def run():
    respuesta=input('''Welcome to your accounting assistant,          
What would you like to see from present year?
1. Net income
2. Total revenue
3. Total expense
4. Average monthly revenue
5. Average monthly expense
:''')
    data=import_data()
    ventas=[int(row[1]) for row in data]
    gastos=[int(row[2]) for row in data]
    if respuesta=='1':
        print('This year net income is',str(reduce(lambda x,y:x+y,ventas)-reduce(lambda x,y:x+y,gastos)),'COP')
    elif respuesta=='2':
        print('This year total revenue is',str(reduce(lambda x,y:x+y,ventas)),'COP')
    elif respuesta=='3':
        print('This year total expense is',str(reduce(lambda x,y:x+y,gastos)),'COP')
    elif respuesta=='4':
        print('This year average monthly income is',str(reduce(lambda x,y:x+y,ventas)/len(ventas)),'COP')
    elif respuesta=='5':
        print('This year average monthly expense is',str(reduce(lambda x,y:x+y,gastos)/len(gastos)),'COP')
    else:
        print('Try again')
        
if __name__=='__main__':
    run()
    
