Id = {'name':'李鑫','age':'18','height':'175','weigh':'120'}
print(Id)
Id['address'] = '北京'
Id['group'] = '汉'
print(Id)
Id.pop('group')
print(Id)
Id['age'] = '19'
print(Id)
print(Id['name'])
