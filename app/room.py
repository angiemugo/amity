class RoomClass(object):

    def __init__(self, room_name=None, room_type=None, max_occupants=None,
                 occupants=None):
        self.room_name = room_name
        self.room_type = room_type
        self.occupants = occupants
        self.max_occupants = max_occupants


class Office(RoomClass):
    def __init__(self, room_name, room_type):
        super(Office, self).__init__(room_name,  room_type="OFFICE",
                                     max_occupants=6, occupants=0)


class Lspace(RoomClass):
    def __init__(self, room_name, room_type):
        super(Lspace, self).__init__(room_name,  room_type="LSPACE",
                                     max_occupants=4, occupants=0)
#add lspace, office here
