# Bridge API

Este é um MVP para conclusão da terceira sprint do curso de pós graduação em engenharia de software pela PUC-Rio.

A Bridge API é uma aplicação Flask que intermedia a comunidação com a [OpenWeather API](http://openweathermap.org) para
obtenção de nomes de cidades e de previsão do tempo.

Além disso, este projeto é composto por uma aplicação React que consome a API para fornecer uma interface amigável ao
usuário e uma outra api que permite o gerenciamento de tarefas a serem realizadas, incluindo a adição, edição e
remoção de usuários, tarefas e prioridades.

Os repositórios das aplicações podem ser encontrados em:

- [ToDo-App](https://github.com/BrunoBasstos/mvp3-app-todo).
- [ToDo-Api](https://github.com/BrunoBasstos/mvp3-api-todo)

## Rotas implementadas

- `GET /location/search/<string:query>`: Retorna uma lista de cidades que correspondem à query.
- `GET /weather/<string:city>`: Retorna a previsão do tempo de um dia para uma cidade específica.
- `GET /forecast/<string:city>`: Retorna a previsão do tempo para uma cidade específica para os próximos 3 dias.

## Tecnologias utilizadas

- Flask
- Flask RestX
- Flask CORS
- Docker

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.6 ou superior: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- pip (geralmente já incluído com
  Python): [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)
- Docker (caso deseje executar o projeto usando
  Docker): [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

## Como executar

1. Clone o repositório.
2. Crie o arquivo .env usando o arquivo .env.example como base e configure seu ambiente. Recomendamos manter a aplicação
   rodando na porta 5001.
3. Crie e ative um ambiente virtual Python 3.
    1. No Windows, utilize o comando `python -m venv venv` para criar o ambiente virtual e `venv\Scripts\activate` para
       ativá-lo.
    2. No Linux, utilize o comando `python3 -m venv venv` para criar o ambiente virtual e `source venv/bin/activate`
       para ativá-lo.
4. Instale as dependências do projeto com o comando `pip install -r requirements.txt`.
5. Inicie a aplicação com o comando `python app.py`.
6. Acesse a documentação da API em `http://localhost:5001`.

## Como executar com Docker

1. Clone o repositório.
2. Crie o arquivo .env usando o arquivo .env.example como base e configure seu ambiente. Recomendamos manter a aplicação
   rodando na porta 5001.
3. Abrir o terminal na pasta do projeto.
4. Executar o comando `docker build -t bridge-api .`.
5. Executar o comando `docker run --name bridge-api -p 5001:5001 bridge-api`.
    1. Note que isto criará um container com o nome bridge-api. Para reiniciar a aplicação nas próximas vezes, basta
       executar o comando `docker start bridge-api`. Caso você queira remover o container,
       execute `docker rm -f bridge-api`.

## Testes

Para executar os testes, basta executar o comando `pytest` na pasta raiz do projeto.

## Contribuições

Contribuições são sempre bem-vindas! Se você deseja contribuir com este projeto, por favor, abra uma issue para discutir
sua ideia antes de submeter um pull request.

## Licença

Este projeto está licenciado sob a licença MIT.

## TODO

- [ ] Aumentar cobertura de testes
