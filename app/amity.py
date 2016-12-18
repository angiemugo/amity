

import random
from app.room import RoomClass
from app.employee import PersonClass


class Amity:
    all_people = []
    all_rooms = []
    amity_allocations = {"None" : []}
    amity_unallocated = []
    fellows_list = []
    staff_list = []
    lspace_list = []
    office_list = []

    def create_room(self, room_name, room_type):
        if room_name in Amity.all_rooms:
            print ("sorry, room already exists!please choose another name")
        elif room_type.upper == "LSPACE":
                lspace = RoomClass.Lspace(room_name, room_type)
                self.all_rooms.append(lspace)
                self.lspace_list.append(lspace)
        elif room_name.upper == "OFFICE":
                    office = RoomClass.Lspace(room_name, room_type)
                    self.all_rooms.append(office)
                    self.office_list.append(office)
        else:
                print("sorry, that room_type does not exist")
    create_room("angie", "office")


    def generate_lspace(self):
        lspaces = [room for room in Amity.available_lspaces if room.room_type == "lSPACE"]
        for lspace in Amity.available_lspaces:
            if lspace.occupants > lspace.max_occupants:
                chosen_lspace = None
            else:
                chosen_lspace = random.choice(Amity.available_lspaces)
                return chosen_lspace
    def generate_office(self):
        offices = [room for room in Amity.available_offices if room.room_type == "office"]
        for office in Amity.available_offices:
            if office.occupants > office.max_occupants:
                chosen_office = None
            else:
                chosen_office = random.choice(Amity.available_offices)
            return chosen_office

    def create_person(self, person_name, person_description, wants_accommodation):
        if person_name in Amity.all_people:
            print("sorry, this user already exists. please choose another name")
            if person_description.upper == "STAFF":
                staff = PersonClass.Staff(person_name, person_description)
                self.all_people.append(staff)
                self.staff_list.append(staff)
                allocated_office = Amity.generate_office
                if chosen_office != None:
                    Amity.office_allocations.append(person_name.upper + " " + person_description)
                    print("congratulations,%S, you have been assigned to room %S" % (person_name, allocated_office))
                else:
                    Amity.amity_unallocated.append(person_name.upper + "" + person_description)
                    print("sorry, all rooms are full at this time.")
            elif person_description.upper == "FELLOW":
                fellow = PersonClass.Fellow(person_name, person_description)
                self.all_people.append(fellow)
                self.fellows_list.append(fellow)
                allocated_office = Amity.generate_office
                if chosen_office != None:
                    Amity.office_allocations.append(person_name.upper + " " + person_description)
                    print("congratulations,%S, you have been assigned to room %S" % (person_name, allocated_office))
                else:
                    Amity.amity_unallocated.append(person_name.upper + "" + person_description)
                    print("sorry, all rooms are full at this time.")
                if wants_accommodation.upper == "Y":
                    if chosen_lspace != None
                        allocated_lspace = Amity.generate_lspace()
                        Amity.lspace_allocations.append(person_name.upper + " " + person_description.upper)
                        print("congratulations,%S, you have been assigned to room %S" % (person_name, allocated_lspace))
                    else:
                        Amity.amity_unallocated.append(person_name.upper + "" + person_description)
                        print("sorry, all rooms are full at this time.")

                else:
                    print("user has been successfully created")

        else:
            print ("sorry, that person does not exist")

    def reallocate_person(self, person_name, person_description, new_room):
            if new_room in Amity.amity_lspaces:
                if person_name in Amity.amity_staff:
                    print("sorry, staff cannot be assigned living spaces")
                elif person_name in Amity.amity_fellows:
                    if new_room.upper not in Amity.available_lspaces:
                        print("sorry, the room is not available")
                    else:
                        reallocated_lspace = new_room
                        Amity.lspace_allocations.append(person_name.upper + " " + person_description.upper)
                        print("congratulations,%S, you have been re-assigned to room %S" % (
                        person_name, reallocated_lspace))
            else:
                print("The room you chose does not exist")


    def load_people(self, file):
        if file:
            with open(file, 'r') as file:
                file_content = file.readlines()
                for line in file_content:
                    information = line.split
                    first_name =  information[0]
                    second_name = information[1]
                    self.person_name = first_name + second_name
                    information[2] = self.person_description
                    if information[3] in file:
                        self.wants_accommodation == "Y"
                    else:
                        self.wants_accomodation == "N"
        else:
            print("please provide a text file")


    def print_allocations(filename=None):
        print("-"*30 +"\n"+ "amity_allocations\n" + "-"*30)
        for room in Amity.amity_allocations.keys():
            if room != "None":
                print (room)
            for person in Amity.amity_allocations[room]:
                print(person)
        if filename:
            file = open(filename+ ".txt", "a")
            for room in Amity.amity_allocations.keys():
                for person in Amity.amity_allocations[person]:
                    file.write (person)


    def print_unallocated(filename=None):
        print("-" * 30 + "\n" + "amity_allocations\n" + "-" * 30)
        for person in Amity.Amity_unallocated[person]:
            print (person)
        if filename:
            file = open(filename + ".txt", "a")
            for person in Amity.amity_unallocated[person]
                file.write(person)

    def save_state():
















