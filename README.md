# Gerenciador de tarefas com Django

Esta aplicação foi desenvolvida seguindo o tutorial da Treina Web uma plataforma online de ensino de programação. Esta é uma simples aplicação web de um gerenciador de tarefas, ela foi desenvolvida com o pacote Django do Python.

## Tecnologias e ferramentas estudadas:

* Python
* Django
    * Django template
    * Django ORM
* Venv
* MySQL
* PyCharm
* Bootstrap
* Heroku

# Para executar este projeto em sua máquina:

* Crie um banco de dados: No seu banco de dados MySQL, crie um schema com o nome "gerenciador_tarefas", eu sugiro o uso do [Workbench](https://dev.mysql.com/downloads/workbench/) para acessar o banco diretamente.

* Execute os comandos a seguir

Clone o projeto
```bash
git clone https://github.com/mateus-oliveira/gerenciador-de-tarefas.git
cd gerenciador-de-tarefas/
```
Configure a VirtualEnv
```bash
mkdir ~/venv
pip install virtualenv
virtualenv ~/venv/gerenciador_tarefas
source ~/venv/gerenciador_tarefas/bin/activate
pip install -r requirements.txt
```

* No arquivo [settings.py](./gerenciador_tarefas/gerenciador_tarefas/settings.py) altere as credenciais para que o Django possa se conectar ao seu banco
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gerenciador_tarefas',
        'USER': '<YOUR_MYSQL_USERNAME>', # Eu usei o usuário 'root'
        'PASSWORD': '<YOUR_MYSQL_PASSWORD>',
        'HOST': '<HOSTNAME>', # Eu usei 'localhost'
        'PORT': '<PORT_MYSQL_NUMBER>', # Eu usei a porta padrão '3306'
    }
}
```

* Após isso, execute os comandos abaixo
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Depois disso, vá para a url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) e veja as rotas da aplicação.