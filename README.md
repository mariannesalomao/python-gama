# Projeto CRUD de Modelo de Carros

> Comando para atualizar pip: python -m pip install --upgrade pip

> Comandos do Jenkins desktop:
Start the Jenkins service: brew services start jenkins-lts
Restart the Jenkins service: brew services restart jenkins-lts
Update the Jenkins version: brew upgrade jenkins-lts



# Comandos

python3 -m pip install virtualenv
python3 -m venv ambiente_virtual

> Comando pra criar uma vm pro projeto ficar só aqui e não de forma global no PC 
    python -m venv ambiente_virtual 
    python3 -m venv ambiente_virtual
    
> Comando para ativar a VM. Toda vez que vcs desligarem a máquina, deve repetir esse comando. VÁ ATÉ A PASTA QUE TÁ O PROJETO
    
    # Em windows
    
    Entra na pasta do ambiente virtual
    
    ambiente_virtual\Scripts\activate    
    ambiente_virtual\Scripts\activate.bat
    
    # Unix ou MacOS
    
    source ambiente_virtual/bin/activate
    
> Instalar DJango no ambiente virtual

    python -m pip install Django
    
> Iniciar uma aplicação devidamente usando Python: O ponto é para não criar outra pasta dentro de project

    django-admin startproject project .
    
> Iniciar a aplicação com o nome de app

    python manage.py startapp app


# VAI ATÉ A AQUI AS CONFIGURAÇÕES INICIAIS. FAÇA O PULL REQUEST AQUI
    
> Crie um repositório no GITHUB

> Suba as alterações iniciais remotamente:

    git remote add origin https://github.com/mariannesalomao/crud_python.git
    git branch -M main
    git add .
    git commit -m 'mensagem'
    git push -u origin main
    
# Codando

> Vc deve colocar 'app' no arquivo settings.py dentro de project pro python entender que app faz parte do projeto

> Modifique os arquivos urls e views

> Rode o server: (Tem que ser no terminal q logou a VM)

    python3 manage.py runserver
    
### Começando o LAYOUT da aplicação

> Crie a pasta TEMPLATE dentro de APP

> Crie o index.html dentro de template

> Modifique o arquivo views.py

> Copie e cole o CDN do bootstrap dentro de index.html

> Pesquise table bootstrap no google

> Mudei a classe padrão thead-dark pra table-dark

#### Como podem ver tudo começa com a rota, chama a função e depois ela renderiza a view que vc quer

> Crie o form e importe ele

> Comece agr nas models

> procurar no google models django

> mostrar o seguinte link:

    https://docs.djangoproject.com/en/3.2/topics/db/models/#field-types

> Rode as migrations

    python manage.py makemigrations
    
> Vá na pasta migrations e mostre

> Depois crie as tabelas no banco de dados:

    python manage.py migrate
    
> Automaticamente vai no sqlite3. vá na pasta settings e mostre o atributo ENGINE

> Abra o db browser e conecte com banco de dados da app. Colocando o arquivo db.sqlite3

> Agora crie as models. Link https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/

> Vá nas views e import essa model

> Crie um dicionario chamado data

> form.as_p gera em nome de parágrafo o render da pagina

> No redirect de views, coloque o nome da rota



> Instalando jenkins

    brew install jenkins-lts
    
    brew services start jenkins-lts
    
> configurando:

    sudo nano /usr/local/opt/jenkins-lts/homebrew.mxcl.jenkins-lts.plist
    
> ! Mude a linha onde tem o host por 0.0.0.0, como abaixo:

    <string>--httpListenAddress=0.0.0.0</string>

> Pegar senha do Jenkins no macos:

    sudo cat /Users/mariannesalomaodeoliveira/.jenkins/secrets/initialAdminPassword




> Finalmente Deus! Criando imagem da aplicação: Esse problema é porque você não criou uma tag para a imagem, essa tag deve ter seu
usuario_docker_hub/nome_da_imagem, ou se preferir, quando realizar o build já crie a imagem que esse padrão de nome.

    docker build -t django-kubernetes .
    
> Dá treta se não tagear a imagem, então tagueie:

    docker tag django-kubernetes mariannesalomao/django-kubernetes:django-kubernetes
    
    
> Depois dê docker run


# KUBERNETES

> Crie o arquivo deployment.yaml

> Rode o comando:

    minikube start

    kubectl apply -f deployment.yaml
    
    minikube dashboard.   (vai dar erro, pq o minikube não tem a sua imagem do seu projeto, ai rode o comando abaixo:)
    
    docker save django-kubernetes | (eval $(minikube docker-env) && docker load)


