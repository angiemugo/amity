from .room import RoomClass, Lspace, Office
from .employee import PersonClass, Fellow, Staff
import random


class AmityClass:
    all_people = {}
    amity_rooms = {}
    amity_offices = {}
    amity_lspaces = {}
    office_allocations = []
    lspace_allocations = [a]
    available_lspaces = []
    available_offices = []

    def create_room(self, room_name,room_type):
        if room_name.upper in [room_name for room_name in AmityClass.amity_rooms]:
            print("Sorry, name already picked. Give it another shot!")
        else:
            if room_type.upper == "lspace":
                room = RoomClass.Lspace(room_name, room_type)
                self.amity_lspaces.append(room)
                self.amity_rooms.append(room)
            elif room_type.upper == "office":
                room = RoomClass.Office(room_name, room_type)
                self.amity_offices.append(room)
                self.amity_rooms.append(room)

            else:
                print("Only offices and living spaces here!")
                # def check_full_room(self):



    @staticmethod
    def generate_lspace():
        lspaces = [room for room in AmityClass.available_lspaces if room.room_type == "lSPACE"]
        for lspace in AmityClass.available_lspaces:
            if Lspace.occupants > Lspace.max_occupants:
                chosen_lspace = None
            else:
                chosen_room = random.choice(AmityClass.available_lspaces)
            return chosen_lspace

    @staticmethod
    def generate_office():
        offices = [room for room in AmityClass.available_offices if room.room_type == "office"]
        for office in AmityClass.available_offices:
            if Office.occupants > Office . max_occupants:
                chosen_office = None
            else:
                chosen_office = random.choice(AmityClass.available_offices)
            return chosen_office


    def create_person(self, person_name, person_description, wants_accommodation):
        allocated_office = AmityClass.generate_office
        AmityClass.office_allocations.append(person_name.upper + " " + person_description)
        print("congratulations,%S, you have been assigned to room %S" % (person_name, allocated_office))
        if person_description.upper == "fellow":
            person = PersonClass.Fellow(person_name, person_description)
            self.amity_fellows.append(person)
            self.all_people.append(person)
            if wants_accommodation == "y":
                allocated_lspace = AmityClass.generate_lspace()
                AmityClass.lspace_allocations.append(person_name.upper + " " + person_description.upper)
                print("congratulations,%S, you have been assigned to room %S"% (person_name, allocated_lspace))

        elif person_description.upper == "staff":
            person = PersonClass.Staff(person_name, person_description)
            self.amity_staff.append(person)
            self.amity_fellows.append(person)
        else:
            print("amity does not know you")

    def reallocate_person(self, person_name, person_description, new_room):
        if new_room in AmityClass.amity_lspaces:
            if person_name in AmityClass.amity_staff:
                print("sorry, staff cannot be assigned living spaces" )
            elif person_name in AmityClass.amity_fellows:
                if new_room.upper not in AmityClass.available_lspaces:
                    print("sorry, the room is not available")
                elif new_room.upper in AmityClass.available_lspaces:
                    reallocated_lspace = new_room
                    AmityClass.lspace_allocations.append(person_name.upper + " " + person_description.upper)
                    print("congratulations,%S, you have been re-assigned to room %S" % (person_name, reallocated_lspace))
                else:
                    print("The room you chose does not exist")
            else:
                print("sorry, amity does not know you")
        if new_room in AmityClass.amity_offices:
            if person_name in AmityClass:
                reallocated_office = new_room
                AmityClass.office_allocations.append(person_name.upper + " " + person_description.upper)
                print("congratulations,%S, you have been re-assigned to room %S" % (person_name, reallocated_office))
            elif person_name not in AmityClass:

                print("sorry,Amity does not know you")




    def load_people(self):
        pass

    def print_allocations(self):
        pass

    def print_unallocated(self):
        unallocated = []
        pass

    def print_all_rooms(self):
        pass

    def save_state(self):
        pass

    def load_state(self):
        pass
