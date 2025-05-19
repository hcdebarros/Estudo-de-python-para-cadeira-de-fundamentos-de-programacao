# Questão 02: Combinando Informações de Duas Listas em um Dicionário
# • Contexto: Você possui duas listas: uma com nomes de produtos e outra com
# seus respectivos preços na mesma ordem. Você deseja combinar essas
# informações em um dicionário onde os nomes dos produtos sejam as chaves e os
# preços sejam os valores. Adicione 20 produtos e 20 preços
# • Exemplo de Saída: {'Teclado': 75.0, 'Mouse': 30.5, 'Monitor': 350.0, 'Fone de
# Ouvido': 90.0}


produtos = [
    'Placa Mãe', 'Processador', 'Placa de Vídeo', 'Memória RAM', 'NVME-M2', 'Fonte',
    'HD 1TB', 'SSD 512GB', 'Gabinete Gamer', 'Cooler', 'Teclado Mecânico',
    'Mouse Gamer', 'Monitor 24"', 'Headset', 'Webcam Full HD', 'Cadeira Gamer',
    'Estabilizador', 'Notebook', 'Roteador Wi-Fi 6', 'Impressora'
]
precos = [
    750, 1300, 4500, 600, 600, 500,
    350, 550, 400, 150, 250,
    200, 1200, 300, 250, 1200,
    450, 3500, 600, 700
]

dicionario = {}

for i in range(20):
    chave= produtos[i]
    valor = precos[i]
    dicionario[chave] = valor

print(dicionario)

