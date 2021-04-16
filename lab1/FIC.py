import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from dateutil.relativedelta import relativedelta
import seaborn as sns

import matplotlib
import matplotlib.pyplot as plt


df = pd.read_csv('task1.csv')

df['data_inicio'] =  pd.to_datetime(df['Data_inicio'] + ' ' + df['Hora_inicio'], format = '%m/%d/%Y %H:%M:%S')
df['data_fim'] =  pd.to_datetime( df['Data_fim'] + ' ' + df['Horario_fim'], format = '%m/%d/%Y %H:%M:%S')



# Filtrar os dados para o aluno 201510962
df = df.loc[ (df.UC == 2548925) & df.Motivo_expurgo.isnull() , :]

# Exemplo Mês Abril - UC 32542895:

janeiro_começo = datetime.fromisoformat('2014-01-01')
janeiro_fim = datetime.fromisoformat('2014-01-31')

# dados_32542895 = df.query(f"UC == 2548925 & data_inicio > {abril_começo} & data_fim < {abril_fim}")
sum_mes = []
sum_result = []
for i in range(1,13):
    df[f"mes_{i}"] = 0
    df.loc[  (df.data_inicio >=  janeiro_começo + relativedelta(months = i)) & (df.data_fim <= janeiro_fim + relativedelta(months = i)), f'mes_{i}' ] = (df.data_fim - df.data_inicio)/np.timedelta64(1, 'h')
    sum_result.append(df.query(f'mes_{i} > 0' )[f'mes_{i}'].count())
    sum_mes.append(f"{i}/14")


sum_mes = []
max_total = []
for i in range(1,13):
    df[f"mes_{i}"] = 0
    df.loc[  (df.data_inicio >=  janeiro_começo + relativedelta(months = i)) & (df.data_fim <= janeiro_fim + relativedelta(months = i)), f'mes_{i}' ] = (df.data_fim - df.data_inicio)/np.timedelta64(1, 'h')
    max_total.append(df.query(f'mes_{i} > 0' )[f'mes_{i}'].max())
    sum_mes.append(f"{i}/14")

# fig, ax = plt.subplots()

# p1 = ax.bar(sum_mes,sum_result)

# ax.axhline(0, color='grey', linewidth=0.8)
# ax.set_ylabel('Horas')
# ax.set_title('DIC por mensal da unidade consumidora 2548925')
# ax.set_xticklabels(sum_mes)

# Label with label_type 'center' instead of the default 'edge'


# sns.set()
sns.set_theme(style="ticks", color_codes=True)


x_pos = [i for i, _ in enumerate(sum_result)]

plt.bar(x_pos, sum_result, color='green')
plt.xlabel("Mês/Ano")
plt.ylabel("Numero de Interrupções")
plt.title("Grafico 2: FIC mensal")

plt.xticks(x_pos, sum_mes)

plt.show()