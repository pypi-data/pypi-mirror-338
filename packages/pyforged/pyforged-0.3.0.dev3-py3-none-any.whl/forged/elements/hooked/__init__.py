"""
The `hooked` subpackage provides a system for managing and executing hooked within the application.

Hooks are a way to allow custom code to be executed at specific points in the application lifecycle. This subpackage includes utilities for defining, registering, and invoking hooks.

Modules:
    - `__init__.py`: Initializes the hooked subpackage.


Usage:
    To use the hooks system, import the necessary functions and classes from this subpackage and define your hooks as needed.


Example:

    from forged.elements.hooked import register_hook, execute_hook

    def my_custom_hook():
        print("Custom hook executed!")

    register_hook('my_hook', my_custom_hook)
    execute_hook('my_hook')
    ```

"""