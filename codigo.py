import pyautogui as pg
import pandas as pd
import time

# pyautogui.write -escrever
# pyautogui.press - apertar 1 tecla
# pyautogui.click - evento clicar na tela

pg.PAUSE = 0.3

#Abrir Windows, Chome e pressionar enter
pg.press("win")
pg.write("chrome")
# pg.write("edge")
pg.press("enter")


#Entar no link do sistema
#bAVEGADOR ANONIMO
#pg.hotkey("ctrl", "shift", "n")
pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press("enter")
#Anonnimo

time.sleep(3)

pg.click(x=898, y=538)
pg.write("nadi192002@gmail.com")
pg.press("tab")
pg.write("admin123")
pg.click(x=1006, y=783)

time.sleep(3)

dados = pd.read_csv("produtos.csv")
print(dados)

#Cadastrar o produto
linha = 0
pg.click(x=712, y=364)
codigo = dados.loc[linha,"codigo"]
pg.write(str(codigo))
pg.press("tab")


#botpython1