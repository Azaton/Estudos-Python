### Porjeto CFD - Consultar BD, gerar gráfico e plotar no frontend ###
# Cada linha será comentada para fim de estudos e não seguem uma boa prática.
# Boa prática: indentação do código está sendo aplicada

import sqlite3 # interagir com o banco de dados SQLite
from flask import Flask, render_template, send_from_directory # para criar um servidor web, render_template para renderizar um modelo HTML,send_from_directory para enviar arquivos estáticos
import seaborn as sns # para melhorar a estética do gráfico,
import numpy as np # para manipulação de arrays 
import matplotlib.pyplot as plt # para plotar o gráfico.
import os

app = Flask(__name__)

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

@app.route('/chart/<path:filename>')
def serve_chart(filename):
    return send_from_directory(static_dir, filename)

@app.route('/') # Rota para exibir o gráfico
def show_cfd_chart():
    conn = sqlite3.connect(r'D:\DevOps\Projetos\Cumulative Flow Diagram\BD\CFD') # Conectando ao banco de dados (no exemplo está local)
    cursor = conn.cursor() # Criando o cursor    
    query = "SELECT * FROM TB_CFD" # Executando a consulta SQL para selecionar todos os dados da tabela
    cursor.execute(query)

    results = cursor.fetchall() # Obtendo todos os resultados da consulta

    # Fechando o cursor e a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Separando os dados em listas para plotagem do gráfico
    dates = [row[1] for row in results]
    statuses = [row[2] for row in results]
    counts = [row[3] for row in results]
    
    fig, ax = plt.subplots() # Criando o gráfico CFD, uma figura e um conjunto de eixos para o gráfico. 
    unique_statuses = np.unique(statuses)  # Obter estados únicos
    colors = sns.color_palette('tab20', len(unique_statuses))  # Cores para os estados únicos da lista "statuses" e geram uma paleta de cores com base nesses estados usando o "seaborn".

    for i, status in enumerate(unique_statuses):
        status_counts = [count if s == status else 0 for s, count in zip(statuses, counts)]
        cumulative_counts = np.cumsum(status_counts)
        ax.plot(dates, cumulative_counts, marker='o', label=status, color=colors[i])

    ax.set_xlabel('Semanas')
    ax.set_ylabel('Quantidade de Trabalho')
    ax.set_title('Diagrama de Fluxo Cumulativo')
    ax.legend()
    ax.grid(True)

    fig.canvas.draw() 

    chart_path = os.path.join(static_dir, 'chart.png') # Salvando o gráfico em um arquivo temporário
    plt.savefig(chart_path)
    plt.close(fig)

    # Renderizando o template HTML com o gráfico
    return render_template('chart.html', chart_path=chart_path)

if __name__ == '__main__': # Executando o servidor Flask    
    app.run()