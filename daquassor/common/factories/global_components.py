# Used instead of Zope, as getting objects / classes by key was the only feature of zope I used.
from typing import Dict, Any

component_classes: Dict[str, Any] = dict()
initialized_components: Dict[str, Any] = dict()
