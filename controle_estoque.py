import sqlite3
import PySimpleGUI as sg

# === BANCO DE DADOS ===

def conectar():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT,
            quantidade INTEGER,
            preco REAL
        )
    ''')
    conn.commit()
    return conn

def inserir_produto(nome, categoria, quantidade, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, categoria, quantidade, preco) VALUES (?, ?, ?, ?)',
                   (nome, categoria, quantidade, preco))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def vender_produto(produto_id, quantidade_vendida):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT quantidade FROM produtos WHERE id = ?', (produto_id,))
    resultado = cursor.fetchone()
    if resultado:
        estoque_atual = resultado[0]
        novo_estoque = estoque_atual - quantidade_vendida
        cursor.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (novo_estoque, produto_id))
        conn.commit()
    conn.close()

def produtos_baixo_estoque(limite=5):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos WHERE quantidade < ?', (limite,))
    produtos = cursor.fetchall()
    conn.close()
    return produtos

# === INTERFACE ===

def janela_principal():
    sg.theme('LightBlue')

    layout = [
        [sg.Text('Nome'), sg.Input(key='-NOME-')],
        [sg.Text('Categoria'), sg.Input(key='-CATEGORIA-')],
        [sg.Text('Quantidade'), sg.Input(key='-QUANTIDADE-')],
        [sg.Text('Preço'), sg.Input(key='-PRECO-')],
        [sg.Button('Cadastrar Produto'), sg.Button('Vender Produto')],
        [sg.Button('Ver Estoque'), sg.Button('Produtos com Baixo Estoque')],
        [sg.Output(size=(80, 20))],
    ]

    return sg.Window('Controle de Estoque', layout)

def iniciar_interface():
    window = janela_principal()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == 'Cadastrar Produto':
            try:
                inserir_produto(
                    values['-NOME-'],
                    values['-CATEGORIA-'],
                    int(values['-QUANTIDADE-']),
                    float(values['-PRECO-'])
                )
                print('✅ Produto cadastrado com sucesso!')
            except Exception as e:
                print(f'Erro ao cadastrar produto: {e}')

        elif event == 'Ver Estoque':
            produtos = listar_produtos()
            print('\n📦 ESTOQUE ATUAL:')
            for p in produtos:
                print(f"ID: {p[0]} | Nome: {p[1]} | Cat: {p[2]} | Qtde: {p[3]} | Preço: R${p[4]:.2f}")

        elif event == 'Vender Produto':
            try:
                produto_id = int(sg.popup_get_text('Digite o ID do produto:'))
                qtde = int(sg.popup_get_text('Quantidade vendida:'))
                vender_produto(produto_id, qtde)
                print(f'🛒 Venda registrada. Produto ID {produto_id} atualizado.')
            except Exception as e:
                print(f'Erro na venda: {e}')

        elif event == 'Produtos com Baixo Estoque':
            produtos = produtos_baixo_estoque()
            print('\n⚠️ PRODUTOS COM BAIXO ESTOQUE:')
            for p in produtos:
                print(f"ID: {p[0]} | Nome: {p[1]} | Qtde: {p[3]}")

    window.close()

# === EXECUÇÃO ===

if __name__ == '__main__':
    iniciar_interface()

