"""
Interface for the program
"""

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from adressformatting import FormatAddress


class Interface(ctk.CTk):
    """
    Interface class for the program
    """

    def __init__(self) -> None:
        """
        Initializes the class interface
        """
        super().__init__()
        self.resizable(False, False)
        self.geometry("600x400")

        self.title("Formatador de endereço para o CG")
        self.data_error: list[str] = ["CODIGO", "ENDEREÇO", "CAIXA"]
        self.data_error_list: list = []
        self.file_name: str = ""
        self.file_path: str = ""
        self.formated_file: FormatAddress = None

        self.select_file_button = ctk.CTkButton(
            self, text="Selecionar Arquivo", command=self.select_file)
        self.select_file_button.pack(pady=20)

        self.file_name_label = ctk.CTkLabel(
            self, text="Arquivo Selecionado: ____")
        self.file_name_label.pack(pady=20)

        self.generate_file_button = ctk.CTkButton(
            self, text="Formatar", command=self.generate_formated_file)
        self.generate_file_button.pack(pady=20)

    def select_file(self) -> None:
        """
        Selects the file function
        """
        self.file_path = ctk.filedialog.askopenfilename(
            filetypes=[("Arquivos de Excel", "*.xlsx")])
        self.file_path = "".join(self.file_path)
        self.get_file_name(self.file_path)
        self.file_name_label.configure(
            text=f"Arquivo Selecionado: {self.file_name}")
        if self.file_path != "":
            selected_file = CTkMessagebox(self, message=f"Arquivo Selecionado: {
                self.file_name}", option_1="OK")
            selected_file.wait_window()
            self.formated_file = FormatAddress(self.file_path)
            df = self.formated_file.df

            self.data_validation(df)

            if self.data_error_list:
                self.data_validation_warn()
                self.file_path = ""
                self.file_name_label.configure(
                    text="Arquivo Selecionado: ____")
                self.data_error_list.clear()
        else:
            CTkMessagebox(
                title="Nenhum Arquivo Selecionado:", message="Selecione um Arquivo!", option_1="OK")

    def generate_formated_file(self) -> None:
        """
        Generates the formated file
        """
        if self.file_path != "" and not self.data_error_list:
            generate = FormatAddress(self.file_path)
            generate.formated_file()
            CTkMessagebox(
                self.master, message="Arquivo Gerado: EndereçoFormatadoCG.xlsx")
        else:
            CTkMessagebox(
                self.master, message="Selecione um Arquivo Válido!", title="Erro", option_1="OK")

    def get_file_name(self, path) -> None:
        """
        Gets the file name
        """
        split_file_path = path.split('/')
        split_len = len(split_file_path)-1
        self.file_name = split_file_path[split_len]

    def data_validation_warn(self) -> None:
        """
        Warns if the columns are not in the file
        """
        if self.data_error_list:
            error_list_warn: str = ", ".join(self.data_error_list)
            CTkMessagebox(
                title="Erro: Planilha sem as colunas necessárias",
                message=f"Colunas não encontradas: {error_list_warn}")

    def data_validation(self, datalist) -> None:
        """
        Verifies if the columns exist in the file
        """
        for error in self.data_error:
            if error in datalist.columns:
                pass
            else:
                self.data_error_list.append(error)
