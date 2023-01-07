from time import sleep
#Importei o módulo sleep para organizar melhor as frases impressas e tornar o código mais agradável de ler

#Pequena mensagem de boas-vindas aos clientes em um formato bem convidativo de modo a atrai-los para a cafeteria
print('-='*30)
print('BEM VINDOS A CAFETERIA EAST BLUE!')
print('-='*20)
sleep(1)
print('AQUI VOCÊ ENCONTRARÁ O ONE PIECE!')
print('-='*20)
sleep(1)
print('PREPARADO PARA EMBARCAR NESSA AVENTURA COM A GENTE?')
print('-=')
sleep(1)
print('ENTÂO FAÇA SEU PEDIDO!')
sleep(2)
print('-='*30)
sleep(3)
#Menu de opções contendo código, nome do produto e preço
print("""Menu:
    |COD||PEDIDO||VALOR|
    201-Expresso Luffy-2.50
    202-Latte Sanji-3.00
    203-Cappuccino Usopp-3.50
    204-Cheesecake Zoro sabor brigadeiro-4.50
    205-Croissant Mihawk sabor frango-4.50
    206-Sorvete de creme com passas da Grand Line-3.00
    207-Água Water 7-2.00""")
preco=[2.50,3.00,3.50,4.50,4.50,3.00]
codigo=0
total=0
while True:#Comando em que o cliente irá escolher seu pedido com base nos códigos fornecidos
    codigo=int(input('Digite o código do seu pedido'))
    if codigo==201:
        print(f'Perfeita escolha! Aproveite bem seu expresso forte assim como nosso Rei dos Piratas por um preço simbólico de {preco[0]}')

    elif codigo==202:
        print(f'Ótima opção! Sinta a doçura dessa latte lembrando do melhor chefe de Baratie, só vai custar {preco[1]} ')
    elif codigo==203:
        print(f'O sabor divino desse cappuccino não é mentiroso igual ao nosso capitão... prove por si mesmo por {preco[2]}')
    elif codigo==204:
        print(f'Aprecie esse cheese cake no estilo Santoryo... só precisa de {preco[3]}')
    elif codigo==205:
        print(f'Quer saber se é possível combinar francês e japonês? Então experimente esse croissant por {preco[4]}')
    elif codigo==206:
        print(f'Uma sobremesa pra relaxar? Misteriosa e cheia de vida igual a ilha de Grand Line disponível por {preco[5]}')
    elif codigo==207:
        print(f'A fim de beber só uma água? Mas não qualquer uma, direto da ilha de Water 7 só por {preco[6]}')
    #Definição da posição de cada pedido,a  fim de computar corretamente o valor total
    if codigo in [201,202,203,204,205,206,207]:
        index=codigo-201
        total+=preco[index]
    if codigo < 201 or codigo > 207:
        break


print(f'Essa maravilhosa aventura te custou só {total}, esperamos que tenha valido a pena!!!')
sleep(1)
print('Agradecemos a sua companhia nessa maravilhosa aventura dentro do mundo de One Piece!!!')
sleep(1)
print('-='*30)
print('Até logo e volte sempre, ainda há muito o que se fazer até acharmos o One Piece!!!')
sleep(2)
print('-='*30)
#Mensagem de despedida aos clientes
#Fim do programa
