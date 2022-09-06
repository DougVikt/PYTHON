# mini biblioteca simples de calculos diversos 
pi=3.14159265359
class calcular :
    # começando from calcular import calcular 
    # depois so chamar qualquer função  ex: calcular.soma(n1,n2)

    def soma (n1,n2):
        soma = n1+n2 
        return soma

    def subtra(n1,n2):
        subtra = n1-n2 
        return subtra

    def dividir(n1,n2) :
        dividir=n1/n2
        return dividir 

    def multip(n1,n2):
        multip=n1*n2
        return multip

    def potencia(n1,n2=2): # n1 = numero a ser elevado , n2 = a potencia , caso não imformado sera 2
        potencia=n1**n2
        return potencia         

    def raiz(n1): # n1 = numero a calcular raiz
        raiz=n1**(1/2)
        return raiz

    def porcent(n1,n2): # n1 = numero principal , n2 = valor da porcentagem 
        porct=n1*(n2/100)
        return porct
# chamar ex: perimt.quadrado(n1)
class perimt:
        
    def quadrado(n1):
        quadro=4*n1
        return quadro
    
    def circulo(n1):
        circul=2*pi*(n1/2)
        return circul

    def retang(n1,n2):
        retang=2*(n1+n2)    
        return retang

    def triang(n1,n2,n3):
        triang=n1+n2+n3
        return triang

class area:

    def quadrado(n1):
        quadro=n1**2
        return quadro

    def triang(n1,n2):
        triang=(n1*n2)/2
        return triang

    def retang(n1,n2):
        retang=n1*n2
        return retang

    def circulo(n1):
        n1=n1/2
        circu=pi*(n1**2)
