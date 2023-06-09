#!/usr/bin/env python3
""" MRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Creates a class LRU that inherits form BaseCaching
    """

    def __init__(self):
        """ Initialize from the parent class
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Must assign to the dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """ Return the value
        """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
