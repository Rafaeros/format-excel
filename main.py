from interface import interface
import customtkinter as ctk
import CTkMessagebox

def main():
  root = ctk.CTk()
  app = interface(root)
  root.mainloop()

if __name__ == "__main__":
  main()