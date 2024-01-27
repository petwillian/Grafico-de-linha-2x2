# Grafico 2x2, 2 linha 2 coluna

# passo 1 - importa a biblioteca
import matplotlib.pyplot as plt

#passo 2 - intanciar o objeto figura
fig, ax = plt.subplots(2, 2) # 2x2

#passo 3 - Definir os dados
indices = [1,2,3,4]
amostra_a = [1,4,2,3]
amostra_b = [2,8,4,6]
amostra_c = [4,16,8,12]
amostra_d = [8,32,16,24]

#passo 4 - plotar os dados no axe/eixo(grafico)
ax[0][0].plot(indices, amostra_a, label="Amostra A", color = 'blue', marker = 'o')
ax[0][1].plot(indices, amostra_b, label="Amostra B", color = 'green', marker = 'o')
ax[1][0].plot(indices, amostra_c, label="Amostra C", color = 'red', marker = 'o')
ax[1][1].plot(indices, amostra_d, label="Amostra D", color = 'yellow', marker = 'o')

# titulo do grafico
ax[0][0].set_title("Titúlo do Gráfico 0x0")
ax[0][1].set_title("Titúlo do Gráfico 0x1")
ax[1][0].set_title("Titúlo do Gráfico 1x0")
ax[1][1].set_title("Titúlo do Gráfico 1x1")

# titulo do eixo x
ax[0][0].set_xlabel("Label X 0x0")
ax[0][1].set_xlabel("Label X 0x1")
ax[1][0].set_xlabel("Label X 1x0")
ax[1][1].set_xlabel("Label X 1x1")

#ax[1].set_xlabel("Label X 1")

# titulo do eixo y
ax[0][0].set_ylabel("Label y 0x0")
ax[0][1].set_ylabel("Label y 0x1")
ax[1][0].set_ylabel("Label y 1x0")
ax[1][1].set_ylabel("Label y 1x1")

# a legenda
ax[0][0].legend()
ax[0][1].legend()
ax[1][0].legend()
ax[1][1].legend()

#passo 5 - apresentar o grafico
plt.show()