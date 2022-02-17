class My_Exception(Exception):
    def __init__(self, exc: str):
        self.exc = exc



class Candidate:

    def __init__(self, item: dict):
        self.id: int = item['id']
        self.name: str = item['name']
        self.picture: str = item['picture']
        self.position: str = item['position']
        self.gender: str = item['gender']
        self.age: int = item['age']
        self.skills: str = item['skills']
