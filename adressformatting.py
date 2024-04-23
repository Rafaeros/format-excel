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
  
formatedS = formatSheet(adress)
formatedS['CONCATENADO'] = formatedS.apply(concatAdressBoxes, axis=1)

print(formatedS)

formatedS.to_excel("formated.xlsx", index=(False))
