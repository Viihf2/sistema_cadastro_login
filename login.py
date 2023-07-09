# import tkinter
#
# janela = tkinter.Tk()
# janela.geometry("500x300")
#
# def clique():
#     print("Fazer Login")
#
# texto = tkinter.Label(text="Fazer login")
# texto.pack(padx=10, pady=10)
#
# botao = tkinter.Button(janela, text="Login", command=clique)
# botao.pack(padx=10, pady=10)
#
#
#
# janela.mainloop()
import sqlite3
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Cria a conexão com o banco de dados
conn = sqlite3.connect('cadastro.db')

# Cria o cursor para executar as consultas SQL
cursor = conn.cursor()

def login():
    email_valor = email.get().strip()
    senha_valor = senha.get().strip()

    # Consulta o banco de dados para verificar o login
    cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email_valor, senha_valor))
    usuario = cursor.fetchone()

    if usuario:
        print("Login bem-sucedido!")
        abrir_janela_usuarios()
    else:
        print("Email ou senha incorretos!")

def abrir_janela_usuarios():
    import usuarios

janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar login")
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=login)
botao.pack(padx=10, pady=10)

janela.mainloop()

# Fecha a conexão com o banco de dados ao finalizar o programa
conn.close()
