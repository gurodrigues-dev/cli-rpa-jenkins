# CLI-RPA-Jenkins

- Com o objetivo de facilitar a vida de usuários de RPA. Construímos este CLI. Para que você rode seus jobs de forma remota, sem necessáriamente ir até o Jenkins, e apenas rodar um comando.

# Como utilizar

### Requisitos
- [ ] Python na máquina

- Caso você não tenha o Python, o arquivo pode ser executado em um `Google Collab` ou algo parecido. Peça mais informações aos desenvolvedores.

```
COMANDO     ACRÔNIMO        AÇÃO
-------    ----------     --------
--token        -t         Insira seu token fornecido pelo time de RPA.
--robot        -r         Insira o nome do robô.
--help         -h         Menu de ajuda.
```

**Exemplo:**
```
python3 src/cli.py -r Robô -t Token
```

Além na pasta raíz do diretório há um arquivo chamado `.env` nele você deve adicionar suas senhas e dados sensíveis. Tais como: `user_name` e `password`, etc.

- Observe o meu arquivo `.env`

```
user_name = gustavo
password = 1234
jenkins_url = JENKINS_URL/job/
api_key = API_KEY_USER_ADMIN_JENKINS
```

Você deve deixar suas credenciais idênticas a minha, no caso: user_name, password e o resto, mas claro, com valores diferentes.

# Como receber acesso

Solicite a equipe de RPA's para que registrem uma conta na sua área, assim vocês receberão uma key universal para que todos da sua equipe a utilizem.

# Segurança

> Existe algum perigo em utilizar o CLI?

- Na verdade sim, se você rodar muitas vezes o processo ao mesmo tempo, é bem provável que o Jenkins não rode tudo ao mesmo tempo, e você trave o processo de outros usuários. Isso não é nada legal :/. Saiba, que os administradores do Jenkins, conseguem ver quem ativou e qual robô está sendo executado várias vezes, portanto tome cuidado.

> Quero utilizar, vou poder utilizar todos os robôs do Jenkins?

- Não! Os robôs são dividos por usuários de acordo com o permissionamento de cada conta. Então você provavelmente não vai conseguir rodar o robô de outro usuário.

# Recomendações aos Admins

- Se atentem com as seguranças de cada job, e ativem o build remoto e dos mesmos, para melhor uso permissionem a segurança dos users via job, assim facilitando seu gerenciamento.
