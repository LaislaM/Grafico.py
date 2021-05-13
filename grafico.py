import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter 

#Criar dados para o eixo x 
np.random.seed(19680800)

X= np.linspace(0.5,7, 150)
X

# Criar dados para a função Y1
Y1 = 4+np.cos(X)
Y1

# Criar dados para a função Y2
Y2 = 1+np.cos(3+X/0.5)/2
Y2

# Criar dados para a função Y3
Y3 = np.random.uniform(Y1, Y2, len(X))
Y3

# Função para rotular ticks
def minor_tick(x, pos):
    if not x % 0.20:
        return ""
    return "%.2f" % x

# Função para criar círculos
def circle(x, y, radius=0.20):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke
    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=1,
                    edgecolor='black', facecolor=(0, 0, 0, .0125),
                    path_effects=[withStroke(linewidth=5, foreground='w')])
    ax.add_artist(circle)

# Função para criar rótulos
def text(x, y, text):
    ax.text(x, y, text, backgroundcolor="white",
            ha='center', va='top', weight='bold', color='blue')
    
    # Criar um área de trabalho
fig = plt.figure(figsize=(12, 12))
# Criar um espaço para colocar um gráfico
ax = fig.add_subplot(1, 1, 1, aspect=1)

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)
#Dimensionar os eixos
ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
#Colocar os rótulos dos ticks
ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

fig = plt.figure(figsize=(12, 812))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

def minor_tick(x, pos):
    if not x % 1.0:
        return ""
    return "%.2f" % x
ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))
#Colocar novos limites aos eixos
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
#Definir o formato das divisões
ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0)
ax.tick_params(which='minor', length=5, labelsize=8, labelcolor='0.5')

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')
#Colocar o grid valores possíveis '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
ax.grid(linestyle="--", linewidth=0.5, color='8', zorder=-10)

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=8)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
#Plotar a função Y1 (X,Y,cor,espessura da linha,etiqueta)
ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Linha Azul", zorder=10)

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limte superior", zorder=10)
#Plotar a função Y2 (X,Y,cor,espessura da linha,etiqueta)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite inferior")

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite inferior")
#Plotar a função Y2 (X,Y,cor,espessura da linha,etiqueta)   https://matplotlib.org/stable/api/markers_api.html
ax.plot(X, Y3, linewidth=1, marker='p', markerfacecolor='b', markeredgecolor='black')

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite  inferior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')
# Colocar o título do gráfico
ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite inferior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
#Colocar o título do eixo X
ax.set_xlabel("Título do eixo X")

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Linha Azul", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Linha Vermelha")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Titulo eixo do x")
#Colocar o título do eixo Y
ax.set_ylabel("Titulo eixo do Y")

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Linha Vermelha")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")
#Colocar a leyenda das funções
ax.legend()

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite inferior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')
ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Colocar Indicador de Marcas menores
circle(1, 0.1)
text(1, 75, "2100486")

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))
ax.yaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite inferior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite superior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Marcas Menores
circle(0.50, -0.10)
text(0.50, -0.32, "Marcas menores")

# Marca Menor
circle(0.00, 3.50)
text(0.00, 3.30, "Marca menor")

# Marca Maior
circle(-0.03, 4.00)
text(0.03, 3.80, "Marca maior")

# Etiqueta Marca Maior
circle(-0.15, 3.00)
text(-0.15, 2.80, "Etiqueta marca maior")

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite inferior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite superior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Marcas Menores
circle(0.50, -0.10)
text(0.50, -0.32, "Marcas menores")

# Marca Menor
circle(0.00, 3.50)
text(0.00, 3.30, "Marca menor")

# Marca Maior
circle(-0.03, 4.00)
text(0.03, 3.80, "Marca maior")

# Etiqueta Marca Maior
circle(-0.15, 3.00)
text(-0.15, 2.80, "Etiqueta marca maior")

# Título eixo X 
circle(1.80, -0.27)
text(1.80, -0.45, "Título eixo X")

