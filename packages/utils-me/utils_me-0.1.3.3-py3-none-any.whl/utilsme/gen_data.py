import random
import yaml
import os
from string import ascii_letters


def load_yaml_data_model(model_path) -> dict:
    """
    Load the data model from a YAML file.
    """
    # Check if the file exists and is readable
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model file {model_path} not found.")
    
    with open(model_path, 'r') as model:
        return yaml.safe_load(model)


def generate_data(data_model, nb_rows: int=10):
    
    data = {}
    data_settings = {}
    
    for key, values in data_model.items():
        if key == 'columns':
            for i in range(nb_rows):
                
                for col in values:
                    if col['name'] not in data.keys():
                        data[col['name']] = []
                    
                    if col['type'] == 'integer':
                        data[col['name']].append(gd.genInteger())
                    elif col['type'] == 'decimal':
                        data[col['name']].append(gd.genDecimal())
                    elif col['type'] == 'string':
                        data[col['name']].append(gd.genString())
                    elif col['type'] == 'boolean':
                        data[col['name']].append(gd.genBool())
                    
        else:
            data_settings[key] = values
    
    return data, data_settings

def genInteger(min: int=1, max: int=5) -> int:
    """
    Generate a random integer between min and max.
    """
    return random.randint(min, max)

def genDecimal(min: float=2, max: float=5) -> float:
    """
    Generate a random float between min and max.
    """     
    return random.uniform(min, max)

def genString(length: int=10) -> str:
    """
    Generate a random string of fixed length.
    """
    result = '' if length == 0 else ''.join(random.choice(ascii_letters) for i in range(length))
    return result

def genBool() -> bool:
    """
    Generate a random boolean value.
    """
    return random.choice([True, False])
