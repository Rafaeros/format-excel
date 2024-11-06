"""
  Adress Formatting format the excel file concatenate the address of the codes.
"""

import pandas as pd

class FormatAddress():
    """
    Formats the excel file
    """

    def __init__(self, path: str) -> None:
        """
        Initializes the class
        """
        self.path: str = path
        self.df: pd.DataFrame = pd.read_excel(self.path)
        self.concatdf: pd.DataFrame = pd.DataFrame()

    def format_sheet(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Formats the sheet
        """
        dataframe['CAIXA'] = '(' + dataframe['CAIXA'] + ')'
        return dataframe

    def concat_adress_boxes(self, row) -> str:
        """
        Concatenates the address
        """
        if pd.notnull(row['CAIXA']) and row['CAIXA'] != '':
            return str(row['ENDEREÇO']) + ' ' + str(row['CAIXA'])
        else:
            return str(row['ENDEREÇO'])

    def concat_codes(self, group) -> str:
        """
        Concatenates the unique codes
        """
        unique_addresses = set(group['ENDEREÇO'])  # Remove duplicados
        return ' / '.join(unique_addresses)

    def formated_file(self) -> None:
        """
        Formats the excel file
        """
        self.df = self.format_sheet(self.df)
        self.df['ENDEREÇO'] = self.df.apply(self.concat_adress_boxes, axis=1)
        concatdf = self.df.groupby('CODIGO').apply(
            self.concat_codes).reset_index(name="ENDEREÇOS_CONCATENADOS")
        concatdf.to_excel("EndereçoFormatadoCG.xlsx", index=False)
