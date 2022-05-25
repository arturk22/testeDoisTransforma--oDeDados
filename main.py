from sys import displayhook
import zipfile
import tabula
import requests


def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code== requests.codes.OK:    
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Donwload Finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

if __name__ == "__main__":
    baixar_arquivo('https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf', 'Anexo 1.pdf')

