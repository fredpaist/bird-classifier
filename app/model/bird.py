class Bird:
    __id: int
    __name: str
    __score: float

    def __init__(self, bird_id, name):
        self.id = bird_id
        self.name = name
        self.score = 0

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, bird_id: int):
        self.__id = bird_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def score(self) -> float:
        return self.__score

    @score.setter
    def score(self, score: float):
        self.__score = score

    def __str__(self):
        return '"%s" with score: %s' % (self.name, self.score)
