# consulta_cep_django
API criada usando Django e Django REST Framework para consultar e registrar endereços consumindo [API externa de consulta de CEP](https://viacep.com.br/).

## Execução do projeto
Para executar o projeto, é instalar o [Pipenv](https://pipenv.pypa.io/en/latest/), para gerenciamento de pacotes e criação de ambientes virtuais, e o [pyenv](https://github.com/pyenv/pyenv), requisito do Pipev para gerenciamento das versões do Python nos ambientes.

Feito isso, rode os seguintes comandos para criar o ambiente do repositório e instalar os requisitos necessários:
```
pipenv shell
pipenv install
```
Em seguida, rode o seguinte comando:
```
python manage.py migrate
```
Por fim, execute o projeto com o comando abaixo:
```
python manage.py runserver
```
Por padrão, o projeto rodará no endereço http://localhost:8000/.
## Endpoints e payloads
Utilizando o endereço citado anteriormente, você pode acessar os seguintes endponts:
| Endpoint        | Método | Body payload                     | Funcionalidade               |   |
|-----------------|--------|----------------------------------|------------------------------|---|
| `/endereco`       | GET    | -                                | Listar endereços registrados |   |
| `/endereco`       | POST   | `{"cep": "11111111"}` | Registrar endereço           |   |
| `/endereco/<cep>` | GET    | -                                | Detalhar endereço registrado |   |
