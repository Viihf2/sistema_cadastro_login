import sqlite3
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Cria a conexão com o banco de dados
conn = sqlite3.connect('cadastro.db')

# Cria o cursor para executar as consultas SQL
cursor = conn.cursor()

def exibir_usuarios():
    # Obtém os dados dos usuários do banco de dados
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    # Limpa a lista de labels
    for label in labels:
        label.destroy()
    labels.clear()

    # Exibe os dados dos usuários como labels
    for i, usuario in enumerate(usuarios):
        for j in range(4):
            label = customtkinter.CTkLabel(janela, text=usuario[j])
            label.grid(row=i+2, column=j, padx=10, pady=5)
            labels.append(label)

janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text="Usuários")
texto.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Cria uma lista para armazenar as labels dos usuários
labels = []

# Cria os cabeçalhos da tabela
cabecalhos = ["Nome", "Data de Nascimento", "Email", "Senha"]
for i, cabecalho in enumerate(cabecalhos):
    cabecalho_label = customtkinter.CTkLabel(janela, text=cabecalho)
    cabecalho_label.grid(row=2, column=i, padx=10, pady=5)
    labels.append(cabecalho_label)

# Chama a função para exibir os usuários cadastrados
exibir_usuarios()

janela.mainloop()

# Fecha a conexão com o banco de dados ao finalizar o programa
conn.close()
