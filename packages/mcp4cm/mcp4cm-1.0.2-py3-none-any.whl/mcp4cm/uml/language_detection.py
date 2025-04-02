from collections import defaultdict
from langdetect import detect, DetectorFactory

from mcp4cm.uml.dataloading import UMLDataset, UMLModel


def process_file(model: UMLModel) -> str:
    """
    Process a single model to detect its language.
    
    This function uses langdetect to identify the language of the text content
    in a UML model.
    
    Args:
        model (UMLModel): The model to process for language detection.
        
    Returns:
        str: ISO 639-1 language code (e.g., 'en' for English, 'fr' for French),
             or None if the model has no text content or detection fails.
    """
    if model.model_txt and model.model_txt.strip():  # Ensure it's not empty or whitespace
        return detect(model.model_txt)
    return None


def detect_dataset_languages(dataset: UMLDataset) -> dict:
    """
    Detect the language of each model in the dataset.
    
    This function analyzes all models in the dataset and categorizes them
    by their detected language. It also prints a summary of language distribution.
    
    Args:
        dataset (UMLDataset): The dataset containing UML models.
    
    Returns:
        dict: A dictionary where keys are language codes (e.g., 'en', 'fr') and 
              values are lists of UMLModel objects in that language.
              
    Example:
        >>> languages = detect_dataset_languages(dataset)
        >>> print(f"Found {len(languages['en'])} English models")
    """
    DetectorFactory.seed = 0  # Set seed for reproducibility
    language_dict = defaultdict(list)
    
    for model in dataset.models:
        if model.model_txt is None:
            continue
        lang = process_file(model)
        if lang:
            language_dict[lang].append(model)
    
    print("Language Distribution Across Models:")
    for lang, models in language_dict.items():
        print(f"Language: {lang}, Count: {len(models)}")
    
    return language_dict

def extract_non_english_models(dataset: UMLDataset) -> UMLDataset:
    """
    Extract non-English models from the dataset.
    
    This function creates a new dataset containing only models whose text
    content is not in English. This is useful for filtering out non-English
    models for language-specific analysis or cleaning.
    
    Args:
        dataset (UMLDataset): The dataset containing UML models.
    
    Returns:
        UMLDataset: A new dataset containing only non-English models.
        
    Example:
        >>> non_english = extract_non_english_models(dataset)
        >>> print(f"Found {len(non_english.models)} non-English models")
    """
    non_english_models = []
    
    for model in dataset.models:
        if model.model_txt is None:
            continue
        lang = process_file(model)
        if lang and lang != 'en':
            non_english_models.append(model)
    
    return UMLDataset(name=dataset.name, models=non_english_models)

