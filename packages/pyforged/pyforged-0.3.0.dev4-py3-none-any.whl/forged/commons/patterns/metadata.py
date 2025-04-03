import datetime
from typing import Any

from loguru import logger
from omegaconf import OmegaConf

class Metadata:
    """
    Metadata class to store information about the dataset.
    """

    def __init__(self, instance_set: bool = False, **kwargs):
        """
        Initialize the metadata object.

        :param kwargs: Key-value pairs for metadata.
        """

        #
        self._metad = OmegaConf.create({})
        if kwargs:
            for key, value in kwargs.items():
                if isinstance(value, dict):
                    self._metad[key] = OmegaConf.create(value)
                else:
                    self._metad[key] = value
        logger.debug(f"Added {len(kwargs) if len(kwargs) > 0 else ''} metadata {'items ' if len(kwargs) > 0 else ''}to the object.")
        self._frozen_meta = False

        if instance_set:
            self._metad._instance = {
                "type": self.__class__.__name__,  # TODO: Fix it to use best name
                "created_at": str(datetime.datetime.now()),
                "version": "1.0"
            }

    @property
    def metadata(self):
        return self._metad

    def add_metadata(self, key: str, value: Any) -> None:
        """
        Add metadata to the dataset.

        :param key: The key for the metadata.
        :param value: The value for the metadata.
        """
        if self._frozen_meta:
            raise ValueError("Cannot modify frozen metadata.")

        self._metad[key] = value

    def get_metadata(self, key: str, default: Any = None) -> any:
        """
        Get metadata from the dataset.

        :param key: The key for the metadata.
        :param default: The value if the key is not found. Raises an error if not provided.
        :return: The value for the metadata.
        :raises KeyError: If the key is not found and default is not provided.
        """

        if key in self._metad:
            return self._metad[key]
        elif default is not None:
            return default
        else:
            raise KeyError(f"Metadata key '{key}' not found.")

    def update_metadata(self, key: str, value: any, create_new: bool = True) -> None:
        """
        Update metadata in the dataset.

        :param key: The key for the metadata.
        :param value: The new value for the metadata.
        :param create_new: If True, create a new key if it doesn't exist.
        """
        if self._frozen_meta:
            raise ValueError("Cannot modify frozen metadata.")

        if key in self._metad:
            self._metad[key] = value
        else:
            if create_new:
                self._metad[key] = value
            else:
                logger.warning(f"Metadata key '{key}' not found. No action taken.")

    def remove_metadata(self, key: str) -> None:
        """
        Remove metadata from the dataset.

        :param key: The key for the metadata to remove.
        """
        if self._frozen_meta:
            raise ValueError("Cannot modify frozen metadata.")

        if key in self._metad:
            del self._metad[key]
        else:
            logger.warning(f"Metadata key '{key}' not found. No action taken.")


    def clear_metadata(self) -> None:
        """
        Clear all metadata from the dataset.
        """
        if self._frozen_meta:
            raise ValueError("Cannot modify frozen metadata.")

        self._metad.clear()

    def freeze_metadata(self, fallover: bool = False) -> None:  # TODO: Ensure compatibility with OmegaConf dot notation access
        """
        Freeze the metadata to prevent further modifications.

        :param fallover: If True, raises an error if metadata is already frozen.
        :raises ValueError: If metadata is already frozen and fallover is True.
        """
        if self._frozen_meta:
            if fallover:
                raise ValueError("Metadata is already frozen. Cannot freeze again.")
            else:
                logger.debug(f"Metadata is already frozen. Ignoring freeze request.")
        else:
            self._frozen_meta = True

    def unfreeze_metadata(self):
        """
        Unfreeze the metadata to allow modifications.
        """
        if not self._frozen_meta:
            logger.warning(f"Metadata is not frozen. Cannot unfreeze.")

        self._frozen_meta = False

    def as_dict(self) -> dict:
        """
        Returns a standard dictionary representation of the metadata.
        """
        return OmegaConf.to_container(self._metad, resolve=True)

    def merge_metadata(self, update_dict: dict) -> None:
        """
        Merge a given dictionary into the metadata.

        :param update_dict: A dictionary to merge into the metadata.
        """
        if self._frozen_meta:
            raise ValueError("Cannot modify frozen metadata.")

        # Merge the update_dict into _metad; OmegaConf supports merging.
        self._metad = OmegaConf.merge(self._metad, OmegaConf.create(update_dict))

    def to_yaml(self) -> str:
        """
        Serialize the metadata to a YAML formatted string.
        """
        return OmegaConf.to_yaml(self._metad)

    def to_json(self) -> str:
        """
        Serialize the metadata to a JSON formatted string.
        """
        import json
        return json.dumps(OmegaConf.to_container(self._metad, resolve=True), indent=2)


def apply_metadata_mixin(target_obj, instance_set: bool = False, **kwargs):
    """
    Mixin to add metadata functionality to any object.

    :param target_obj: The object to which metadata functionality is added.
    :param kwargs: Initial metadata as key-value pairs.
    :returns: None
    """
    # Create a new class that inherits from both the target object's class and Metadata
    new_class = type('Mixed' + target_obj.__class__.__name__, (target_obj.__class__, Metadata), {})
    target_obj.__class__ = new_class
    # Initialize the Metadata part of the new class with kwargs
    Metadata.__init__(target_obj, **kwargs)



if __name__ == '__main__':
    # Example usage
    class ExampleClass:
        pass

    class SecondExample(Metadata()):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

    example_instance = ExampleClass()
    apply_metadata_mixin(example_instance, instance_set=True)

    # Now example_instance has metadata methods and properties
    print(example_instance.metadata)
    print(isinstance(example_instance, Metadata))  # True

    example_instance.add_metadata('key1', 'value1')

    print(example_instance.metadata.key1)
    print(example_instance.metadata)
