import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


CJTO = 12803 # RA 201510962

dics = [
    pd.read_csv('dics/1_jan.csv'),
    pd.read_csv('dics/2_fev.csv'),
    pd.read_csv('dics/3_mar.csv'),
    pd.read_csv('dics/4_abri.csv'),
    pd.read_csv('dics/5_mai.csv'),
    pd.read_csv('dics/6_jun.csv'),
    pd.read_csv('dics/7_jul.csv'),
    pd.read_csv('dics/8_ago.csv'),
    pd.read_csv('dics/9_set.csv'),
    pd.read_csv('dics/10_out.csv'),
    pd.read_csv('dics/11_nov.csv'),
    pd.read_csv('dics/12_dez.csv')
]

consumidores = [
    pd.read_csv('consumidores/1_jan.csv'),
    pd.read_csv('consumidores/2_fev.csv'),
    pd.read_csv('consumidores/3_marc.csv'),
    pd.read_csv('consumidores/4_abril.csv'),
    pd.read_csv('consumidores/5_mai.csv'),
    pd.read_csv('consumidores/6_jun.csv'),
    pd.read_csv('consumidores/7_jul.csv'),
    pd.read_csv('consumidores/8_ago.csv'),
    pd.read_csv('consumidores/9_set.csv'),
    pd.read_csv('consumidores/10_out.csv'),
    pd.read_csv('consumidores/11_nov.csv'),
    pd.read_csv('consumidores/12_dez.csv')
]

results_dec = []
results_fec = []
sum_mes = []
conjuto_consumidores = []
for i in range(12):
    dics[i] = dics[i][ dics[i]['Cjto'] == CJTO ]
    consumidores[i] = consumidores[i][ consumidores[i]['Código do Conjunto'] == CJTO ]
    results_dec.append(  dics[i].DIC.sum() / consumidores[i]['Nº de Consumidores do Cojunto'].iat[0])
    results_fec.append(  dics[i].FIC.sum() / consumidores[i]['Nº de Consumidores do Cojunto'].iat[0])
    sum_mes.append(f"{i}/14")
    conjuto_consumidores.append(consumidores[i]['Nº de Consumidores do Cojunto'].iat[0])

media_conjuto_consumidores = sum(conjuto_consumidores) / 12

Fec_anual = 0
Dec_anual = 0
for i in range(12):
    Fec_anual += (results_dec[i] * conjuto_consumidores[i] / media_conjuto_consumidores )
    Dec_anual += (results_fec[i] * conjuto_consumidores[i] / media_conjuto_consumidores )

sns.set_theme(style="ticks", color_codes=True)


x_pos = [i for i, _ in enumerate(results_dec)]

plt.bar(x_pos, results_dec, color='green')
plt.xlabel("Mês/Ano")
plt.ylabel("Horas")
plt.title("Grafico 3: DEC mensal")

plt.xticks(x_pos, sum_mes)

plt.show()

x_pos = [i for i, _ in enumerate(results_fec)]

plt.bar(x_pos, results_fec, color='green')
plt.xlabel("Mês/Ano")
plt.ylabel("Numero de interrupções")
plt.title("Grafico 4: FEC mensal")

plt.xticks(x_pos, sum_mes)

plt.show()