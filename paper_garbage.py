from garbage import Garbage


class PaperGarbage(Garbage):

    is_squeezed = False

    def __init__(self, name, is_squeezed):
        super().__init__(name)
        self.is_squeezed = is_squeezed

    def get_squeezed(self):
        return self.is_squeezed

    def squeeze(self):
        self.is_squeezed = True
