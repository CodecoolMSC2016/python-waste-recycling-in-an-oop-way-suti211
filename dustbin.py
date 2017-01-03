from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:

    def __init__(self, color, paper_content, plastic_content, house_waste_content):
        self._color = color
        self._paper_content = paper_content
        self._plastic_content = plastic_content
        self._house_waste_content = house_waste_content

    def throw_out_garbage(garbage):
        if isinstance(garbage, PlasticGarbage):
            if garbage.get_is_clean():
                self._plastic_content.append(garbage.get_name())
            else:
                raise DustbinContentError("The garbage is dirty!(:D)")

        if isinstance(garbage, PaperGarbage):
            if garbage.get_squeezed():
                self._paper_content.append(garbage.get_name())
            else:
                raise DustbinContentError.append("The garbage isn't squeezed!")
