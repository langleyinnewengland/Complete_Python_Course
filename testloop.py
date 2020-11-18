import yaml
a_yaml_file = open("11_9_swagger.yaml")
#asssigns the contact to yamlfile
yamlfile = yaml.load(a_yaml_file, Loader= yaml.FullLoader)
description = yamlfile['info']['description']
tags = yamlfile['tags']
specifictags = yamlfile['tags'][0]['name']
for i in range(0, 20):
    tags=yamlfile['tags'][i]['name']
    des=yamlfile['tags'][i]['description']
    print(f"Name: {tags}")
    print (f"Description: {des}")