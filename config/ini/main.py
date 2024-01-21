from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

print(config.sections())
print(config['account'])
print(list(config['account']))

print(config['account']['pin'])
try:
    config.add_section('bank')
except:
    print('add_section was already done.')
    
config.set('bank', 'name', 'hsbc')

with open(file, 'w') as configfile:
    config.write(configfile)
