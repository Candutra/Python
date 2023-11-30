import os

os.system("cls")
lst = os.listdir("C:/")
count = 1
for i in lst:
    print(str(count)+"º - "+i)
    count+=1

esc = input("Digite o número correspondente a pasta que deseja ver: ")

match esc:
    case "1":
        print(os.listdir("c:/$Recycle.Bin"))
    case "2":
        print(os.listdir("c:/$WinREAgent"))
    case "3":
        print(os.listdir("c:/A506087AD475"))
    case "4":
        print(os.listdir("c:/Arquivos de Programas"))
    case "5":
        print(os.listdir("c:/Ativar_Pacote_Office_Visio_Project.bat"))
    case "6":
        print(os.listdir("c:/Documents and Settings"))
    case "7":
        print(os.listdir("c:/DumpStack.log.tmp"))
    case "8":
        print(os.listdir("c:/eclipse"))
    case "9":
        print(os.listdir("c:/HashiCorp"))
    case "10":
        print(os.listdir("c:/hiberfil.sys"))
    case "11":
        print(os.listdir("c:/Intel"))
    case "12":
        print(os.listdir("c:/npm"))
    case "13":
        print(os.listdir("c:/OneDriveTemp"))
    case _:
        print("Diretorio não localizado")