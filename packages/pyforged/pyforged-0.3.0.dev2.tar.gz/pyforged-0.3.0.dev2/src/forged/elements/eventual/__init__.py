"""
A lightweight abstraction layer for managing signals (events) and reactive streams, allowing you to plug in different
backends like PyDispatcher and RxPy under a unified interface
"""
from forged.elements.eventual.core.actions import Action
from forged.elements.eventual.core.activities import Activity
from forged.elements.eventual.core.context import scoped_context

__all__ = ["Action", "Activity", "scoped_context"]


