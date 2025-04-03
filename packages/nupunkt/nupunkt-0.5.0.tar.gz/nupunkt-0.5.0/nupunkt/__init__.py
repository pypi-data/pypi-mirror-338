"""
nupunkt is a Python library for sentence boundary detection based on the Punkt algorithm.

It learns to identify sentence boundaries in text, even when periods are used for
abbreviations, ellipses, and other non-sentence-ending contexts.
"""

__version__ = "0.5.0"

# Core classes
# Import for type annotations
from typing import List

from nupunkt.core.language_vars import PunktLanguageVars
from nupunkt.core.parameters import PunktParameters
from nupunkt.core.tokens import PunktToken

# Models
from nupunkt.models import load_default_model

# Tokenizers
from nupunkt.tokenizers.sentence_tokenizer import PunktSentenceTokenizer

# Trainers
from nupunkt.trainers.base_trainer import PunktTrainer


# Function for quick and easy sentence tokenization
def sent_tokenize(text: str) -> List[str]:
    """
    Tokenize text into sentences using the default pre-trained model.

    This is a convenience function for quick sentence tokenization
    without having to explicitly load a model.

    Args:
        text: The text to tokenize

    Returns:
        A list of sentences
    """
    tokenizer = load_default_model()
    return tokenizer.tokenize(text)


__all__ = [
    "PunktParameters",
    "PunktLanguageVars",
    "PunktToken",
    "PunktTrainer",
    "PunktSentenceTokenizer",
    "load_default_model",
    "sent_tokenize",
]
