from enum import Enum
from pydantic import BaseModel
from typing import List, Optional, Union, Dict

class Model(BaseModel):
    """
    Base class for model objects.
    
    This class represents a single model within a dataset and contains
    common attributes shared by all model types.
    
    Attributes:
        id (str): Unique identifier for the model.
        file_path (str): Path to the model file on disk.
        hash (str): Hash value of the model for duplicate detection.
        model_json (Optional[Union[List, Dict]]): Model data in JSON format, if available.
        model_xmi (Optional[str]): Model data in XMI format, if available.
        model_txt (Optional[str]): Model data in plain text format, if available.
        category (Optional[str]): Category or classification of the model.
        tags (Optional[List[str]]): List of tags associated with the model.
    """
    id: str
    file_path: str
    hash: str
    model_json: Optional[Union[List, Dict]] = None
    model_xmi: Optional[str] = None
    model_txt: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None


class Dataset(BaseModel):
    """
    Base class for datasets.
    
    This class represents a collection of models and provides common
    attributes and methods for working with model datasets.
    
    Attributes:
        name (str): Name of the dataset.
        models (List[Model]): List of models contained in the dataset.
    """
    name: str
    models: List[Model]



class DatasetType(Enum):
    """
    Enum for different dataset types.
    
    This enumeration defines the valid dataset types that can be loaded
    by the library. Currently supports:
    
    - MODELSET: Standard model dataset format
    """
    MODELSET = "modelset"
