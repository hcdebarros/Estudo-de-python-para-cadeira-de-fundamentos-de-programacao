# Questão 01: Agrupamento de Livros por Gênero 
# • Contexto: Você possui uma lista de livros, onde cada livro é representado por um 
# dicionário contendo o título e o gênero. Você deseja organizar esses livros em um 
# dicionário onde as chaves são os gêneros e os valores são listas dos títulos dos 
# livros pertencentes a cada gênero. Adicione dez(10) livros com diferentes gêneros. 
# • Exemplo de Saída: 
# {'Fantasia': ['O Senhor dos Anéis', 'Harry Potter e a Pedra Filosofal'], 'Romance':
# ['Dom Casmurro', 'Orgulho e Preconceito'], 'Ficção Científica': ['1984']}

livros = [
    {"titulo": "Duna", "genero": "Ficção Científica"},
    {"titulo": "1984", "genero": "Ficção Científica"},
    {"titulo": "Neuromancer", "genero": "Ficção Científica"},
    {"titulo": "Orgulho e Preconceito", "genero": "Romance"},
    {"titulo": "Dom Casmurro", "genero": "Romance"},
    {"titulo": "O Morro dos Ventos Uivantes", "genero": "Romance"},
    {"titulo": "O Código Da Vinci", "genero": "Mistério"},
    {"titulo": "A Sombra do Vento", "genero": "Mistério"},
    {"titulo": "Harry Potter e a Pedra Filosofal", "genero": "Fantasia"},
    {"titulo": "O Hobbit", "genero": "Fantasia"},
] 


livros_separados = {}

for livro in livros:
    genero = livro["genero"] # nomeando o genero c o nome q tem em cada genero
    titulo = livro["titulo"] # msm coisa so q pro titulo

    if genero not in livros_separados:
        livros_separados[genero] = [] # se n tiver a lista criada do genero, ele cria
    
    livros_separados[genero].append(titulo) # na lista criada, na key genero ele adiciona o filme como value

print(livros_separados)
