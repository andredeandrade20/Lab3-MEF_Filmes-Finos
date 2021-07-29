import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## medidas de corrente e tensão para depósito de prata com 140nm, 200nm e 260nm de espessura
data = {'I(mA) +/- 0.001': [1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0], '140nm - V(mV) +/- 0.01': [101.8, 101.3, 181.3, 181.2, 280.4, 276.2, 365.0, 363.0, 480.0, 475.0], '200nm - V(mV) +/- 0.01': [15.23, 14.90, 29.71, 29.60, 43.80, 43.70, 58.07, 57.90, 72.25, 71.97] , '260nm - V(mV) +/- 0.01': [4.08, 4.08, 8.18, 8.16, 12.29, 12.27, 16.51, 16.42, 21.02, 21.05]}
df1 = pd.DataFrame(data = data)

## Média das medições de corrente e tensão para depósito de prata com 140nm, 200nm e 260nm de espessura
data2 = {'I(mA)': [1.0, 2.0, 3.0, 4.0, 5.0], 'V(mV) - 140nm': [101.55, 181.25, 278.30, 365.00, 477.50], 'R(Ohm) - 140nm': [101.5, 90.6, 92.8, 91.0, 95.5], 'V(mV) - 200nm': [15.06, 29.66, 43.75, 57.98, 72.11] , 'R(Ohm) - 200nm': [15.1, 14.8, 14.6, 14.5, 14.4], 'V(mV) - 260nm': [4.08, 8.17, 12.28, 16.46, 21.04], 'R(Ohm) - 260nm': [4.08, 4.08, 4.09, 4.12, 4.20]}
df2 = pd.DataFrame(data = data2)

## Cálculo de a (largura) baseado na fórmula R = ro*L/A, com A = a*e
roag = 1.62*(10**(-8)) ## Ohm.m
df2 = df2.assign(a140 = (roag*3*(10**(12))/(df2['R(Ohm) - 140nm']*140)))
df2 = df2.assign(a200 =(roag*3*(10**(12))/(df2['R(Ohm) - 200nm']*200)))
df2 = df2.assign(a260 = (roag*3*(10**(12))/(df2['R(Ohm) - 260nm']*260)))
df2.rename(columns = {'a140': 'a(nm) - 140nm', 'a200': 'a(nm) - 200nm', 'a260': 'a(nm) - 260nm'}, inplace = True)

## Cálculo da média do parâmetro a
mean140 = df2['a(nm) - 140nm'].mean()
mean200 = df2['a(nm) - 200nm'].mean()
mean260 = df2['a(nm) - 260nm'].mean()

## Cálculo do parâmetro de correlaçao para corrente x tensão de cada espessura
corr140 = df2['I(mA)'].corr(df2['V(mV) - 140nm'])
corr200 = df2['I(mA)'].corr(df2['V(mV) - 200nm'])
corr260 = df2['I(mA)'].corr(df2['V(mV) - 260nm'])

print('Suas respectivas médias de largura do canal são: {:2f} para 140nm, {:2f} para 200nm e {:2f} para 260nm'.format(mean140,mean200,mean260))
print('Os valores de corr para cada espessura são: {:2f} para 140nm, {:2f} para 200nm e {:2f} para 260nm'.format(corr140,corr200,corr260))

## Declaração dos eixos do gráfico de Tensão x Corrente
x = df2.iloc[:,0]
y140 = df2.iloc[:,1]
y200 = df2.iloc[:,3]
y260 = df2.iloc[:,5]

## Gráfico Tensão x Corrente
plt.plot(x, y140, 'o-', x, y200, 'o-', x, y260, 'o-')
plt.xlabel('Corrente(mA)')
plt.ylabel('Tensão(mV)')
plt.savefig('graph.png')
plt.title('Tensão x Corrente')
plt.show()