# Título eixo Y
circle(-0.27, 1.80)
text(-0.27, 1.6, "Título eixo Y")

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Linha Azul", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Linha Vermelha")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Anatomía de um gráfico", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Marcas Menores
circle(0.50, -0.10)
text(0.50, -0.32, "Marcas menores")

# Marca Menor
circle(0.00, 3.50)
text(0.00, 3.30, "Marca menor")

# Marca Maior
circle(-0.03, 4.00)
text(0.03, 3.80, "Marca maior")

# Etiqueta Marca Maior
circle(-0.15, 3.00)
text(-0.15, 2.80, "Etiqueta marca maior")
# Título eixo X 
circle(1.80, -0.27)
text(1.80, -0.45, "Título eixo X")

# Título eixo Y
circle(-0.27, 1.80)
text(-0.27, 1.6, "Título eixo Y")

# Título
circle(1.60, 4.13)
text(1.60, 3.93, "Título")

# Linha Azul
circle(1.75, 2.80)
text(1.75, 2.60, "Linha\n(gráfico de linha)")

# Linha Vermelha
circle(1.20, 0.60)
text(1.20, 0.40, "Linha\n(gráfico de linha)")

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite Superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite Inferior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()
# Marcas Menores
circle(0.50, -0.10)
text(0.50, -0.32, "Marcas menores")

# Marca Menor
circle(0.00, 3.50)
text(0.00, 3.30, "Marca menor")

# Marca Maior
circle(-0.03, 4.00)
text(0.03, 3.80, "Marca maior")

# Etiqueta Marca Maior
circle(-0.15, 3.00)
text(-0.15, 2.80, "Etiqueta marca maior")

# Título eixo X 
circle(1.80, -0.27)
text(1.80, -0.45, "Título eixo X")

# Título eixo Y
circle(-0.27, 1.80)
text(-0.27, 1.6, "Título eixo Y")

# Título
circle(1.60, 4.13)
text(1.60, 3.93, "Título")

# Linha Azul
circle(1.75, 2.80)
text(1.75, 2.60, "Linha\n(gráfico de linha)")

# Linha Vermelha
circle(1.20, 0.60)
text(1.20, 0.40, "Linha\n(gráfico de linha)")

# Scatter
circle(3.20, 1.75)
text(3.20, 1.55, "Markers\n(scatter plot)")

# Grade
circle(3.00, 3.00)
text(3.00, 2.80, "Grade")

# Legenda
circle(3.70, 3.80)
text(3.70, 3.60, "Legenda")
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite Superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite Inferior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Marcas Menores
circle(0.50, -0.10)
text(0.50, -0.32, "Marcas menores")

# Marca Menor
circle(0.00, 3.50)
text(0.00, 3.30, "Marca menor")

# Marca Maior
circle(-0.03, 4.00)
text(0.03, 3.80, "Marca maior")

# Etiqueta Marca Maior
circle(-0.15, 3.00)
text(-0.15, 2.80, "Etiqueta marca maior")

# Título eixo X 
circle(1.80, -0.27)
text(1.80, -0.45, "Título eixo X")

# Título eixo Y
circle(-0.27, 1.80)
text(-0.27, 1.6, "Título eixo Y")

# Título
circle(1.60, 4.13)
text(1.60, 3.93, "Título")

# Linha Azul
circle(1.75, 2.80)
text(1.75, 2.60, "Linha\n(gráfico de linha)")

# Linha Vermelha
circle(1.20, 0.60)
text(1.20, 0.40, "Linha\n(gráfico de linha)")

# Scatter
circle(3.20, 1.75)
text(3.20, 1.55, "Markers\n(scatter plot)")

# Grade
circle(3.00, 3.00)
text(3.00, 2.80, "Grade")

# Legenda
circle(3.70, 3.80)
text(3.70, 3.60, "Legenda")

# Eixos
circle(0.5, 0.5)
text(0.5, 0.3, "Eixos")

# Figura
circle(-0.3, 0.65)
text(-0.3, 0.45, "Figura")

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))
ax.yaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite Superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite Inferior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Marca Menor
circle(0.50, -0.10)
text(0.50, -0.32, "Marcas menores")

