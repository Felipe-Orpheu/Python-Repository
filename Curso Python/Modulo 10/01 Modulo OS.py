import os

#Verificar o sistema operacional - "nt = Windows", "posix = Linux", "Java = Mac"
#print(os.name)

#Verificar se o arquivo existe:
"""print(os.path.exists('texto.py'))
print(os.path.exists('teste.py'))"""

#Verificar se um diretorio existe
"""print(os.path.exists('python'))
print(os.path.exists('pastanova'))"""

#Exemplo de caminhos: 
"""print(os.path.exists('pastanova/texto.py'))"""

#Criando arquivos: 
"""os.mknod('olamundo.py')"""

#Criando um diretorio: 
"""os.mkdir('python')"""

#Apagando Arquivos
"""os.remove('teste.txt')
print(os.path.exists('teste.txt'))"""

#Apagando Diretorios
"""os.remove('python') - Função exclusiva para aquivos
os.rmdir('python') - Não conseguimos remover diretorios que possuem aquivos"""

#Renomeando Aquivos e Diretorios
"""os.rename("olamundo.py", "olamundo.txt") - renomear somente arquivos
os.rename("./diretorio/teste.txt", "./documentos/compras.txt") - renomear aquivos e diretorios
"""