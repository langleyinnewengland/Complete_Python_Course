import yaml
filename = input("What YAML file would you like to open?: ")
info = input("what information would you like to list (t)ags or (d)escriptionn?"
a_yaml_file = open(filename)
#asssigns the contact to yamlfile
yamlfile = yaml.load(a_yaml_file, Loader= yaml.FullLoader)

#assign components of file to variables
description = yamlfile['info']['description']
tags = yamlfile['tags']
specifictags = yamlfile['tags'][0]['name']
paths=yamlfile['paths']['/cff/app/api/accountbalances/']
method=yamlfile['paths']['/cff/app/api/accountbalances/']['delete']
responses=yamlfile['paths']['/cff/app/api/accountbalances/']['delete']['responses']
teser=yamlfile['paths']
print(responses)




#print(f"paths = {paths}")
#print(f"tester = {teser}")
print(responses)
#for i in range(0, 20):
#tags=yamlfile['tags'][i]['name']
#des=yamlfile['tags'][i]['description']
#method=
#print(f"Name: {tags}")
#print (f"Description: {des}")