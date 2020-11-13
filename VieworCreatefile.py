import yaml
a_yaml_file = open("11_9_swagger.yaml")
#asssigns the contact to yamlfile
yamlfile = yaml.load(a_yaml_file, Loader= yaml.FullLoader)
description = yamlfile['info']['description']
tags = yamlfile['tags']
specifictags = yamlfile['tags'][0]['name']

def choice():
    menuchoice = input("Would you like to (o) open or (c) create or a (append): ")
    if (menuchoice == 'o'):
        openfile()
    elif (menuchoice == 'c'):
        namefile()
    elif (menuchoice == 'a'):
        appendfile()
def namefile():

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

def appendfile():
    nameappendfile = input("What is the name of the file to append?:")
    whattoappend = input("What do you want to append? (d) description (t) tags or (s) specifc tags?: ")
    if (whattoappend) == 'd':
        with open(nameappendfile, "a") as myfile:
            myfile.write(description)
            myfile.close()
    elif (whattoappend) == 't':
        with open(nameappendfile, "a") as myfile:
            myfile.write(tags)
            myfile.close()
            choice()


choice()