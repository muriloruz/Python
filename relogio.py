from datetime import datetime
import tkinter as tk


def get_horas():
    agora = datetime.now()
    horaf = agora.strftime("%d/%m/%Y - %H:%M:%S")
    return horaf


def att_time():
    label = tk.Label(root, text=get_horas(), font=("Arial", 20, "bold"), foreground="white")
    label.config(bg="black")
    label.place(relx=0.5, rely=0.5, anchor='center')
    root.after(1000, att_time)

def cent_window(janela):
    janela.update_idletasks()
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela//2) - (largura_janela//2)
    y = (altura_tela//2) - (altura_janela//2)
    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    print(f"{largura_janela}x{altura_janela}+{x}+{y}")


root = tk.Tk()
root.geometry("300x50")
cent_window(root)
root.title("Clock")
root.config(bg="black")
att_time()
root.mainloop()
