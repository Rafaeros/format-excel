import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from adressformatting import formatAddress

class interface():
  def __init__(self, master):
    self.master = master
    self.master.resizable(False, False)
    self.master.geometry("400x200")
    self.master.title("Formatador de endereço para o CG")
    self.dataError = ["CODIGO", "ENDEREÇO", "CAIXA"]
    self.dataErrorList = []
    self.selectFileButton = ctk.CTkButton(master, text="Selecionar Arquivo", command=self.selectFile)
    self.selectFileButton.pack(pady=20)
    self.fileName = ""

    self.fileNameLabel = ctk.CTkLabel(master, text="Arquivo Selecionado: ____")
    self.fileNameLabel.pack(pady=20)

    self.generateButton = ctk.CTkButton(master, text="Formatar", command=self.generateFormatedFile)
    self.generateButton.pack(pady=20)

  def selectFile(self):
    self.filepath = ctk.filedialog.askopenfilename(filetypes=[("Arquivos de Excel", "*.xlsx")])
    self.filepath = "".join(self.filepath)
    self.getFileName(self.filepath)
    self.fileNameLabel.configure(text=f"Arquivo Selecionado: {self.fileName}")
    if(self.filepath!=""):
      selectedFile = CTkMessagebox(self.master, message=f"Arquivo Selecionado: {self.fileName}", option_1="OK")
      selectedFile.wait_window()
      self.formatedFile = formatAddress(self.filepath)
      df = self.formatedFile.df

      self.dataValidation(df)

      if(self.dataErrorList!=[]):
        self.dataValidationWarn()
        self.filepath=""
        self.fileNameLabel.configure(text="Arquivo Selecionado: ____")
        self.dataErrorList.clear()
    else:
      emptyFilePath = CTkMessagebox(title="Nenhum Arquivo Selecionado:", message="Selecione um Arquivo!", option_1="OK")

  def generateFormatedFile(self):
    if(self.filepath!="" and self.dataErrorList == []):
      generate = formatAddress(self.filepath)
      generate.formatedFile()
      generatedMessage = CTkMessagebox(self.master,message="Arquivo Gerado: EndereçoFormatadoCG.xlsx")
    else:
      validFile = CTkMessagebox(self.master, message="Selecione um Arquivo Válido!", title="Erro", option_1="OK")
    
  def getFileName(self, path):
    splitFilePath = path.split('/')
    splitLen = len(splitFilePath)-1
    self.fileName = splitFilePath[splitLen]

  def dataValidationWarn(self):
    if self.dataErrorList != []:
        errorListWarn = ", ".join(self.dataErrorList)
        missingColumns = CTkMessagebox(title="Erro: Planilha sem as colunas necessárias", message=f"Colunas não encontradas: {errorListWarn}")

  def dataValidation(self, datalist):
    for error in self.dataError:
      if error in datalist.columns:
        pass
      else:
        self.dataErrorList.append(error)