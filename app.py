# Negocia em Python

print("\n******************* Python Negociação *******************")

def vlr_negociar(x, y):
	return x + y

print("\nSelecione o número da operação desejada: \n")
print("1 - Consultar Divida")
print("2 - Negociar  Divida")

neg = int(input("\nDigite sua opção (1/2): "))

if neg == 1:
	print ("Sua divida com a instituicao é 290,00")

elif neg == 2:

	print("\nVocê optou por negociar sua divida no valor de R$290,00 . Para negociação com entrada digite S ou N sem entrada: \n")
	
	# Valor da divida
	valor = int(290.00)

	#imput para validar se a negociação´será com ou sem entrada
	flg_entrada = str(input("S/N: "))

	if flg_entrada.upper() == 'S':
		
		#Imput do valor de entrada
		valor_ent = float(input("\nDigite o valor da entrada(formato 000.00): "))

	elif flg_entrada.upper() == 'N':

		valor_ent = 0.00

	else:
		
		print("\nOpção Invalida , será considerada a negociação sem entrada: \n")
		valor_ent = 0.00

	#Valida se o valor da entrada é maior que o valor da divida	
	if valor_ent > valor:
		print("Valor de Entrada informado é maior que o valor da Divida , desculpe a negociação nao será efetivada!")

	elif valor_ent < valor:
		
		print("\nPara o valor informado , você possui as seguintes opções: \n")

		# Valor negociado = Valor da divida menos o valor da entrada
		valor_neg = valor - valor_ent

		#Politicas de Desconto
		desc1 = 60 #A Vista
		desc2 = 40 # 2x
		desc3 = 35 # 3X
		desc4 = 30 # 4x

		#Valores calculados
		valor1 = str(round(float((valor_neg * desc1)/100),2))
		valor2 = str(round(float((valor_neg * desc2)/100),2))
		valor3 = str(round(float((valor_neg * desc3)/100),2))
		valor4 = str(round(float((valor_neg * desc4)/100),2))

		print("1 - Entrada de : " + str(valor_ent) + " + " + "1x de : " + valor1)
		print("2 - Entrada de : " + str(valor_ent) + " + " + "2x de : " + valor2)
		print("3 - Entrada de : " + str(valor_ent) + " + " + "3x de : " + valor3)
		print("4 - Entrada de : " + str(valor_ent) + " + " + "4x de : " + valor4)

		#Imput da oferta escolhida
		escolha = input("\nDigite sua opção (1/2/3/4): ")

		if escolha > '4' or escolha < '1':

			print("Opção invalida")

		elif escolha >= '1' or escolha <= '4':

			print("Você escolheu a opção " + escolha + " Digite C para confirmar ou S para Sair")
			
			valida = str(input("\nC/S: "))

			if valida.upper() == 'S':

				print("Sua Negociação não foi efetivada , caso necessario refaça a operação!")

			elif valida.upper() == 'C':	

				if escolha == '1':
					print("\n")
					print("Obrigado , sua negociação Entrada de " + str(valor_ent) + " + 1x de " + valor1 + " foi efetivada com sucesso!")
					print("Seu codigo de barras para pagamento é : 190002989283293829382938289")
					print("\n")

				elif escolha == '2':
					print("\n")
					print("Obrigado , sua negociação Entrada de " + str(valor_ent) + " + 2x de " + valor2 + " foi efetivada com sucesso!")
					print("Seu codigo de barras para pagamento é : 190002989283293829382938289")
					print("\n")

				elif escolha == '3':
					print("\n")
					print("Obrigado , sua negociação Entrada de " + str(valor_ent) + " + 3x de " + valor3 + " foi efetivada com sucesso!")
					print("Seu codigo de barras para pagamento é : 190002989283293829382938289")
					print("\n")

				elif escolha == '4':
					print("\n")
					print("Obrigado , sua negociação Entrada de " + str(valor_ent) + " + 4x de " + valor4 + " foi efetivada com sucesso!")
					print("Seu codigo de barras para pagamento é : 190002989283293829382938289")
					print("\n")
		else:
			print("\nOpção Inválida!")
else:
	print ("Opcao digitada é Inválida , por gentileza digite uma das opções informadas (1/2)")