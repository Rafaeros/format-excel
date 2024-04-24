import pandas as pd
import numpy

path = './address.xlsx'

adress = pd.read_excel(path)
#adress['CAIXA'] = '(' + adress['CAIXA'] + ')'
#dataframe['ENDEREÇO'] = dataframe['ENDEREÇO'] + " " + dataframe['CAIXA']

def formatSheet(dataframe):
  dataframe['CAIXA'] = '(' + dataframe['CAIXA'] + ')'
  return dataframe

def concatAdressBoxes(row):
  if pd.notnull(row['CAIXA']) and row['CAIXA']!= '':
    return str(row['ENDEREÇO']) + ' ' + str(row['CAIXA'])
  else: 
    return str(row['ENDEREÇO'])
  
def concatCodes(group):
  return ' / '.join(group['ENDEREÇO'])

dff = formatSheet(adress)
dff['ENDEREÇO'] = dff.apply(concatAdressBoxes, axis=1)
dfconcat = dff.groupby('CODIGO').apply(concatCodes).reset_index(name='endereços_concatenados')

dfconcat.to_excel("EnderecoFormatadoCG.xlsx", index=False)