class veiculo:
  def __init__(self, marca, qtdRodas, modelo):
    self.marca = marca
    self.qtdRodas = qtdRodas
    self.modelo = modelo
    self.velocidade = 0
    
  def imprimirInformacoesVeiculo(self):
    print(self.__dict__)
  
  def acelerar(self, valor):
    if valor > 0:
      self.velocidade += valor
  
  def frear(self, valor):
    if valor > 0:
      self.velocidade -= valor
      if self.velocidade < 0:
        self.velocidade = 0


class automovel(veiculo):
  def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor):
    veiculo.__init__(self, marca, qtdRodas, modelo)
    self.potenciaDoMotor = potenciaDoMotor
  
  def imprimirInformacoesAutomovel(self):
    print('Automovel:')
    print(self.__dict__)

class bicicleta(veiculo):
  def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro):
    veiculo.__init__(self, marca, qtdRodas, modelo)
    self.numMarchas = numMarchas
    self.bagageiro = bagageiro
    
  def imprimirInformacoesBicicleta(self):
    print(' BICICLETA \n - Marca: {} \n - Qnt. Rodas: {}\n - Modelo: {}\n - Numero de marchas: {}\n - Bagageiro: {}'.format(self.marca, self.qtdRodas, self.modelo, self.numMarchas, self.bagageiro))

class moto(automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaMotor, partidaEletrica):
        automovel.__init__(self, marca, qtdRodas, modelo, potenciaMotor)
        self.partidaEletrica = partidaEletrica
    
    def imprimirInformacoesMoto(self):
        print(' MOTO \n - Marca: {} \n - Qnt. Rodas: {}\n - Modelo: {}\n - Potencia do motor: {}\n - Partida Eletrica: {}'.format(self.marca, self.qtdRodas, self.modelo, self.potenciaDoMotor, self.partidaEletrica))

class carro(automovel):
  def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas):
    automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor)
    self.qtdPortas = qtdPortas

  def imprimirInformacoesCarro(self):
    print(' CARRO \n - Marca: {} \n - Qnt. Rodas: {}\n - Modelo: {}\n - Potencia do motor: {}\n - Qnt Portas: {}'.format(self.marca, self.qtdRodas, self.modelo, self.potenciaDoMotor, self.qtdPortas))

#print(self.__dict__)