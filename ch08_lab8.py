# ch08_lab8.py

def switch():
    global state

    if  state =='OFF':
        state = 'ON'
       
    else :
        state = 'OFF'

    print(f'전구 {state}')

state = 'OFF'
switch()
switch()    
switch()
switch()
