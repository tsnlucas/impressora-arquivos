import tkinter as tk
from file_operations import select_files, clear_list, print_files, log_printed_files, export_list
from ui import create_ui

# Criar a interface do usuário
root, file_list, progress_bar, status_label, select_button, print_button, clear_button, export_button = create_ui()

# Conectar os botões às funções
select_button.config(command=lambda: select_files(file_list))
print_button.config(command=lambda: status_label.config(text=print_files(file_list, status_label, progress_bar, root)))  # Passar root
clear_button.config(command=lambda: clear_list(file_list))
export_button.config(command=lambda: status_label.config(text=export_list(file_list)))

# Iniciar o loop principal da aplicação
root.mainloop()
