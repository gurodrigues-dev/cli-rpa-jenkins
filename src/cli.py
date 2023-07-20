import requests
import argparse
import variables
import time
from requests.auth import HTTPBasicAuth

class JenkinsCLI():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="CLI Jenkins")
        self.argumentos = [
            {'key': '-t', 'nome':'--token', 'tipo':str, 'help':'Insira seu token fornecido pelo Squad RPA', 'variable':'token'},
            {'key': '-r', 'nome':'--robot', 'tipo':str, 'help':'Insira o nome do robô', 'variable':'robot'}
        ]
    
    def adiciona_argumentos(self):
        for argumento in self.argumentos:
            self.parser.add_argument(argumento['key'], argumento['nome'], type=argumento['tipo'], help=argumento['help'])

    def executar(self):

        args = self.parser.parse_args()

        token = args.token
        robot = args.robot

        if token and robot:

            self.get_remote_build_job(robot, token)

        elif token and not robot:

            print("\nÉ necessário passar o nome do robô para que o mesmo seja executado\n")
            exit()
            
        elif robot and not token:

            print("\nVocê inseriu apenas o robô, é necessário também sua key, fornecida pelo time de RPA\n")
            exit()

        else:

            print("\nParece que você não inseriu nenhum argumento válido, por gentileza rode o código novamente com '-h' ou '--help' para verificar as opções disponíveis.\n")
            exit()

    def get_remote_build_job(self, nome_robot, token, jenkins_url=variables.JENKINSURL):
        url = jenkins_url + nome_robot + "/build?token=" + token

        try:
            ctx = requests.get(url, auth=(variables.USERNAME, variables.PASSWORD))

            if ctx.status_code == 201:

                url_job = variables.JENKINSURL + nome_robot + "/lastBuild/api/json"

                response = requests.get(url_job, auth=HTTPBasicAuth(variables.USERNAME, variables.APIKEY))

                res = response.json()['result']

                print("Robô rodando...")

                time.sleep(1)

                while res == None:
                    response = requests.get(url_job, auth=HTTPBasicAuth(variables.USERNAME, variables.APIKEY))

                    res = response.json()['result']

                if res == "SUCCESS":
                    print("O robô rodou com sucesso!")

                else:
                    print("Robô sofreu erro! ", res)

            else:

                print("Conexão incompleta, algo aconteceu. Sinto muito. :/")

        except requests.ConnectTimeout:

            list_msg = [
                "Parece que você não está conectado na VPN",
                "Verifique se seu token ou se o nome do robô está correto",
                "Ou então talvez os usuários inseridos no arquivo '.env' estão incorretos",
                "Caso todas opções estejam corretas, pode ser algum problema de permissionamento ou conta inexistente no jenkins, se você tem uma conta no Jenkins, provavelmente o Jenkins caiu, entre em contato com o time de RPA"
            ]

            print("\nParece que houve algum problema ao tentar se conectar com o Jenkins. Sinto muito. :/")

            for idx, msg in enumerate(list_msg):
                print(f'\n{idx + 1}. {msg}\n')

            exit()

        except Exception as err:
            print(err)

def main():

    cli = JenkinsCLI()

    cli.adiciona_argumentos()

    cli.executar()

if __name__ == '__main__':
    main()
