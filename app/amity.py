from collections import defaultdict
import random
import json
from room import RoomClass, Office, Lspace
from employee import PersonClass, Fellow, Staff
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Employee, Room, create_db, Base
from sqlalchemy.sql import select

import random


class Amity(object):
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
        """creates a room not previously in system"""
        all_room_names = [room.room_name for room in self.all_rooms]

        if room_name in all_room_names:
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
        """returns a list of all rooms not full"""
        available = []
        for room in self.all_rooms:

            if room.room_type.upper() == r_type.upper() and room.occupants < room.max_occupants:
                if room.room_type.upper() =="LSPACE":
                    max_occupants = 4
                    available.append(room)
                
                if room.room_type.upper() =="OFFICE":
                    max_occupants = 6
                    available.append(room)

        if len(available) == 0:
            return None
        else:
            return random.choice(available)




    def create_person(self, person_name, person_description,
                      wants_accommodation):
        """adds person to system"""
        all_people_names = [person.person_name for person in self.all_people]
        if person_name in all_people_names:
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
                    (person_name.upper())
                    allocated_office.occupants += 1
                    print("congratulations %s, you have been assigned to office %s"
                              % (person_name, allocated_office.room_name.upper()))
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
                    self.office_allocations[allocated_office.room_name].append(person_name.upper())
                    allocated_office.occupants += 1
                    print("congratulations %s, you have been assigned to office %s"
                          % (person_name, allocated_office.room_name.upper()))
                else:
                    self.amity_unallocated.append(person_name.upper() + "" + person_description)
                    print("sorry, all rooms are full at this time.")

                if wants_accommodation.upper() == "Y":
                    allocated_lspace = self.generate_room("LSPACE")
                    if allocated_lspace is not None:
                        self.lspace_allocations[allocated_lspace.room_name].append(person_name.upper())
                        allocated_lspace.occupants += 1
                        print("congratulations %s, you have been assigned to lspace %s"
                              % (person_name, allocated_lspace.room_name))
                    else:
                        person = person_name.upper()
                        self.amity_unallocated.append(person)
                        print("sorry, all rooms are full at this time.")






    def employee_position(self, name):
        """defines position of person"""
        for person in self.fellows_list:
            if person.person_name == name:
                return "IsFellow"
        for person in self.staff_list:
            if person.person_name == name:
                return "IsStaff"


    def reallocate_person(self, person_name, new_room, rtype):
        """reallocates person allocates person to a specifiedroom """

        available = [room.room_name.upper() for room in self.all_rooms if room.occupants < room.max_occupants ]
        person_found = False
        for person in self.all_people:
            if person.person_name == person_name:
                person_found = True
                break
        if not person_found:
            print("Person does not Exist")
            return

        if person_found:
            if rtype == "lspace":

                current_room = [room_name ]
                if self.employee_position(person_name) == "IsStaff":
                    print("sorry, staff cannot be assigned living spaces")
                elif self.employee_position(person_name.upper()) == "IsFellow":
                    if new_room.upper() not in available:
                        print("sorry, the room is not available")
                    else:
                        reallocated_lspace = new_room
                        self.lspace_allocations[new_room].append(person_name.upper())
                        print("congratulations %s, you have been re-assigned to room %s"
                              %(person_name, reallocated_lspace))

            else:
                if new_room.upper() not in available:
                    print("sorry, the room is not available")
                else:
                    reallocated_office = new_room
                    print("congratulations %s, you have been re-assigned to room %s"
                          %(person_name, reallocated_office))
    def load_people(self, filename):
        """it loads people into system from a text file"""
        if filename:

            with open(filename, 'r') as people_file:
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


    def print_office_allocations(self, filename=None):
        """prints all allocations"""
        print("-" * 30 + "\n" + "AMITY OFFICE ALLOCATIONS\n" + "-" * 30 + "\n")
        for office, name in self.office_allocations.items():
            print(office)
            print("-" * 30)
            print("\n")
            for name in name:
                print(name)
            print("\n")

            if filename:

                file = open(filename, "a")
                file.write("\n")
                file.write("-" * 30 + "\n")
                file.write(office)
                file.write ("\n")
                file.write("-" * 30 + "\n")
                for name in self.office_allocations[office]:
                        file.write(name.upper() + ", " )
                file.write("\n"+"-"*30 + "\n")





        def print_lspace_allocations(self, filename=None):
            """prints all allocations"""
            print("-" * 30 + "\n" + "AMITY LSPACE ALLOCATIONS\n" + "-" * 30 + "\n")
            for lspace, name in self.lspace_allocations.items():
                print(lspace.room_name)
                print("-" * 30)
                print("\n")
                for name in name:
                    print(name)
                print("\n")

            if filename:
                file = open(filename, "a")
                file.write("\n")
                file.write("-" * 30 + "\n")
                file.write(office)
                file.write ("\n")
                file.write("-" * 30 + "\n")
                for name in self.office_allocations[office]:
                        file.write(name.upper() + ", " )
                file.write("\n"+"-"*30 + "\n")


    def reallocate_person(self, person_name, new_room, rtype):
        """reallocates person allocates person to a specifiedroom """
        available = [room.room_name.upper() for room in self.all_rooms if room.occupants < room.max_occupants ]


        person_found = False
        for person in self.all_people:
            if person.person_name == person_name:
                person_found = True
                break
        if not person_found:
            print("Person does not Exist")
            return

        if person_found:
            if rtype == "lspace":
                for lspace, name in self.lspace_allocations.items():
                    current_room = lspace
                if new_room == current_room:
                    print("you cannot be assigned to a room you are in" )
                else:
                    if self.employee_position(person_name) == "IsStaff":
                        print("sorry, staff cannot be assigned living spaces")
                    elif self.employee_position(person_name.upper()) == "IsFellow":
                        if new_room.upper() not in available:
                            print("sorry, the room is not available")
                        else:
                            reallocated_lspace = new_room
                            self.lspace_allocations[new_room].append(person_name.upper())
                            print("congratulations %s, you have been re-assigned to room %s"
                                  %(person_name, reallocated_lspace))

            elif rtype == "office":
                for office, name in self.lspace_allocations.items():
                    current_room = office
                    if new_room == current_room:
                        print("you cannot be assigned to a room you are in")
                    else:

                        if new_room.upper() not in available:
                            print("sorry, the room is not available")
                        else:
                            reallocated_office = new_room
                            print("congratulations %s, you have been re-assigned to room %s"
                                  %(person_name, reallocated_office))

    def print_lspace_allocations(self, filename=None):
        """prints all allocations"""
        print("-" * 30 + "\n" + "AMITY ALLOCATIONS\n" + "-" * 30 + "\n")
        for lspace, name in self.lspace_allocations.items():
            print(lspace.upper())
            print("-" * 30)
            print("\n")
            print(name)
            print("\n")
            if filename:
                file = open(filename + ".txt", "a")
                file.write("-" * 30 + "\n")
                for lspace, name in self.lspace_allocations.items():
                    file.write("\n" + lspace + "\n")
                    file.write("-" * 30 + "\n")
                    for name in name:
                        file.write(name)
                        file.write("\n")

    def print_unallocated(self, filename=None):
        """prints all unallocated persons"""
        print("-" * 30 + "\n" + "amity_unallocated\n" + "-" * 30 +"\n")
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
        """prints specified room and all its occupants"""
        for room in self.all_rooms:
            if room.room_name == room_name:
                print("-" * 30 + "\n" + room_name + "\n" + "-" * 30)
                if room.room_type==  'lspace'.upper():
                    if room_name in self.lspace_allocations:
                        print(self.lspace_allocations[room_name])
                        break
                    elif room.room_type==  'office'.upper():
                        if room_name in self.office_allocations:
                            print(self.office_allocations[room_name])
                            break
            else:
                print("the room you chose does not exist. would you like to add it?")


    def save_state(self, db_name='amitydb'):
        """persists information to db"""
        engine = create_db(db_name)
        Base.metadata.bind = engine
        Session = sessionmaker()
        session = Session()
        items = select([Room])
        result = session.execute(items)
        database_rooms_list = [item.room_name for item in result]
        for room in range(len(self.all_rooms)):
            if self.all_rooms[room].room_name not in database_rooms_list:
                people_in_lspace = str(self.lspace_allocations[room]).join(",")
                people_in_office = str(self.lspace_allocations[room]).join(",")
                new_room = Room(room_name=self.all_rooms[room].room_name,
                                room_type=self.all_rooms[room].room_type
                                          )
                session.add(new_room)
                session.commit()

        people = select([Employee])
        response = session.execute(people)

        dbpersons_list = [item.person_name for item in response]
        for people in range(len(self.all_people)):
            person = self.all_people[people].person_name
            if person not in dbpersons_list:
                office_allocated = self.generate_room("office").room_name
                if office_allocated == None:
                    office_allocated = 'N'
                else:
                    office_allocated = self.generate_room("office").room_name
                lspace_allocated = self.generate_room("lspace")
                if lspace_allocated == None:
                    lspace_allocated = 'N'
                else:
                    lspace_allocated = self.generate_room("lspace").room_name
                person_description = self.all_people[people].person_description
                wants_accommodation = self.all_people[people].wants_accommodation
                new_person = Employee(person_name = person ,
                                    person_description = person_description,
                                    wants_accommodation = wants_accommodation,
                                    lspace_allocated = lspace_allocated,
                                    office_allocated = office_allocated)
                session.add(new_person)
                session.commit()


    def load_state(self, dbname='amitydb.db'):
        engine = create_engine('sqlite:///'+dbname)
        Session = sessionmaker(bind=engine)
        session = Session()

        people = session.query(Employee).all()
        rooms = session.query(Room).all()

        all_rooms_names = [room.room_name for room in self.all_rooms]
        for room in rooms:
            if room.room_name not in all_rooms_names:
                self.create_room(room.room_name, room.room_type)
            else:
                print('Room {0} already exists'.format(room.room_name))
        all_people_names = [person.person_name for person in self.all_people]
        for person in people:
            if person.person_name not in all_people_names:
                self.create_person(person.person_name, person.person_description, person.wants_accommodation)
            else:
                print('person {0} already exists'.format(person.person_name))
