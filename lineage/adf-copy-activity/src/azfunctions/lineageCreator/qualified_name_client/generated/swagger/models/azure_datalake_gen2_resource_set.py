# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureDatalakeGen2ResourceSet(Model):
    """AzureDatalakeGen2ResourceSet.

    :param azure_storage_uri:
    :type azure_storage_uri: str
    :param filesystem_name:
    :type filesystem_name: str
    :param resource_set_path:
    :type resource_set_path: str
    """

    _attribute_map = {
        'azure_storage_uri': {'key': 'azure_storage_uri', 'type': 'str'},
        'filesystem_name': {'key': 'filesystem_name', 'type': 'str'},
        'resource_set_path': {'key': 'resource_set_path', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureDatalakeGen2ResourceSet, self).__init__(**kwargs)
        self.azure_storage_uri = kwargs.get('azure_storage_uri', None)
        self.filesystem_name = kwargs.get('filesystem_name', None)
        self.resource_set_path = kwargs.get('resource_set_path', None)
