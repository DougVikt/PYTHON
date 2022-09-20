# formando senhas aleatorias 
def senha_aleatoria(n):

    import random as rd
    import string as st
    
    simbol=['@','!','#','$','%','&','*','_','-','/','?','*','+','=',',','.']
    simbolos=rd.choices(simbol, k=n+5)

    letras = rd.choices(st.ascii_letters , k=n+5)

    hexadecimal = rd.choices(st.hexdigits , k=n+5)
    
    senha = rd.sample(letras +simbolos + hexadecimal, n)

    return print(''.join(senha))
    
n=int(input("quantidade de caracters da senha : "))
senha_aleatoria(n)
