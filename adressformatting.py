import pandas as pd
import numpy

class formatAddress():
  def __init__(self, path):
    self.path = path
    self.df = pd.read_excel(self.path)
    self.concatdf = pd.DataFrame()
    
  def formatSheet(self, dataframe):
    dataframe['CAIXA'] = '(' + dataframe['CAIXA'] + ')'
    return dataframe

  def concatAdressBoxes(self, row):
    if pd.notnull(row['CAIXA']) and row['CAIXA']!= '':
      return str(row['ENDEREÇO']) + ' ' + str(row['CAIXA'])
    else: 
      return str(row['ENDEREÇO'])
  
  def concatCodes(self, group):
    return ' / '.join(group['ENDEREÇO'])
  
  def formatedFile(self):
    self.df = self.formatSheet(self.df)
    self.df['ENDEREÇO'] = self.df.apply(self.concatAdressBoxes, axis=1)
    concatdf = self.df.groupby('CODIGO').apply(self.concatCodes).reset_index(name="ENDEREÇOS_CONCATENADOS")
    concatdf.to_excel("EndereçoFormatadoCG.xlsx", index=False)


""" formatFile = formatAddress(path)
formatFile.formatedFile() """
""" dff = formatSheet(adress)
dff['ENDEREÇO'] = dff.apply(concatAdressBoxes, axis=1)
dfconcat = dff.groupby('CODIGO').apply(concatCodes).reset_index(name='endereços_concatenados')

dfconcat.to_excel("EnderecoFormatadoCG.xlsx", index=False) """