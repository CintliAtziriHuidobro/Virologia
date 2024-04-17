cipher2=""
def get_message2():
     name = 'got'
     ext = 'txt'
     filename = f'{name}.{ext}'
     fo1 = open(filename,"r", encoding="utf8", errors='ignore')
     s = fo1.read()
     s = str(s)
     fo1.close()
     return s
def get_message3():
    return cipher2
def get_key2():
    print ("Ingrese su clave secreta:")
    key2 = input()
    if key2 == '':
        key2 = 'none_public_key'
    return key2
def init_box2(key2):
    """
        Caja S 
    """
    s_box2 = list (range (256)) # Aquí, no importa que la clave sea menor que 256, menos de 256 debe llenarse repetidamente
    j = 0
    for i in range(256):
        j = (j + s_box2[i] + ord(key2[i % len(key2)])) % 256
        s_box2[i], s_box2[j] = s_box2[j], s_box2[i]
    return s_box2

def ex_encrypt2(plain,box2,mode2):
    """
        Use PRGA para generar el flujo de claves y XOR con los bytes de texto cifrado, el mismo algoritmo para el cifrado y descifrado
    """
    if mode2 == '2':
        plain = plain
    res = []
    i = j =0
    for s in plain:
        i = (i + 1) %256
        j = (j + box2[i]) %256
        box2[i], box2[j] = box2[j], box2[i]
        t = (box2[i] + box2[j])% 256
        k = box2[t]
        res.append(chr(ord(s)^k))
    cipher3 = "".join(res)
    if  mode2 == '1':
        fo1=open("gotcifrado.txt","wb+")
                 # La conversión a caracteres visibles requiere codificación
        print ("Salida cifrada:")
        print(cipher3)
        #print(type(cipher3))
        global cipher2
        cipher2 = cipher3
        cipher3 = cipher3.encode()
        fo1.seek(0)
        fo1.write(cipher3)
        fo1.seek(0)
        listsss=[fo1.read(1) for i in range(100)]
        fo1.close()
    if mode2 == '2':
        # La conversión a caracteres visibles requiere codificación
        print ("Salida descifrada:")
        print(cipher3)

def get_mode2():
         print ("Seleccione cifrado o descifrado")
         print("1. Encriptar")
         print("2. Desencriptar")
         mode2 = input()
         if mode2 == '1':
                message2 = get_message2()
                key2 = get_key2()
                box2 = init_box2(key2)
                ex_encrypt2(message2,box2,mode2)
         elif mode2 == '2':
                message2 = get_message3()
                key2 = get_key2()
                box2 = init_box2(key2)
                ex_encrypt2(message2, box2, mode2)
         else:
                print ("¡La entrada es incorrecta!")
if __name__ == '__main__':
    while True:
        get_mode2()