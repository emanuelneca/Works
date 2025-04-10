# Work
Controle de Estoque com PySimpleGUI + SQLite

Este é um projeto simples de controle de estoque com interface gráfica usando PySimpleGUI e banco de dados SQLite. Ele permite realizar um CRUD completo de produtos, com funcionalidades extras como alerta de baixo estoque.

Funcionalidades:

Cadastrar Produto: Nome, categoria, quantidade e preço.

Visualizar Estoque: Lista todos os produtos cadastrados.

Vender Produto: Atualiza automaticamente o estoque.

Alerta de Baixo Estoque: Exibe produtos com quantidade inferior a 5 unidades.

Interface Gráfica: Simples e intuitiva com PySimpleGUI.

Banco de Dados Local: Utiliza SQLite (estoque.db).

Como rodar o projeto:

1- clonar o repositorio:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2 - Se der erro no (sg.theme), precisará reinstalar o PySimpleGUI dessa forma para a visualização do tema.

python -m pip uninstall PySimpleGUI
python -m pip cache purge
python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI

3- Execute o script:

python controle_estoque.py
