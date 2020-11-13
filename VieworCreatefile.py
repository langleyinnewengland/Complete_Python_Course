import yaml
a_yaml_file = open("11_9_swagger.yaml")
#asssigns the contact to yamlfile
yamlfile = yaml.load(a_yaml_file, Loader= yaml.FullLoader)

def choice():
    menuchoice = input("Would you like to (o) open or (c) create: ")
    if (menuchoice == 'o'):
        openfile()
    elif (menuchoice == 'c'):
        namefile()

def namefile():
    description = yamlfile['info']['description']
    namefile = input ("What is the name of the file to create?:")
    #open in "w" mode creates new file, "a" is append
    with open(namefile, "w") as myfile:
        myfile.write(description)
        myfile.close()
        choice()

def openfile():
    whatfile = input ("what file would you like to open?: ")
    with open(whatfile, 'r') as readfile:
        print(readfile.read())
        choice()


choice()