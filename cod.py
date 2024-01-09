import pyautogui as auto
import time
import pandas as pd


     

auto.PAUSE = 1
##########################################Entrando no opera e acessando o site###################################################

auto.press("win")
auto.write("opera")
auto.press("enter")
auto.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
auto.press("enter")



# Apertar win 
# escrever google
#acessar site

#############################################################################################



###############################################Login##############################################

auto.click(x=757, y=382)
auto.write("Emanuel")
auto.press("tab")    

# tab

auto.write("123123")
auto.press("tab")

#tab

auto.press("enter")
#fazer login

#########################################Cadastrar produtos####################################################

#acessando pandas
dados = pd.read_csv("produtos.csv")
print(dados)



for lista in dados.index: #index acessa as linhas    


    auto.click(x=750, y=275)
    auto.write(dados.loc[lista,"codigo"]) #codigo
    auto.press("tab")

    #tab

    auto.write(dados.loc[lista,"marca"])#marca
    auto.press("tab")

    #tab

    auto.write(dados.loc[lista,"tipo"])#tipo

    auto.press("tab")

    #tab

    auto.write(str(dados.loc[lista,"categoria"]))# ou str(1)

    auto.press("tab")

    #tab

    auto.write(str(dados.loc[lista, "preco_unitario"]))#preco_unitario

    auto.press("tab")

    #tab

    auto.write(str(dados.loc[lista,"custo"]))

    auto.press("tab")
    #################################################Logica NaN############################################################
    
    if not pd.isna(dados.loc[lista,"obs"]):#se for nulo 
        auto.write(dados.loc[lista,"obs"])


    #############################################################################################################

    auto.press("tab")
    auto.press("enter")


    #########################################Subindo o scroll####################################################


    auto.scroll(1000)

    #################################################### fim do codigo  #########################################################
