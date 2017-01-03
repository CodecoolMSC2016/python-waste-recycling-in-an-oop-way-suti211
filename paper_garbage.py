from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, name, is_squeezed):
        super().__init__(name)
        self._is_squeezed = False

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_squeezed(self):
        return self._is_squeezed

    def squeeze(self, squeezed):
        self._is_squeezed = squeezed
