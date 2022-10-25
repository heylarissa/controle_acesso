import os
import stat

# Verifica se o arquivo existe
if os.path.isfile("exemplo.txt"):
    # Modifica a permissão do arquivo para leitura, escrita e execução
    os.chmod("exemplo.txt", stat.S_IRWXU)

# Abre o arquivo para escrita
arquivo = open("exemplo.txt", 'w')
# Escreve no arquivo
arquivo.write("Escrevendo Arquivo!")
# Fecha o arquivo
arquivo.close()

# Modifica o arquivo apenas para leitura
os.chmod("exemplo.txt", stat.S_IRUSR)