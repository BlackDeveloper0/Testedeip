#teste de ip
#importando bibliotecas 
import requests
import os
import subprocess

#Logica para testar o IP
def ping_ip(ip):
    try:
        resultado = subprocess.run(["ping", "-n", "3", ip], capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return f"Erro ao executar o ping: {e}"

#Logica para baixar a imagem no diretoio downloads não importando quem é o usuario 
def baixar_imagem():
    url_imagem = "https://hermes.dio.me/articles/cover/aea951a1-825b-43bb-94fc-76b3b744418c.png"
    response = requests.get(url_imagem)
    caminho_imagem = os.path.join(os.path.expanduser("~" + os.sep + "Downloads"), "imagem.png")
    with open(caminho_imagem, "wb") as file:
        file.write(response.content)
    print(f"Imagem salva em '{caminho_imagem}'")

# Lista de IPs
ips_testados = {}

# Lista de opções 
opcoes_menu = {
    '1': baixar_imagem,
    '2': lambda: ping_ip(input("Digite o IP para testar: ")),
    '3': lambda: print("Lista de IPs testados e resultados:", ips_testados),
    '4': exit
}

# menu 
while True:
    print("Menu:")
    print("1. Baixar imagem")
    print("2. Testar IP")
    print("3. Lista de IPs testados")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha in opcoes_menu:
        if escolha == '2':
            ip = input("Digite o IP para testar: ")
            resultado_ping = ping_ip(ip)
            ips_testados[ip] = resultado_ping  # Armazena o resultado na lista 
            print(resultado_ping)
        else:
            opcoes_menu[escolha]() 
    else:
        print("A opção não é válida, tente outra opção.")
