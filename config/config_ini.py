from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

print(config.sections())
print(config['account'])
print(list(config['account']))

print(config['account']['pin'])

config.add_section('bank')
config.set('bank', 'name', 'hsbc')

with open(file, 'w') as configfile:
    config.write(configfile)
