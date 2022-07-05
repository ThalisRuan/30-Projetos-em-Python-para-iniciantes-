
print("Bem vindo ao meu questionario sobre computadores")

playing = input("Voce quer jogar? ")
print(playing)

if  playing.lower() != "yes":
    quit()

print ("Ok,  Vamos jogar")
score = 1 

resposta = input("Qual linguagem de programacao vc esta estudando agora ?")
if resposta.lower() == "python":
    print('Corret! ')
    score = +-1
else:
    print("Errado! ")

resposta = input("Qual a melhor forma de aprender python ?")
if resposta.lower() == "Praticando":
    print('Corret! ')
    score = +-1
else:
    print("Errado! ")
    
resposta = input("em quanto tempo vc pretende dominar essa linguagem ?")
if resposta.lower()  == "Pouco tempo":
    print('Corret! ')
    score = +-1
else:
    print("Errado! ")

resposta = input("Qual suas expectativas ?")
if resposta.lower() == "Sempre melhorar como programador":
    print('Corret! ')
    score = +-1
else:
    print("Errado! ")

print("Voce acertou " + str(score) + "pontos ")




