import os, os.path
import glob
from tkinter import filedialog, messagebox
from shutil import copy, rmtree
from cv2_collage import create_collage

#Messagebox.showinfo é igual uma mensagem de alerta, que aparecem a caixinha no Windowns e você aperta o OK.
#E pedi ao usuario para que ele escolha a pasta com imagens.
messagebox.showinfo(title='Origem', message='Escolha a pasta com as Imagens')
#Aqui eu fiz aparecer aquela janela de escolher pastas e armazenei o valor no 'folder'.
folder = filedialog.askdirectory()
#Messagebox.showinfo mais uma vez, porém aqui peço para que ele escolha o destino.
messagebox.showinfo(title='Destino', message='Escolha o Destino' )
#o usuario vai escolher a pasta e o valor é armazenado em 'destino'.
destino = filedialog.askdirectory()

#loop utilizando o 'for' e uso o glob para copiar todos arquivos de pastas 
#e subpastas para pasta '\colagem'
for file in glob.iglob('%s/**/*.jpg' % folder, recursive=True):
    copy(file, '.\colagem')
#aqui coloco o caminho na varialvel 'folderf' assim fazendo encontrar as imagens copiadas de pastas e subpastas.
folderf = r".\colagem"
lst = [os.path.join(folderf, file) for file in os.listdir(folderf)]

#aqui começa a colagem das imagens utilizando 'cv2_collage'
collage = create_collage( 
     #aqui é definida a cor de fundo, a pasta de destino, e o nome e formato do arquivo
    lst=lst, width=1000, background=(255,255,255), save_path= destino +'\colagem.png'
    )
#nessa etapa temos que apagar os arquivos que foram copiados para a pasta '\colagem'
dir = '.\colagem'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
    
#logo após tudo terminar o programa avisa ao usuario que acabou.
messagebox.showinfo(title='Concluido', message='Pronto')


 
