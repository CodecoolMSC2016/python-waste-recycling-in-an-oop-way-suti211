from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:

    color = ""
    paper_content = []
    plastic_content = []
    house_waste_content = []

    def __init__(self, color):
        self.color = color
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []

    def throw_out_garbage(self, garbage):

        if (isinstance(garbage, PlasticGarbage)):
            if garbage.get_is_clean():
                self.plastic_content.append(garbage.get_name())
                return
            else:
                raise DustbinContentError("The garbage is dirty!(:D)")

        if (isinstance(garbage, PaperGarbage)):
            if garbage.get_squeezed():
                self.paper_content.append(garbage.get_name())
                return
            else:
                raise DustbinContentError(
                    "The paper garbage isn't squeezed!")

        if(isinstance(garbage, Garbage)):
            self.house_waste_content.append(garbage.get_name())
        else:
            raise DustbinContentError(
                "The garbage didn't fit in nowhere :(")

    def empty_contents(self):
        self.house_waste_content = []
        self.paper_content = []
        self.plastic_content = []
