from collections import defaultdict
import random
from app.room import RoomClass, Office, Lspace
from app.employee import PersonClass, Fellow, Staff
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Employee, Room, create_db, Base

import random





class Amity:
    def __init__(self):
        self.all_people = []
        self.all_rooms = []
        self.office_allocations = defaultdict(list)
        self.lspace_allocations = defaultdict(list)
        self.amity_unallocated = []
        self.fellows_list = []
        self.staff_list = []
        self.lspace_list = []
        self.office_list = []

    def create_room(self, room_name, room_type):

        if room_name in self.all_rooms:
            print("sorry, room already exists!please choose another name")

        else:
            if room_type.upper() == "LSPACE":
                room = Lspace(room_name, room_type)
                self.all_rooms.append(room)
                print("room successfully created")
            elif room_type.upper() == "OFFICE":
                room = Office(room_name, room_type)
                self.all_rooms.append(room)
                print("room successfully created")
            else:
                print("sorry, that room_type does not exist")

    def generate_room(self, r_type):
        available = []
        for room in self.all_rooms:
            if room.room_type == r_type.upper() and room.occupants <= room.max_occupants:
                available.append(room)

        if len(available) == 0:
            return None
        else:
            return random.choice(available)

    def create_person(self, person_name, person_description,
                      wants_accommodation):
        if person_name in self.all_people:
            print("sorry, this user already exists.please choose another name")
        else:
            if person_description.upper() == "STAFF":
                staff = Staff(person_name, person_description,
                              wants_accommodation)
                self.all_people.append(staff)
                self.staff_list.append(staff)
                print("person successfully created")

                allocated_office = self.generate_room("OFFICE")


                if allocated_office is not None:
                    self.office_allocations[allocated_office].append
                    (person_name.upper)
                    allocated_office.occupants += 1
                    print("congratulations %s, you have been assigned to office %s"
                              % (person_name, allocated_office.room_name))




                else:
                    self.amity_unallocated.append(person_name.upper)
                    print("sorry, all rooms are full at this time.")

            elif person_description.upper() == "FELLOW":
                fellow = Fellow(person_name, person_description,
                                wants_accommodation)
                self.all_people.append(fellow)
                self.fellows_list.append(fellow)
                allocated_office = self.generate_room("OFFICE")
                if allocated_office is not None:
                    self.office_allocations[allocated_office].append(person_name)
                    allocated_office.occupants += 1
                    print("congratulations %s, you have been assigned to office %s"
                          % (person_name, allocated_office.room_name))
                else:
                    self.amity_unallocated.append(person_name.upper() + "" + person_description)
                    print("sorry, all rooms are full at this time.")

                if wants_accommodation.upper() == "Y":
                    allocated_lspace = self.generate_room("LSPACE")
                    if allocated_lspace is not None:
                        self.lspace_allocations[allocated_lspace.room_name].append(person_name)
                        allocated_lspace.occupants += 1
                        print("congratulations %s, you have been assigned to lspace %s"
                              % (person_name, allocated_lspace.room_name))
                    else:
                        person = person_name.upper()
                        self.amity_unallocated.append(person)
                        print("sorry, all rooms are full at this time.")

                else:
                    print("user has been successfully created")

    def reallocate_person_to_lspace(self, person_name, new_room, rtype):
        room = Lspace(person_name, new_room, rtype)
        available = [room.room_name for room in self.all_rooms if
                             room.room_type == "rtype" and room.occupants < room.max_occupants]
        if rtype == "lspace":
            if person_name in self.staff_list:
                print("sorry, staff cannot be assigned living spaces")
            elif person_name in self.fellows_list:
                if new_room.upper not in self.available:
                    print("sorry, the room is not available")
                else:
                    reallocated_lspace = new_room
                    self.lspace_allocations.append(person_name.upper)

                    print("congratulations %s, you have been re-assigned to room %s"
                          % (person_name, reallocated_lspace))
        else:
            print("The room you chose is not available")
        if rtype == Office:
            if new_room.upper not in self.available:
                print("sorry, the room is not available")
            else:
                reallocated_office = new_room
                self.office_allocations.append(person_name.upper)
                print("congratulations %s, you have been re-assigned to room %s"


    def load_people(self, filename):
        if filename:
            # file = file.txt
            with open(filename, 'r') as people_file:
                # filename_content = people_file.readlines()
                for line in people_file:
                    information = line.split()
                    first_name = information[0]
                    second_name = information[1]
                    full_name = first_name + " " + second_name
                    description = information[2]
                    if len(information) == 4:
                        wants_accommodation = information[3]
                    else:
                        wants_accommodation = "N"
                    self.create_person(person_name=full_name,
                                       person_description=description,
                                       wants_accommodation=wants_accommodation)
                    print("adding people...")

        else:
            print("please provide a text file")

    def print_allocations(self, filename=None):
        print("-" * 30 + "\n" + "AMITY ALLOCATIONS\n" + "-" * 30)

        #print(self.office_allocations)
        for office, name in self.office_allocations.items():
            print(office.room_name)
            print("-" * 30)
            print("\n")
            print(name)
            print("\n")

        if filename:
            file = open(filename + ".txt", "a")
            file.write("-" * 30 + "\n")
            for office in self.office_allocations:
                file.write("/n" + office.room_name + "/n")
                file.write("-" * 30 + "\n")
                for name in self.office_allocations[office]:
                    file.write(name + ", " )
                file.write("\n")

    def print_unallocated(self, filename=None):
        print("-" * 30 + "\n" + "amity_unallocated\n" + "-" * 30)
        if len(self.amity_unallocated)!=0:
            for person in self.amity_unallocated:
                print(person)
        else:
            print("All people have been allocated rooms!")
            if filename:
                file = open(filename + ".txt", "a")
                for person in self.amity_unallocated[person]:
                    file.write(person)



    def print_room(self, room_name):
        print("-" * 30 + "\n" + room_name + "\n" + "-" * 30)
        for room,person in self.lspace_allocations.items() :
            print(person)


    def save_state(self, db_name='amity'):
        engine = create_db(db_name)
        Base.metadata.bind = engine
        Session = sessionmaker()
        session = Session()
        items = select([self.all_rooms])
        result = session.execute(items)
        drooms_list = [item.room_name for item in result]
        if self.all_rooms[room]['room_name'] not in drooms_list:
            new_room = RoomClass(room_name=self.all_rooms[room]['room_name'],
                                      room_type=self.all_rooms[room]['room_type'])
            session.add(new_room)
            session.commit()
        people = select([self.all_people])
        response = session.execute(people)
        dbpersons_list = [item.person_name for item in response]
        for people in range(len(self.all_people)):
            person = self.all_people[people]['person_name']
            if person not in dbpersons_list:
                office_allocated = self.generate_room("office")
                lspace_allocated = self.generate_room("lspace")
                person_name = self.all_people[people]['person_name']
                person_description = self.all_people[people]['person_description']
                wants_accommodation = self.all_people[people]['wants_accommodation']
                new_person = people(person_name = person_name ,
                                    person_description = person_description,
                                    wants_accommodation = wants_accommodation,
                                    lspace_allocated = lspace_allocated,
                                    office_allocated = office_allocated)
                session.add(new_person)
                session.commit()


        def load_state():





                pass

inst = Amity()
inst.print_allocations()
inst = Amity()
inst.create_room("angie", "office")

inst.create_room("de", "lspace")
inst.create_room("de1", "lspace")
inst.create_room("de2", "lspace")
inst.create_room("de3", "lspace")

inst.create_person("Angela", "fellow", "Y")
inst.create_person("Ian", "fellow", "Y")

inst.print_allocations("load_file")
inst.print_unallocated()

inst.load_people("people_file.txt")
inst.print_room("angie")
inst.reallocate_person_to_lspace("angie", "de")
inst.save_state(amitydb)
