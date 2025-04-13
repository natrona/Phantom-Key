import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import os
import json

# ----------------------------
# CONFIGURAÇÕES INICIAIS
# ----------------------------

CONFIG_FILE = 'config.json'

DEFAULT_CONFIG = {
    'length': 16,
    'use_uppercase': True,
    'use_lowercase': True,
    'use_digits': True,
    'use_symbols': True,
    'exclude_similar': False,
    'exclude_ambiguous': False,
    'save_history': True,
    'history_limit': 50
}

HISTORY_FILE = 'history.json'

AMBIGUOUS = '{}[]()/\\\'"`~,;:.<>'
SIMILAR = 'il1Lo0O'

# ----------------------------
# GERADOR DE SENHAS
# ----------------------------

class PasswordGenerator:
    def __init__(self, config):
        self.config = config

    def generate(self):
        chars = ''
        if self.config['use_uppercase']:
            chars += string.ascii_uppercase
        if self.config['use_lowercase']:
            chars += string.ascii_lowercase
        if self.config['use_digits']:
            chars += string.digits
        if self.config['use_symbols']:
            chars += '!@#$%^&*()-_=+'

        if self.config['exclude_similar']:
            chars = ''.join([c for c in chars if c not in SIMILAR])
        if self.config['exclude_ambiguous']:
            chars = ''.join([c for c in chars if c not in AMBIGUOUS])

        if not chars:
            return 'Selecione ao menos uma opção.'

        return ''.join(random.choice(chars) for _ in range(self.config['length']))

# ----------------------------
# HISTÓRICO
# ----------------------------

class PasswordHistory:
    def __init__(self, file_path, limit):
        self.file_path = file_path
        self.limit = limit
        self.data = self.load()

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                try:
                    return json.load(f)
                except:
                    return []
        return []

    def add(self, password):
        self.data.insert(0, password)
        self.data = self.data[:self.limit]
        self.save()

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)

# ----------------------------
# GUI PRINCIPAL
# ----------------------------

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senhas Seguras")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.config = self.load_config()
        self.generator = PasswordGenerator(self.config)
        self.history = PasswordHistory(HISTORY_FILE, self.config['history_limit'])

        self.create_widgets()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                try:
                    return json.load(f)
                except:
                    pass
        return DEFAULT_CONFIG.copy()

    def save_config(self):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=4)

    def create_widgets(self):
        self.title = tk.Label(self.root, text="Gerador de Senhas", font=("Helvetica", 18, 'bold'))
        self.title.pack(pady=10)

        self.password_display = tk.Entry(self.root, font=("Courier", 14), justify='center', width=35)
        self.password_display.pack(pady=10)

        self.length_label = tk.Label(self.root, text="Tamanho da senha:")
        self.length_label.pack()
        self.length_slider = tk.Scale(self.root, from_=6, to=64, orient=tk.HORIZONTAL, command=self.update_length)
        self.length_slider.set(self.config['length'])
        self.length_slider.pack()

        # Checkbuttons
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=10)

        self.uppercase_var = tk.BooleanVar(value=self.config['use_uppercase'])
        self.lowercase_var = tk.BooleanVar(value=self.config['use_lowercase'])
        self.digits_var = tk.BooleanVar(value=self.config['use_digits'])
        self.symbols_var = tk.BooleanVar(value=self.config['use_symbols'])
        self.similar_var = tk.BooleanVar(value=self.config['exclude_similar'])
        self.ambiguous_var = tk.BooleanVar(value=self.config['exclude_ambiguous'])

        self.cb1 = tk.Checkbutton(self.options_frame, text="Letras maiúsculas", variable=self.uppercase_var)
        self.cb2 = tk.Checkbutton(self.options_frame, text="Letras minúsculas", variable=self.lowercase_var)
        self.cb3 = tk.Checkbutton(self.options_frame, text="Números", variable=self.digits_var)
        self.cb4 = tk.Checkbutton(self.options_frame, text="Símbolos", variable=self.symbols_var)
        self.cb5 = tk.Checkbutton(self.options_frame, text="Excluir similares", variable=self.similar_var)
        self.cb6 = tk.Checkbutton(self.options_frame, text="Excluir ambíguos", variable=self.ambiguous_var)

        self.cb1.grid(row=0, column=0, sticky='w')
        self.cb2.grid(row=1, column=0, sticky='w')
        self.cb3.grid(row=2, column=0, sticky='w')
        self.cb4.grid(row=3, column=0, sticky='w')
        self.cb5.grid(row=4, column=0, sticky='w')
        self.cb6.grid(row=5, column=0, sticky='w')

        self.generate_btn = tk.Button(self.root, text="Gerar senha", command=self.generate_password, bg='green', fg='white', height=2)
        self.generate_btn.pack(pady=15)

        self.copy_btn = tk.Button(self.root, text="Copiar para área de transferência", command=self.copy_to_clipboard)
        self.copy_btn.pack(pady=5)

        self.save_btn = tk.Button(self.root, text="Salvar configurações", command=self.save_current_config)
        self.save_btn.pack(pady=5)

        # Histórico
        self.history_label = tk.Label(self.root, text="Histórico de Senhas:")
        self.history_label.pack(pady=5)
        self.history_list = tk.Listbox(self.root, height=8, width=50)
        self.history_list.pack()
        self.update_history_display()

    def update_length(self, val):
        self.config['length'] = int(val)

    def generate_password(self):
        self.update_config_from_ui()
        password = self.generator.generate()
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

        if self.config['save_history']:
            self.history.add(password)
            self.update_history_display()

    def update_config_from_ui(self):
        self.config['use_uppercase'] = self.uppercase_var.get()
        self.config['use_lowercase'] = self.lowercase_var.get()
        self.config['use_digits'] = self.digits_var.get()
        self.config['use_symbols'] = self.symbols_var.get()
        self.config['exclude_similar'] = self.similar_var.get()
        self.config['exclude_ambiguous'] = self.ambiguous_var.get()

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

    def save_current_config(self):
        self.update_config_from_ui()
        self.save_config()
        messagebox.showinfo("Configurações", "Configurações salvas com sucesso.")

    def update_history_display(self):
        self.history_list.delete(0, tk.END)
        for pwd in self.history.data:
            self.history_list.insert(tk.END, pwd)

# ----------------------------
# EXECUÇÃO
# ----------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()
