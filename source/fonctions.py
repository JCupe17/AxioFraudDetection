import re
from unidecode import unidecode

def format_column_name(name):
    """Format a string that will be used as a column name
    """
    name = re.sub(r"(\.|°)", "", name)  # Changer les spaces par ""
    name = unidecode(name)  # Supprimer les caractères spéciaux
    name = name.lower()  # Passer les noms en minuscule
    name = re.sub(r"(\s)", "_", name)  # Changer les spaces par ""
    return name
