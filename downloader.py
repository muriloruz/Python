from pytube import YouTube as yt
from tkinter.filedialog import askdirectory
import tkinter as tk

def main():
    root = tk.Tk()
    root.withdraw()
    url = input("Cole a url do video: ")
    try:
        video = yt(url)
        path = askdirectory(title='Escolha uma pasta')
        try:
            melhorQualidade = video.streams.get_highest_resolution()
            a = melhorQualidade.download(path)
            print('Download feito!')
            print(f'O video foi baixado na seguinte pasta:{a}')
        except:
            print("Houve um erro no download, tente novamente")
    except:
        print("Há um erro na URL, por favor, tente novamente")
        main()
    finally:
        root.destroy()
main()



