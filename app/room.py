class RoomClass(object):

    def __init__(self, room_name=None, room_type=None, max_occupants=None):
        self.room_name = room_name
        self.room_type = room_type
        self.max_occupants = max_occupants


class Office:
    def __init__(self, room_name, room_type):
        # super.__init__(room_name, room_type, max_occupants=6)
        super(Office, self).__init__(room_name, room_type, max_occupants=6)

class Lspace:
    def __init__(self, room_name, room_type):

        # super.__init__(room_name, room_type, max_occupants=4)
        super(Lspace, self).__init__(room_name, room_type, max_occupants=4)

