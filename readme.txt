    
Como executar a solução:

    Instale as dependências do angular
    instale as dependências do python ( caso souber usar pipenv será mais facil) que estão listados no arquivo pipfile
    Rode a aplicação Flask, indo pelo terminal até a pasta do arquivo main.py e utilizando os comandos em um terminal windows:
        SET FLASK_APP=main.py
        flask run
    em outro terminal vá a pasta do angular e execute ng serve.


Descrição da solução:

	No backend, foi utilizado um servidor flask na linguagem python para adaptar a API fornecida, e para conseguir salvar novos usuários, se tornando uma NOVA API REST.

	O backend conta com getusers, getuser, adduser e updateuser.

	No frontend, foi utilizado o bootstrap do twitter para responsividade do site, e angular para consumir a API REST. Também é possível vizualizar os dados com paginação, e podendo alterar o tamanho da página. Mas não é possível editar os dados.
