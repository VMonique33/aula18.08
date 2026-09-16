hamburguer=20
refrigerant=5
batata=8
qtd_hamburguer=int(input("Quantos hamburguer?"))
qtd_refrigerante=int(input("Quantos refrigerante?"))
qtd_batata=int(input("Quantos batata?"))
sub_hamburguer=hamburguer*qtd_hamburguer
sub_refrigerante=refrigerant*qtd_refrigerante
sub_batata=batata*qtd_batata
subtotal=sub_hamburguer+sub_refrigerante+sub_batata
taxa=subtotal*0.10
total=subtotal+taxa
pessoas=int(input("Quantas pessoas vao dividir a conta?"))
valor=total/pessoas

print("subtotal:R$",subtotal)
print("taxa de serviços:R$",taxa)
print("total:R$",total)
print("lor por pessoas:R$",pessoas)
print("valor total:R$",valor)

