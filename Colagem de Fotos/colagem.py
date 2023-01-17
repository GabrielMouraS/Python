import os, os.path
import glob
from tkinter import filedialog, messagebox
from shutil import copy, rmtree
from cv2_collage import create_collage


messagebox.showinfo(title='Origem', message='Escolha a pasta com as Imagens')
folder = filedialog.askdirectory()
messagebox.showinfo(title='Destino', message='Escolha o Destino' )
destino = filedialog.askdirectory()

for file in glob.iglob('%s/**/*.jpg' % folder, recursive=True):
    copy(file, '.\colagem')

folderf = r".\colagem"
lst = [os.path.join(folderf, file) for file in os.listdir(folderf)]

collage = create_collage(
    lst=lst, width=1000, background=(255,255,255), save_path= destino +'\colagem.png'
    )
dir = '.\colagem'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

messagebox.showinfo(title='Concluido', message='Pronto')


 
