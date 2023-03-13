from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from pytube.exceptions import RegexMatchError

#variavel que armazena a janela
janela = Tk()

#na janela coloque o titulo que está entre aspas simples
janela.title('Baixar Vídeos do Youtube')

#criamos uma função de Download, que tem também um "local de Download", que é responsavel
#por perguntar local para salvar arquivo
def download(link_):
    if link_:
        #chamando função de download, caso esteja vazio, vai trazer janela de erro
        #caso o link esteja invalido, também vai trazer janela de erro.
        try:
            localdownload = filedialog.askdirectory()
            YouTube(link_).streams.get_highest_resolution().download(localdownload)
            aviso()
        except RegexMatchError:
            aviso_erro()
    else:
        aviso_erro()
    
#criando aviso de de comclusão do download
def aviso():
        janela_mensagem = Toplevel()
        janela_mensagem.title('Aviso')
        janela_mensagem.geometry('300x200')
        #criando Texto e botão após a comclusão aparecer janela dizendo que foi comcluido
        Label(janela_mensagem, text='Download feito com sucesso!', font='arial 12 bold', pady=30).pack()
        Button(janela_mensagem, text='OK', command=janela_mensagem.destroy).pack()

    
    
def aviso_erro():
    janela_mensagem = Toplevel()
    janela_mensagem.title('Aviso')
    janela_mensagem.geometry('300x200')
    #criando Texto e botão que diga que o link é invalido.
    Label(janela_mensagem, text='Insira um Link Válido', font='arial 12 bold', pady=30).pack()
    Button(janela_mensagem, text='OK', command=janela_mensagem.destroy).pack()
    
    

#quadro vai receber frame, onde frame vai está desenhado na janela
quadro = Frame(janela)
#chamar o quadro para colocar na janela
quadro.pack()


#colocar label no quadro, onde vai ter um texto, com a fonte citada.
Label(quadro, text='Insira o Link do YouTube: ', font='arial 12 bold').pack(side='left')

#colocar o espaço para receber link, e no pack disse para desenhar a esquerda
link = Entry(quadro, font='arial 20', width=50)
link.pack(side='left')

#criamos um botão, e nele, tem comando lambda onde vai receber o link que foi inserido no download.
Button(quadro, bg='blue', text='>>>', font='arial 9 bold' , bd=2, fg='white', height=2, command=lambda: download(link.get())).pack()

#deixar a janela aberta por tempo indefinido
janela.mainloop()
