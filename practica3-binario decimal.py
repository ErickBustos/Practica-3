##Binario decimal

print("Indique si es binario o decimal")
conversor= input()

##binario-decimal   ----------------------------------------------------
if conversor.lower== "binario":
    print("Si es binario")
    print("dame el numero binario(8digitos): ")
    numero= list(input())
    x= [128,64,32,16,8,4,2,1]
    sumadores=[]
    for i in range(0, len(x)):
        if numero[i]=="1":
            sumadores.append(x[i])
    print("Valor en decimal: ",sum(sumadores))

##decimal-binario   ----------------------------------------------------
if conversor.lower()== "decimal":
    print("Ingrese valor decimal 0-255: ")
    valor= int(input())
    print("El valor ingresado es: ",valor, "tipo", type(valor))
    x=[128,64,32,16,8,4,2,1]
    binario=[0,0,0,0,0,0,0,0]
    
    for e in range(0,len(x)):
        if valor >= x[e]:
            binario[e]=1
            valor=valor-x[e]
        
    print("El valor decimal a binario es: ", binario)
        
        
