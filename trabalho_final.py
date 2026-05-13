# ============================================================
# Trabalho Final - Limpeza e Tratamento de Dados com Pandas
# ============================================================

import pandas as pd
import numpy as np

# ------------------------------------------------------------
# Passo 3 e 4 - Leitura do CSV e atribuição à variável
# ------------------------------------------------------------
df = pd.read_csv(
    'dados_exercicio.csv',
    sep=';',
    engine='python',
    encoding='utf-8'
)

# ------------------------------------------------------------
# Passo 5 - Verificar se os dados foram importados adequadamente
# ------------------------------------------------------------

# 5a. Informações gerais sobre o conjunto de dados
print("=== Informações gerais ===")
df.info(memory_usage='deep')

# 5b. Primeiras e últimas 5 linhas
print("\n=== Primeiras 5 linhas ===")
print(df.head())

print("\n=== Últimas 5 linhas ===")
print(df.tail())

# ------------------------------------------------------------
# Passo 6 - Criar cópia do conjunto de dados original
# ------------------------------------------------------------
df_copy = df.copy()

# ------------------------------------------------------------
# Passo 7 - Substituir valores nulos da coluna 'Calories' por 0
# ------------------------------------------------------------

# 7a. Substituição
df_copy['Calories'] = df_copy['Calories'].fillna(0)

# 7b. Verificar a mudança
print("\n=== Dados após substituir nulos de Calories por 0 ===")
print(df_copy.to_string())

# ------------------------------------------------------------
# Passo 8 - Tratar a coluna 'Date'
# ------------------------------------------------------------

# 8a. Substituir valores nulos de 'Date' por '1900/01/01'
df_copy['Date'] = df_copy['Date'].fillna('1900/01/01')

# 8b. Verificar a mudança
print("\n=== Dados após substituir nulos de Date por '1900/01/01' ===")
print(df_copy.to_string())

# 8c. Tentar converter 'Date' para datetime
# ATENÇÃO: este passo irá gerar um erro, pois '1900/01/01' não corresponde
# ao formato '%Y/%m/%d' dos demais registros (que usam aspas simples).
# O erro será tratado no passo 9.
try:
    df_copy['Date'] = pd.to_datetime(df_copy['Date'], format='%Y/%m/%d')
except Exception as e:
    print(f"\n[ERRO esperado no passo 8c]: {e}")

# ------------------------------------------------------------
# Passo 9 - Resolver o erro do valor '1900/01/01'
# ------------------------------------------------------------

# 9a. Substituir '1900/01/01' por NaN
df_copy['Date'] = df_copy['Date'].replace('1900/01/01', np.nan)

# 9b. Tentar novamente a conversão para datetime
# ATENÇÃO: este passo irá gerar um novo erro, pois o valor '20201226'
# (linha 26) não está no formato '%Y/%m/%d'. Será tratado no passo 10.
try:
    df_copy['Date'] = pd.to_datetime(df_copy['Date'], format='%Y/%m/%d')
except Exception as e:
    print(f"\n[ERRO esperado no passo 9b]: {e}")

# 9c. Verificar o estado atual dos dados
print("\n=== Dados após substituir '1900/01/01' por NaN ===")
print(df_copy.to_string())

# ------------------------------------------------------------
# Passo 10 - Corrigir o valor '20201226' para formato datetime
# ------------------------------------------------------------
df_copy['Date'] = df_copy['Date'].replace(
    '20201226',
    pd.to_datetime('20201226', format='%Y%m%d')
)

# ------------------------------------------------------------
# Passo 11 - Converter toda a coluna 'Date' para datetime
# ------------------------------------------------------------
df_copy['Date'] = pd.to_datetime(df_copy['Date'], format='%Y/%m/%d', errors='coerce')

print("\n=== Dados após conversão completa da coluna Date para datetime ===")
print(df_copy.to_string())

# ------------------------------------------------------------
# Passo 12 - Remover registros com valores nulos na coluna 'Date'
# ------------------------------------------------------------
df_copy = df_copy.dropna(subset=['Date'])

# ------------------------------------------------------------
# Passo 13 - Impressão final do DataFrame tratado
# ------------------------------------------------------------
print("\n=== DataFrame final após todas as transformações ===")
print(df_copy.to_string())

print("\n=== Informações finais do conjunto tratado ===")
df_copy.info(memory_usage='deep')
