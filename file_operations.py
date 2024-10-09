import os
import win32com.client
import win32api
import datetime
from tkinter import filedialog  # Importar filedialog aqui
import tkinter as tk  # Importar tkinter para uso nas funções

def select_files(file_list):
    files = filedialog.askopenfilenames(title="Selecione os arquivos para imprimir", filetypes=[
        ("PDF files", "*.pdf"),
        ("Word documents", "*.docx"),
        ("Text files", "*.txt"),
        ("All files", "*.*")
    ])
    file_list.delete(0, tk.END)
    for file in files:
        if file not in file_list.get(0, tk.END):  # Evita duplicatas
            file_list.insert(tk.END, file)

def clear_list(file_list):
    file_list.delete(0, tk.END)

def print_files(file_list, status_label, progress_bar, root):
    if file_list.size() == 0:
        return "Nenhum arquivo selecionado."

    status_label.config(text="Enviando arquivos para impressão...")
    root.update_idletasks()

    total_files = file_list.size()
    progress_bar["maximum"] = total_files

    try:
        for i, file in enumerate(file_list.get(0, tk.END)):
            if os.path.isfile(file):  # Verifica se o arquivo existe
                if file.lower().endswith('.pdf'):
                    win32api.ShellExecute(0, "print", file, None, ".", 0)
                elif file.lower().endswith('.docx'):
                    word = win32com.client.Dispatch("Word.Application")
                    doc = word.Documents.Open(file)
                    doc.PrintOut()
                    doc.Close(False)
                    word.Quit()
                elif file.lower().endswith('.txt'):
                    win32api.ShellExecute(0, "print", file, None, ".", 0)
                
                # Atualiza a barra de progresso
                progress_bar["value"] = i + 1
                status_label.config(text=f"Imprimindo {i + 1} de {total_files} arquivos...")
                root.update_idletasks()
            else:
                return f"O arquivo {file} não foi encontrado."

        return "Impressão iniciada!"
    except Exception as e:
        return f"Erro ao imprimir arquivos: {e}"

def log_printed_files(file_list):
    with open("historico_impressao.txt", "a") as log_file:
        for file in file_list.get(0, tk.END):
            log_file.write(f"{datetime.datetime.now()}: {file}\n")

def export_list(file_list):
    with open("lista_arquivos.txt", "w") as export_file:
        for file in file_list.get(0, tk.END):
            export_file.write(file + "\n")
    return "A lista de arquivos foi exportada para lista_arquivos.txt"
