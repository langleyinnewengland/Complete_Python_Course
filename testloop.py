import yaml
a_yaml_file = open("11_9_swagger.yaml")
#asssigns the contact to yamlfile
yamlfile = yaml.load(a_yaml_file, Loader= yaml.FullLoader)
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