import hashlib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from matplotlib import pyplot as plt
from mcp4cm.uml.dataloading import UMLDataset
import time

from mcp4cm.uml.filtering_patterns import TFIDF_DUPLICATE_THRESHOLD

def get_file_hash(file_path):
    """
    Compute a SHA-256 hash for the content of a file.
    
    This function reads a text file and generates a hash value based on its
    normalized content. The hash can be used for exact duplicate detection.
    
    Args:
        file_path (str): Path to the file to hash.
        
    Returns:
        str: SHA-256 hash value as a hexadecimal string, or None if an error occurs.
        
    Example:
        >>> hash_value = get_file_hash("path/to/model.txt")
        >>> print(f"File hash: {hash_value}")
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip().lower()  # Read and normalize text content
            return hashlib.sha256(content.encode()).hexdigest()  # Hash the content
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def detect_duplicates_by_hash(dataset: UMLDataset, hash_function=get_file_hash, inplace: bool=False, plt_fig: bool=False):
    """
    Detect duplicate UML models based on their hash values.
    
    This function identifies exact duplicates in a dataset by computing hash values
    for each model's content. It can optionally modify the dataset in-place to remove
    duplicates and visualize the duplicate distribution.
    
    Args:
        dataset (UMLDataset): The dataset containing UML models.
        hash_function (callable): Function to compute hash values. Defaults to get_file_hash.
        inplace (bool): If True, removes duplicates from the dataset. Defaults to False.
        plt_fig (bool): If True, displays a pie chart of unique vs. duplicate files. Defaults to False.
    
    Returns:
        tuple: A tuple containing:
            - List[UMLModel]: A list of unique UML models.
            - List[tuple]: A list of duplicate groups, where each group is a tuple of (original, duplicate).
    
    Example:
        >>> unique_models, duplicate_groups = detect_duplicates_by_hash(dataset, inplace=True)
        >>> print(f"Found {len(duplicate_groups)} duplicate groups")
    """
    hash_dict = {}
    duplicate_groups = []
    unique_files = []
    duplicate_files = []
    
    start_time = time.time()
    for model in dataset.models:
        if model.model_xmi is None:
            continue
        file_hash = hash_function(model.file_path)
        if file_hash is not None:
            if file_hash in hash_dict:
                duplicate_groups.append((hash_dict[file_hash], model))
                duplicate_files.append(model)
            else:
                hash_dict[file_hash] = model
                unique_files.append(model)
    
    end_time = time.time()
    print(f"Hashing and duplicate detection took {end_time - start_time:.2f} seconds.")
    print(f"Total files processed: {len(dataset.models)}")
    print(f"Total unique files: {len(unique_files)}")
    print(f"Total duplicate files: {len(duplicate_files)}")
    print(f"Duplicate groups: {len(duplicate_groups)}")
    
    if inplace:
        dataset.models = unique_files
    
    if plt_fig:
        labels = ['Unique Files', 'Duplicate Files']
        sizes = [len(unique_files), len(duplicate_files)]
        colors = ['green', 'red']

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
        plt.title("Proportion of Unique vs. Duplicate Files")
        plt.show()
    
    return unique_files, duplicate_groups


def tfidf_near_duplicate_detector(dataset: UMLDataset, threshold: float=TFIDF_DUPLICATE_THRESHOLD, inplace: bool=False, plt_fig: bool=False):
    """
    Detect near-duplicate UML models based on TF-IDF vectorization and cosine similarity.
    
    This function identifies near-duplicate models by computing TF-IDF vectors
    for model text content and measuring their cosine similarity. Models with
    similarity above the threshold are considered near-duplicates.
    
    Args:
        dataset (UMLDataset): The dataset containing UML models.
        threshold (float): The similarity threshold for considering two models as near-duplicates.
            Values range from 0 to 1, with 1 being identical. Defaults to TFIDF_DUPLICATE_THRESHOLD.
        inplace (bool): If True, removes near-duplicates from the dataset. Defaults to False.
        plt_fig (bool): If True, displays a pie chart of unique vs. near-duplicate files. Defaults to False.
    
    Returns:
        tuple: A tuple containing:
            - List[UMLModel]: A list of unique UML models.
            - List[tuple]: A list of near-duplicate groups, where each group is a tuple of (model1, model2).
    
    Example:
        >>> unique_models, near_duplicate_groups = tfidf_near_duplicate_detector(dataset, threshold=0.85)
        >>> print(f"Found {len(near_duplicate_groups)} near-duplicate groups with threshold {threshold}")
    """
    
    
    # Extract the text content from the models
    start_time = time.time()
    text_data = [model.model_txt for model in dataset.models if model.model_txt is not None]
    
    # Vectorize the text data using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(text_data)
    
    # Compute cosine similarity between all pairs of models
    cosine_similarities = cosine_similarity(tfidf_matrix)
    
    # Identify near-duplicate models based on the threshold
    duplicate_groups = []
    unique_files = []
    
    for i in range(len(cosine_similarities)):
        for j in range(i + 1, len(cosine_similarities)):
            if cosine_similarities[i][j] >= threshold:
                duplicate_groups.append((dataset.models[i], dataset.models[j]))
    
    print(f"Total near-duplicate groups: {len(duplicate_groups)}")
    end_time = time.time()
    print(f"TF-IDF duplicate detection took {end_time - start_time:.2f} seconds.")
    print("\n=== Dataset Statistics ===")
    print(f"Total files processed: {len(dataset.models)}")
    print(f"Total unique files: {len(set(dataset.models))}")
    print(f"Total near-duplicate files: {len(duplicate_groups)}")
    print(f"Duplicate groups: {len(duplicate_groups)}")

    
    if inplace:
        unique_files = [model for model in dataset.models if model not in [dup[1] for dup in duplicate_groups]]
        dataset.models = unique_files
    
    if plt_fig:
        labels = ['Unique Files', 'Near-Duplicate Files']
        sizes = [len(unique_files), len(duplicate_groups)]
        colors = ['green', 'red']

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
        plt.title("Proportion of Unique vs. Near-Duplicate Files")
        plt.show()
    
    return unique_files, duplicate_groups