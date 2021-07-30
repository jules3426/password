import time

time.sleep(1)
print('welcome, user')
time.sleep(1)
while True:
    A=input('what is the password?:')
    if A=='simplepasswor':
        break
    else:
        print('wrong try again')
        time.sleep(1)


print('congrats you succeded')
