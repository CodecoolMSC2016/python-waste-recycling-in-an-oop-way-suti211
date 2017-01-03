from garbage import Garbage


class PlasticGarbage(Garbage):

    def __init__(self, name, is_clean):
        super().__init__(name)
        self._is_clean = is_clean

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_is_clean(self):
        return self._is_clean

    def clean(self):
        self._is_clean = True
