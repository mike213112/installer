file = open('requirements/Nginx/masterip.txt','r')

dato = file.read()
datos = dato.split('$')

for i in datos:
    x = i.split('\n')
    print(x)
