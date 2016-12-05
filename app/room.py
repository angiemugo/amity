class Room:

    def __init__(self, room_name, room_type, max_occupants):
        self.room_name = room_name
        self.room_type = room_type
        self.max_occupants = max_occupants


class Office:
    def __init__(self, room_name, max_occupants):
        super(Office, self).__init__(room_name, max_occupants=6)


class Livingspace:
    def __init__(self, room_name, max_occupants):

        super(Livingspace, self).__init__(room_name, max_occupants=4)

        self.room_name = room_name
