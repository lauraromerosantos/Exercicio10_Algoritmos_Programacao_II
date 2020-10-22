from veiculo import veiculo, automovel, bicicleta, moto, carro

carro = carro('Mercedes-Benz', 4, 'GLC SUV', 194, 4)
moto = moto('Harley Davidson', 2, 'CVO Limited', 95, True)
bicicleta = bicicleta('Tito Bikes', 2, 'BLITZ Avanti', 6, True)


opcao = "" 
while( opcao != "4" ):
    print("\n----------------------")
    print("1 - Carro")
    print("2 - Moto")
    print("3 - Bicicleta")
    print("4 - Sair")
    print("\n----------------------")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        carro.imprimirInformacoesCarro()
        print ('-'*20)
        break

    if opcao == "2":
        moto.imprimirInformacoesMoto()
        print ('-'*20)
        break

    if opcao == "3":
        bicicleta.imprimirInformacoesBicicleta()
        print ('-'*20)
        break