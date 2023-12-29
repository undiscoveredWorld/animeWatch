from models.anime import Anime


class INewAnime:
    @classmethod
    def get_elements(cls) -> list[Anime]:
        """
        Method must get elements from any source and return them in a list
        :return: list of navigation elements
        """
        pass


class NewAnimeFromList(INewAnime):
    elements: list[Anime] = []

    @classmethod
    def get_elements(cls) -> list[Anime]:
        result: list[Anime] = []
        for element in cls.elements:
            result.append(Anime(

            ))
