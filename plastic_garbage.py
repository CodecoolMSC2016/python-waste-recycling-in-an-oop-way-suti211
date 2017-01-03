from garbage import Garbage


class PlasticGarbage(Garbage):

    is_clean = False

    def __init__(self, name, is_clean):
        super().__init__(name)
        self.is_clean = is_clean

    def get_is_clean(self):
        return self.is_clean

    def clean(self):
        self.is_clean = True
