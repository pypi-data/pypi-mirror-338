import yaml
import os
from utilsme.model_format import CsvDataModel, ColumnModel
from pydantic import ValidationError


def load_yaml_data_model(model_path) -> dict:
    """
    Load the data model from a YAML file.
    """
    # Check if the file exists and is readable
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model file {model_path} not found.")
    
    # Load the YAML file
    try:
        with open(model_path, 'r') as model:
            yaml_model = yaml.safe_load(model)
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
    
    # Validate the loaded data model
    try:
        data_model = CsvDataModel(**yaml_model)
    except ValidationError as e:
        raise ValueError(f"Validation error in data model: {e}")
    
    data_model_dict = data_model.model_dump(exclude_unset=True)
    return data_model_dict
