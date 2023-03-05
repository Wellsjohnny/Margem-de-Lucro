import tkinter as tk
import sys
import os

class App:
    def __init__(self, master):
        self.master = master
        master.title("Margem de lucro")
        master.geometry("350x150")
        master.configure(bg='#3d405b')
        
       # Adicionando o icone na janela
            #  retorna caminho completo do diretório onde o script está localizado, sem o nome do próprio script.
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
            # Junta o caminho onde está o diretório com a pasta imgs onde está o icone "calculator-icon.ico"
        icon_path = os.path.join(script_dir, "imgs","calculator-icon.ico")
        master.iconbitmap(icon_path)

        # Criando os elementos na tela
        self.label1 = tk.Label(master, bg='#3d405b', fg='#edf2f4',text="Digite o custo do produto R$:")
        self.campo1 = tk.Entry(master)

        self.label2 = tk.Label(master, bg='#3d405b',fg='#edf2f4',text="Digite valor do produto R$:")
        self.campo2 = tk.Entry(master)

        self.label3 = tk.Label(master, bg='#3d405b',fg='#edf2f4',text="Lucratidade %:")
        self.campo3_var = tk.StringVar()
        self.campo3 = tk.Entry(master, state='readonly', textvariable=self.campo3_var)

        # Posicionamentos 
        self.label1.grid(row=0, column=0, padx=5)
        self.campo1.grid(row=0, column=1, padx=10)
      
        self.label2.grid(row=2, column=0,padx=5)
        self.campo2.grid(row=2, column=1, padx=10)

        self.label3.grid(row=3, column=0, padx=5)
        self.campo3.grid(row=3, column=1, padx=10)
        
        empty_label = tk.Label(root, text="",bg='#3d405b')
        empty_label.grid(row=4, column=0, padx=10, pady=20)
       
        # Criar o botão de cálculo
        self.botao = tk.Button(master, text='Calcular', fg='white', bg='#e63946', command=self.calcular_campos)
        self.botao.grid(row=4,column=1)
        
    def calcular_campos(self):
        # Obter os valores dos dois campos de entrada
        valor1 = float(self.campo1.get().replace(",","."))
        valor2 = float(self.campo2.get().replace(",","."))
        
        # Calcular os valores e definir o valor do terceiro campo de entrada como o resultado
        self.campo3.delete(0, tk.END)
        self.campo3_var.set(str(round((valor2 - valor1) / valor1 * 100, 2)) + '%')

root = tk.Tk()
app = App(root)
root.mainloop()
