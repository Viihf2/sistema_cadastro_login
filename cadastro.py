import sqlite3
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Cria a conexão com o banco de dados
conn = sqlite3.connect('cadastro.db')

# Cria o cursor para executar as consultas SQL
cursor = conn.cursor()

def cadastrar():
    nome_valor = nome.get().strip()
    nascimento_valor = nascimento.get().strip()
    email_valor = email.get().strip()
    senha_valor = senha.get().strip()

    # Insere os dados na tabela 'usuarios'
    cursor.execute("INSERT INTO usuarios (nome, nascimento, email, senha) VALUES (?, ?, ?, ?)",
                   (nome_valor, nascimento_valor, email_valor, senha_valor))

    # Comita as alterações no banco de dados
    conn.commit()

    print("Cadastro realizado com sucesso!")
    abrir_janela_login()

def abrir_janela_login():
    import login

janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text="Fazer Cadastro")
texto.pack(padx=10, pady=10)

nome = customtkinter.CTkEntry(janela, placeholder_text="Digite seu nome")
nome.pack(padx=5, pady=5)

nascimento = customtkinter.CTkEntry(janela, placeholder_text="Digite sua data de nascimento")
nascimento.pack(padx=5, pady=5)

email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")
email.pack(padx=5, pady=5)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack(padx=5, pady=5)

botao = customtkinter.CTkButton(janela, text="Cadastrar", command=cadastrar)
botao.pack(padx=10, pady=10)

janela.mainloop()

# Fecha a conexão com o banco de dados ao finalizar o programa
conn.close()
