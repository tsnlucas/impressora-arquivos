import tkinter as tk
from tkinter import ttk

def create_ui():
    root = tk.Tk()
    root.title("Impressora de Arquivos")
    root.geometry("600x600")
    root.resizable(False, False)

    # Usando ttk para estilo
    style = ttk.Style()
    style.theme_use('clam')  # Escolha de um tema

    # Configurando estilos personalizados
    bg_color = "#f4f4f4"  # Cor de fundo do aplicativo
    style.configure("TButton", padding=6, relief="flat", background=bg_color, foreground="black", font=("Arial", 12, "bold"))
    style.map("TButton", background=[("active", "#d9d9d9")])  # Cor ao passar o mouse

    # Frame para o título
    title_frame = ttk.Frame(root)
    title_frame.pack(pady=10)

    # Título
    title_label = ttk.Label(title_frame, text="Impressora de Arquivos", font=("Arial", 18, "bold"))
    title_label.pack()

    # Frame para a lista de arquivos
    frame_list = ttk.Frame(root)
    frame_list.pack(pady=10, fill=tk.BOTH, expand=True)

    # Lista para mostrar os arquivos selecionados
    file_list = tk.Listbox(frame_list, selectmode=tk.MULTIPLE, width=80, height=15)
    file_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbar para a lista de arquivos
    scrollbar = ttk.Scrollbar(frame_list, orient=tk.VERTICAL, command=file_list.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    file_list.config(yscrollcommand=scrollbar.set)

    # Frame para os botões de controle
    frame_controls = ttk.Frame(root)
    frame_controls.pack(pady=10, fill=tk.X)

    # Botões com estilo
    select_button = ttk.Button(frame_controls, text="Selecionar Arquivos")
    select_button.pack(side=tk.LEFT, padx=10, pady=10)

    print_button = ttk.Button(frame_controls, text="Imprimir Arquivos")
    print_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Frame para os botões "Limpar Lista" e "Fechar"
    frame_bottom_controls = ttk.Frame(root)
    frame_bottom_controls.pack(pady=10, fill=tk.X)

    clear_button = ttk.Button(frame_bottom_controls, text="Limpar Lista")
    clear_button.pack(side=tk.LEFT, padx=10, pady=10)

    export_button = ttk.Button(frame_bottom_controls, text="Exportar Lista")
    export_button.pack(side=tk.LEFT, padx=10, pady=10)

    close_button = ttk.Button(frame_bottom_controls, text="Fechar", command=root.quit)
    close_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Frame para a barra de progresso e status
    frame_status = ttk.Frame(root)
    frame_status.pack(pady=10)

    progress_bar = ttk.Progressbar(frame_status, orient="horizontal", length=400, mode="determinate")
    progress_bar.pack(pady=5)

    # Label para mostrar o status
    status_label = ttk.Label(root, text="", padding=10)
    status_label.pack(pady=5)

    return root, file_list, progress_bar, status_label, select_button, print_button, clear_button, export_button
