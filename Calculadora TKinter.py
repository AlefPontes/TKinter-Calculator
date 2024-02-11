from tkinter import *
from tkinter import ttk, font

# Front-End

# Definindo cores para usar no programa
cor1 = "#000000" # Preto
cor2 = "#ffffff" # Branco
cor3 = "#ECEFF1" # Cinza
cor4 = "#a80b00" # Vermelho escuro
cor5 = "#FFAB40" # Laranja
cor6 = "#38576b" # Azul carregado
cor7 = "#d4060a" # Vermelho

# Definindo o tamanho, título e cor da janela
janela = Tk() # Definindo a janela
janela.title("Calculadora Simples") # Título da janela
janela.geometry("235x310") # Tamanho da janela
janela.config(bg=cor1) # Alguns parâmetros de configuração, como a cor do BackGround

# Criando os frames/divisões

# Frame do visor
frame_tela = Frame(janela, width=235, height=50, bg=cor6)
frame_tela.grid(row=0, column=0)

# Frame do corpo
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Back-End

#Variáveis
todos_valores = ''
valor_texto = StringVar() # Transformando a conta em string

#Criando funções

# Função que atualiza o visor da calculadora
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

# Função para calcular a expressão
def calcular():
    try: 
        global todos_valores
        expressão = todos_valores.replace('÷', '/').replace(',', '.').replace('x', '*')
        resultado = eval(expressão)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except:
        valor_texto.set('ERRO')

# Função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

def apagar():
    global todos_valores
    nova_string = todos_valores.rstrip(todos_valores[-1])
    todos_valores = nova_string
    valor_texto.set(todos_valores)
    todos_valores = ''

# Criando label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor6, fg=cor2)
app_label.place(x=0, y=0)

# Criando os botões

# 1ª Linha de botões
b1 = Button(frame_corpo, command = limpar_tela, text="C", width=11, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #Botão clean
b1.place(x=-1, y=0)
b2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão porcentagem
b2.place(x=118, y=0)
b3 = Button(frame_corpo, command = lambda: entrar_valores('÷'), text="÷", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão divisão
b3.place(x=177, y=0)

# 2ª Linha de botões
b4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 7
b4.place(x=0, y=52)
b5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 8
b5.place(x=59, y=52)
b6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 9
b6.place(x=118, y=52)
b7 = Button(frame_corpo, command = lambda: entrar_valores('x'), text="x", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão multiplicação
b7.place(x=177, y=52)

# 3ª Linha de botões
b8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 4
b8.place(x=0, y=104)
b9 = Button(frame_corpo, command = lambda: entrar_valores('5'),  text="5", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 5
b9.place(x=59, y=104)
b10 = Button(frame_corpo, command = lambda: entrar_valores('6'),  text="6", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 6
b10.place(x=118, y=104)
b11 = Button(frame_corpo, command = lambda: entrar_valores('-'),  text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão subtração
b11.place(x=177, y=104)

# 4ª Linha de botões
b12 = Button(frame_corpo, command = lambda: entrar_valores('1'),  text="1", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 1
b12.place(x=0, y=156)
b13 = Button(frame_corpo, command = lambda: entrar_valores('2'),  text="2", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 2
b13.place(x=59, y=156)
b14 = Button(frame_corpo, command = lambda: entrar_valores('3'),  text="3", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 3
b14.place(x=118 , y=156)
b15 = Button(frame_corpo, command = lambda: entrar_valores('+'),  text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão adição
b15.place(x=177, y=156)

# 5ª Linha de botões
b16 = Button(frame_corpo, command = lambda: entrar_valores('0'),  text="0", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 1
b16.place(x=0, y=208)
b17 = Button(frame_corpo, command = lambda: entrar_valores(','),  text=",", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 2
b17.place(x=59, y=208)
b18 = Button(frame_corpo, command = apagar, text="⬅", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão Num 3
b18.place(x=118 , y=208)
b19 = Button(frame_corpo, command = calcular,  text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão igualdade
b19.place(x=177, y=208)

janela.mainloop()
