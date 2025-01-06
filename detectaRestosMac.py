import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox


def buscar_arquivos():
    pasta_selecionada = filedialog.askdirectory()
    if not pasta_selecionada:
        return

    lista_arquivos.delete(0, tk.END)  # Limpar a lista antes de buscar novos arquivos
    arquivos_encontrados.clear()

    for root, _, files in os.walk(pasta_selecionada):
        for file in files:
            if file.startswith('._'):
                caminho_completo = os.path.join(root, file)
                arquivos_encontrados.append(caminho_completo)
                lista_arquivos.insert(tk.END, caminho_completo)

    atualizar_resumo()

    if not arquivos_encontrados:
        messagebox.showinfo("Resultado", "Nenhum arquivo encontrado com prefixo ._.")


def excluir_arquivos_selecionados():
    arquivos_selecionados = lista_arquivos.curselection()
    if not arquivos_selecionados:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado para exclusão.")
        return

    for indice in reversed(arquivos_selecionados):  # Reverso para evitar problemas de exclusão em loop
        arquivo = arquivos_encontrados[indice]
        try:
            os.remove(arquivo)
            lista_arquivos.delete(indice)
            arquivos_encontrados.pop(indice)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir o arquivo {arquivo}: {str(e)}")

    atualizar_resumo()
    messagebox.showinfo("Sucesso", "Os arquivos selecionados foram excluídos com sucesso.")


def excluir_todos():
    if not arquivos_encontrados:
        messagebox.showwarning("Aviso", "Nenhum arquivo encontrado para exclusão.")
        return

    for arquivo in arquivos_encontrados:
        try:
            os.remove(arquivo)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir o arquivo {arquivo}: {str(e)}")
    arquivos_encontrados.clear()
    lista_arquivos.delete(0, tk.END)

    atualizar_resumo()
    messagebox.showinfo("Sucesso", "Todos os arquivos foram excluídos com sucesso.")


def atualizar_resumo():
    """Atualiza o rótulo com o número de arquivos encontrados."""
    total = len(arquivos_encontrados)
    resumo_var.set(f"Arquivos encontrados: {total}")


# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Excluir Arquivos com Prefixo ._")

# Lista para armazenar os arquivos encontrados
arquivos_encontrados = []

# Variável para o resumo
resumo_var = tk.StringVar(value="Arquivos encontrados: 0")  # Inicializa o resumo com 0

# Botões e widgets
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_buscar = tk.Button(frame_botoes, text="Selecionar Pasta", command=buscar_arquivos)
btn_buscar.grid(row=0, column=0, padx=5)

btn_excluir_selecionados = tk.Button(frame_botoes, text="Excluir Selecionados", command=excluir_arquivos_selecionados)
btn_excluir_selecionados.grid(row=0, column=1, padx=5)

btn_excluir_todos = tk.Button(frame_botoes, text="Excluir Todos", command=excluir_todos)
btn_excluir_todos.grid(row=0, column=2, padx=5)

# Resumo do número de arquivos encontrados
resumo_label = tk.Label(janela, textvariable=resumo_var, font=("Arial", 12), fg="blue")
resumo_label.pack(pady=5)

# Lista de arquivos encontrados
lista_arquivos = Listbox(janela, width=80, height=20, selectmode=tk.MULTIPLE)
lista_arquivos.pack(padx=10, pady=10)

# Executar a interface gráfica
janela.mainloop()
