import yaml

data = {
    "name": "Mike",
    "age": 25,
    "languages": ["Python", "C", "Java"],
    "address": {
        "city": "NYC",
        "ZIP": "1234",
        "country": "US" 
    }
}


with open("somefile.yml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)