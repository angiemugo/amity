class RoomClass(object):

    def __init__(self, room_name=None, room_type=None, max_occupants=None,
                 occupants=None):
        self.room_name = room_name
        self.room_type = room_type
        self.occupants = occupants
        self.max_occupants = max_occupants


class Office:
    def __init__(self, room_name, room_type, occupants):
        super(Office, self).__init__(room_name,  occupants,room_type="office",
                                     max_occupants=6)


class Lspace:
    def __init__(self, room_name, room_type, occupants):
        super(Lspace, self).__init__(room_name, occupants, room_type="lspace",
                                     max_occupants=4)
#add lspace, office here
