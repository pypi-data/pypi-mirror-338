"""
Providing the main classes and functions for creating and managing **namespaces**.

Including:
    - **Namespace**:  *The primary class for creating and managing namespaces.*
    - **CompositeNamespace**:  *A class for combining multiple namespaces into a single namespace.*
"""
from forged.elements.named.core.namespace import Namespace
from forged.elements.named.composite import CompositeNamespace
from forged.elements.named.utils import *

__all__ = ["Namespace", "CompositeNamespace", "validate_path"]