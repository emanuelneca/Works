import sqlite3
import PySimpleGUI as sg

def listar_produtos():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def janela_visualizacao():
    sg.theme('LightGrey1')

    layout = [
        [sg.Text('📦 Produtos no Estoque:', font=('Arial', 14))],
        [sg.Multiline(size=(80, 20), key='-OUTPUT-', font=('Courier', 10))],
        [sg.Button('Atualizar'), sg.Button('Fechar')]
    ]

    return sg.Window('Visualizador de Estoque', layout, finalize=True)

def main():
    window = janela_visualizacao()

    def atualizar_output():
        produtos = listar_produtos()
        texto = ''
        for p in produtos:
            texto += f"ID: {p[0]} | Nome: {p[1]} | Cat: {p[2]} | Qtde: {p[3]} | Preço: R${p[4]:.2f}\n"
        window['-OUTPUT-'].update(texto)

    atualizar_output()

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, 'Fechar'):
            break
        elif event == 'Atualizar':
            atualizar_output()

    window.close()

if __name__ == '__main__':
    main()
