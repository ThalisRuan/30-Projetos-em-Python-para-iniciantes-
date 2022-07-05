
# Importe a biblioteca "random" para gerar numeros aleatorios
import random 

# Defina a string que sera mostrada para o usuario (input), para que ele digite o numero.
maior_do_range = input("Digite um numero: ")

numero_random = random.randrange(-25, 100)

# Defina as condicoes que a logica ira ocorrer.
# Se "maior do range for <=0, gere um numero que esteja entre o numero 0 e o numero que foi adicionado na "string".
if  maior_do_range.isdigit():
    maior_do_range = int(maior_do_range)

    if maior_do_range <= 0:
        print('Digite um numero maior que zero')
        quit()

maior_do_range = random.randint(0, maior_do_range)
palpites =  0    

# Crie um looping para cadastrar as perguntas 

while True:
    palpites += 1
    usuario = input("Advinhe")
    if  usuario.isdigit():
        usuario = int(usuario)
    else:
        print('Digite novamente o numero')
        continue 

    if usuario == maior_do_range:
        print("voce acertou")
        break 
    elif usuario > maior_do_range:
            print("voce esta perto ")
    else: 
            print("voce esta longe do numero")
            
print ("Voce acertou em ", palpites , " palpites, Parabens")








