import importlib

_datasets_info = {
    'california_housing': {
        'size': {'train': 6880, 'val': 6880, 'test': 6880, 'shard': 2000},
    }
}

from . import ds

#__import__('.ds.california_housing')

print(1)

#def _update_info(dataset_name):
#  _datasets_info[dataset_name]['info'] = __import__(dataset_name + '.py').get_features()

# class Dataset:
#   def __init__(name):
#     info = _datasets_info[name]