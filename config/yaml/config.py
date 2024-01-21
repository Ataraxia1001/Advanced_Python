import yaml

with open("config.yml", "r") as f:
    data = yaml.safe_load(f)

print(data)