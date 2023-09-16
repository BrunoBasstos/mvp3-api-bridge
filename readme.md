# Bridge API
![todo-app-diagrama](https://github.com/BrunoBasstos/mvp3-api-bridge/assets/5402439/057ce1a2-e228-4f45-9d82-64f5a07ceb5b)

Este é um MVP para conclusão da terceira sprint do curso de pós graduação em engenharia de software pela PUC-Rio.

A Bridge API é uma aplicação Flask que intermedia a comunidação com a [OpenWeather API](http://openweathermap.org) para
obtenção de nomes de cidades e de previsão do tempo.

Além disso, este projeto é composto por uma aplicação React que consome a API para fornecer uma interface amigável ao
usuário e uma outra api que permite o gerenciamento de tarefas a serem realizadas, incluindo a adição, edição e
remoção de usuários, tarefas e prioridades.

Os repositórios das aplicações podem ser encontrados em:

- [ToDo-App](https://github.com/BrunoBasstos/mvp3-app-todo).
- [ToDo-Api](https://github.com/BrunoBasstos/mvp3-api-todo)

## Configurações .env

- FLASK_ENV: Ambiente de execução do Flask.
- FLASK_APP: Arquivo principal da aplicação Flask.
- FLASK_RUN_PORT: Porta em que a aplicação Flask será executada (padrão: 5001).
- WEATHER_API_KEY: Chave de acesso à OpenWeather API.
- WEATHER_API_URL: URL base da OpenWeather API (padrão: http://api.openweathermap.org/data/2.5).
- WEATHER_API_UNITS: Unidade de medida utilizada pela OpenWeather API (padrão: metric).
- WEATHER_API_LANG: Idioma utilizado pela OpenWeather API (padrão: pt_br).
- WEATHER_API_TIMEZONE: Fuso horário utilizado pela OpenWeather API (padrão: "+03:00").
- WEATHER_FORECAST_DAYS_COUNT: Quantidade de dias da previsão do tempo (padrão: 24 que corresponde a 3 dias).
- GEOCODE_API_URL: URL base da Geocode API (padrão: http://api.openweathermap.org/geo/1.0).
- GEOCODE_API_DEFAULT_LIMIT: Limite padrão de resultados da Geocode API (padrão: 5).

## OpenWeather API

- Para utilizar essa API é necessário criar uma conta no site [OpenWeather API](http://openweathermap.org), gerar uma
  chave de acesso e adicioná-la ao arquivo .env.
- A documentação da API pode ser encontrada em [https://openweathermap.org/api](https://openweathermap.org/api).

## Rotas implementadas

- `GET /location/search/<string:query>`: Retorna uma lista de cidades que correspondem à query.
    - Exemplo: `GET /location/search/rio de janeiro` retorna uma lista de cidades com o nome "Rio de Janeiro".
    - Esta rota encaminhará requisições para o endpoint http://api.openweathermap.org/geo/1.0/direct?q={city_name}
    - Veja [aqui a documentação](https://openweathermap.org/api/geocoding-api#direct) deste endpoint no site da
      OpenWeather para mais detalhes
    - Esta rota não busca cidades pelo nome parcial, apenas pelo nome completo.
- `GET /weather/<string:city>`: Retorna a previsão do tempo de um dia para uma cidade específica.
    - Exemplo: `GET /weather/rio de janeiro` retorna a previsão do tempo para a cidade do Rio de Janeiro na data atual.
    - Esta rota encaminhará requisições para o endpoint http://api.openweathermap.org/data/2.5/weather?q={city_name}
    - Veja [aqui a documentação](https://openweathermap.org/current#one) deste endpoint no site da OpenWeather para mais
      detalhes
- `GET /forecast/<string:city>`: Retorna a previsão do tempo para uma cidade específica para os próximos 3 dias.
    - Exemplo: `GET /forecast/rio de janeiro` retorna a previsão do tempo para a cidade do Rio de Janeiro para os
      próximos 3 dias.
    - Esta rota encaminhará requisições para o endpoint http://api.openweathermap.org/data/2.5/forecast?q={city_name}
    - Veja [aqui a documentação](https://openweathermap.org/forecast5) deste endpoint no site da OpenWeather para mais
      detalhes
    - A quantidade de dias dessa previsão pode ser alterada no arquivo .env através da
      variável `WEATHER_FORECAST_DAYS_COUNT`. A OpenWeather retorna previsões para até 5 dias e de 3 em 3 horas. A
      Bridge API vai filtrar os resultados e exibir apenas uma previsão por dia, de modo que, para exibir a previsão de
      3 dias, o valor da variável deve ser setado para 24 (3 dias * 8 previsões por dia).

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
