import hashlib

class ClubType:
    def __init__(self, name, drink_type, music_type):
        self.name = name
        self.drink_type = drink_type
        self.music_type = music_type

    def draw(self, city, x, y, z):
        print(f"Draw club at {x, y, z} on {city}")

class Club:
    def __init__(self, x, y, z, type_: ClubType):
        self.x = x
        self.y = y
        self.z = z
        self.type_ = type_

    def draw(self, city):
        self.type_.draw(city, self.x, self.y, self.z)

class ClubFactory:
    _club_types = {}

    def get_club_type(self, name, drink_type, music_type):
        key = self._get_key(name, drink_type, music_type)
        if not self._club_types.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._club_types[key] = ClubType(name, drink_type, music_type)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._club_types[key]

    def _get_key(self, name, drink_type, music_type):
        key = "_".join([name, drink_type, music_type])
        bytes_key =  bytes(key, 'utf-8') 
        return hashlib.sha256(bytes_key).hexdigest()




class ClubCity:
    clubs = []

    def create_club(self, x, y, z, name, drink_type, music_type):
        type_ = ClubFactory().get_club_type(name, drink_type, music_type)
        club = Club(x, y, z, type_)
        self.clubs.append(club)

    def draw(self, city):
        for club in self.clubs:
            club.draw(city)


if __name__ == "__main__":
    forest = ClubCity()

    forest.create_club(1, 1, 1, "Spartak's club", "alcoholic", "irish")

    forest.draw("moscow")

    forest.create_club(1, 2, 1, "Mark's club", "non alcoholic", "irish")

    forest.draw("moscow")

    forest.create_club(1, 2, 3, "Spartak's club", "alcoholic", "irish")


    forest.draw("moscow")