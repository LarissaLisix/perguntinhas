nome=input('Qual seu nome?: ')
nasc=int(input('em que ano você naceu?:'))
an=int(input('em que ano estamos?'))
idade = an-nasc
if nasc==an:
    print(f'Nossa impressionante {nome}, você tem exatamente {idade} anos, suspeitoooo!')

gt=input('O que você gosta?: ')
tb=int(input('Qual é a sua ocupação? Digite o número correspondente \n0-desocupado \n1-estudante \n2-universitario \n3-trabalhador: \n'))

if tb==1:
    print('logo voê chegara na etapa da vida, que não estará tão animada!')
elif tb==0 and idade>=18:
    print(f'você já tem {idade} anos, já está na hora de fazer alguma coisa, amigo(a)')
    print(f'Olha {nome}, eu sei que você gosta de {gt}, mais está na hora de crescer!')
elif tb==0 and idade<=17:
    print(f'Bom recomendo você já pensar o que vai fazer! quanto mais cedo melhor')

elif tb==3:
    print(f'Olha interessante {nome}!')
    trabalho=input('Qual sua profisão?: ')
    print(f'uau incrive! ser um {trabalho} parece ser dificil! continue crescendo e sendo um ótimo profissional {nome}!')
          
else:
    print('Olha só! você já é veterana na vida adulta parabéns! pelo sofrimento')

print(f'Em todo caso deixando as formalidades prazer em conhecer você {nome}!')

resp=input('R: ')

print(f'foi bom nossa conversa! até breve {nome}')