# Marca Menor
circle(0.00, 3.50)
text(0.00, 3.30, "Marca menor")

# Marca Maior
circle(-0.03, 4.00)
text(0.03, 3.80, "Marca maior")

# Etiqueta Marca Maior
circle(-0.15, 3.00)
text(-0.15, 2.80, "Etiqueta marca maior")

# Título eixo X 
circle(1.80, -0.27)
text(1.80, -0.45, "Título eixo X")

# Título eixo Y
circle(-0.27, 1.80)
text(-0.27, 1.6, "Título eixo Y")

# Título
circle(1.60, 4.13)
text(1.60, 3.93, "Título")

# Linha Azul
circle(1.75, 2.80)
text(1.75, 2.60, "Linha\n(gráfico de linha)")

# Linha Vermelha
circle(1.20, 0.60)
text(1.20, 0.40, "Linha\n(gráfico de linha)")

# Scatter
circle(3.20, 1.75)
text(3.20, 1.55, "Markers\n(scatter plot)")

# Grade
circle(3.00, 3.00)
text(3.00, 2.80, "Grade")

# Legenda
circle(3.70, 3.80)
text(3.70, 3.60, "Legenda")

# Eixos
circle(0.5, 0.5)
text(0.5, 0.3, "Eixos")

# Figura
circle(-0.3, 0.65)
text(-0.3, 0.45, "Figura")

#Colocar comentarios
color = 'blue'
ax.annotate('bordas', xy=(4.0, 0.35), xycoords='data',
            xytext=(3.3, 0.5), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.annotate('', xy=(3.15, 0.0), xycoords='data',
            xytext=(3.45, 0.45), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Linha inferior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Marca Menor
circle(0.50, -0.10)
text(0.50, -0.32, "Marcas menores")

# Marca Menor
circle(0.00, 3.50)
text(0.00, 3.30, "Marca menor")

# Marca Maior
circle(-0.03, 4.00)
text(0.03, 3.80, "Marca maior")

# Etiqueta Marca Maior
circle(-0.15, 3.00)
text(-0.15, 2.80, "Etiqueta marca maior")

# Título eixo X 
circle(1.80, -0.27)
text(1.80, -0.45, "Título eixo X")

# Título eixo Y
circle(-0.27, 1.80)
text(-0.27, 1.6, "Título eixo Y")

# Título
circle(1.60, 4.13)
text(1.60, 3.93, "Título")

# Linha Azul
circle(1.75, 2.80)
text(1.75, 2.60, "Linha\n(gráfico de linha)")

# Linha Vermelha
circle(1.20, 0.60)
text(1.20, 0.40, "Linha\n(gráfico de linha)")

# Scatter
circle(3.20, 1.75)
text(3.20, 1.55, "Markers\n(scatter plot)")

# Grade
circle(3.00, 3.00)
text(3.00, 2.80, "Grade")

# Legenda
circle(3.70, 3.80)
text(3.70, 3.60, "Legenda")

# Eixos
circle(0.5, 0.5)
text(0.5, 0.3, "Eixos")

# Figura
circle(-0.3, 0.65)
text(-0.3, 0.45, "Figura")

color = 'blue'
ax.annotate('bordas', xy=(4.0, 0.35), xycoords='data',
            xytext=(3.3, 0.5), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                               color=color))

ax.annotate('', xy=(3.15, 0.0), xycoords='data',
            xytext=(3.45, 0.45), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

#Colocar texto
ax.text(4.0, -0.4, "Made with http://matplotlib.org",
        fontsize=10, ha="right", color='0.5')
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))
ax.yaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite inferior")
ax.plot(X, Y3, linewidth=0, 
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Laisla Souza", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Marca Menor
circle(1, 1)
text(1, 0.8, "RA:2100486")



#Colocar texto
ax.text(4.0, -0.4, "Made with http://matplotlib.org",
        fontsize=10, ha="right", color='0.5')

#plt.show()
#Salvar o arquivo
from google.colab import files
plt.savefig("Hands_On_Matplotlib.png")
files.download("Hands_On_Matplotlib.png")
