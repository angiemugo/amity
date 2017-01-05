
from app.database import Employee, Room, create_db, Base
from app.employee import PersonClass, Fellow, Staff
from app.room import RoomClass, Office, Lspace
import random
from collections import defaultdict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select


class AmityDefaultDict(defaultdict):
    def __setitem__(self, key, value):
        key = key.upper()
        dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        key = key.upper()
        return dict.__getitem__(self, key)


class Amity(object):
    def __init__(self):
        self.all_people = []
        self.all_rooms = []
        self.office_allocations = AmityDefaultDict(list)
        self.lspace_allocations = AmityDefaultDict(list)
        self.amity_unallocated = []
        self.fellows_list = []
        self.staff_list = []

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

            if room.room_type.upper() == r_type.upper():
                if room.room_type.upper() == "LSPACE":
                    if room.occupants < room.max_occupants:
                        available.append(room)

                if room.room_type.upper() == "OFFICE":
                    if room.occupants < room.max_occupants:
                        available.append(room)

        if len(available) == 0:
            return None
        else:
            return random.choice(available)

    def add_person(self, person_name, person_description,
                      wants_accommodation="N"):
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
                    self.office_allocations[allocated_office.room_name].append(person_name)
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
                    self.add_person(person_name=full_name,
                                    person_description=description,
                                    wants_accommodation=wants_accommodation)
                    print("adding people...")

        else:
            print("please provide a text file")

    def employee_position(self, name):
        """defines position of person"""
        for person in self.fellows_list:
            if person.person_name == name:
                return "IsFellow"
        for person in self.staff_list:
            if person.person_name == name:
                return "IsStaff"

    def print_office_allocations(self, filename=None):
        """prints all allocations"""
        print("-" * 30 + "\n" + "AMITY OFFICE ALLOCATIONS\n" + "-" * 30 + "\n")
        for office, names in self.office_allocations.items():
            print(office.upper())
            print("-" * 30)
            print("\n")
            for name in names:
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
        for lspace, names in self.lspace_allocations.items():
            print(lspace.upper())
            print("-" * 30)
            print("\n")
            for name in names:
                print(name)
                print("\n")

            if filename:
                file = open(filename, "a")
                file.write("\n")
                file.write("-" * 30 + "\n")
                file.write(lspace)
                file.write ("\n")
                file.write("-" * 30 + "\n")
                for name in self.lspace_allocations[lspace]:
                        file.write(name.upper() + ", " )
                file.write("\n"+"-"*30 + "\n")

    def print_allocations(self, filename=None):
        self.print_office_allocations(filename)
        self.print_lspace_allocations(filename)

    def check_room_type(self, name):
        """checks room allocated to a person"""
        for room in self.all_rooms:
            if name.upper() == room.room_name.upper():
                return room.room_type
        return None

    def check_allocated_room(self, person_name, room_type):
        if room_type == "LSPACE":
            for room in self.lspace_allocations:
                if person_name in self.lspace_allocations[room]:
                    return room
        elif room_type == "OFFICE":
            for room in self.office_allocations:

                if person_name in self.office_allocations[room]:
                    return room
        return None





    def reallocate_person(self, person_name, new_room):
        """reallocates person allocates person to a specifiedroom """
        all_people_names = [person.person_name for person in self.all_people]
        for name in all_people_names:
            if name == person_name:
                if person_name in all_people_names:
                    rtype = self.check_room_type(new_room)
                    current_room = self.check_allocated_room(person_name, rtype)
                    if rtype is None:
                        print(new_room+" does not exist")
                        return
                    elif rtype == 'LSPACE':
                        if current_room is not None:
                            self.lspace_allocations[current_room].remove(person_name)
                        self.lspace_allocations[new_room].append(person_name)
                        print(person_name + " moved to " + new_room)
                        break
                    elif rtype == 'OFFICE':
                        if current_room is not None:

                            self.office_allocations[current_room].remove(person_name)
                        self.office_allocations[new_room].append(person_name)
                        print(person_name + " moved to " + new_room)
                        break
                else:
                    print(person_name+" does not exist")

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
                for person in self.amity_unallocated:
                    file.write(person)

    def print_room(self, room_name):
        """prints specified room and all its occupants"""
        for room in self.all_rooms:
            if room_name.upper() == room.room_name.upper():
                print("-" * 30 + "\n" + room_name.upper() + "\n" + "-" * 30)
                if room.room_type.upper() == 'lspace'.upper():
                    if room_name.upper() in self.lspace_allocations:
                        print(self.lspace_allocations[room_name])

                elif room.room_type.upper() == 'office'.upper():
                    if room_name.upper() in self.office_allocations:
                        print(self.office_allocations[room_name])
                return
    print("the room you chose does not exist. would you like to add it?")

    def save_state(self, db_name='somedb'):
        """persists information to db"""
        engine=create_db(db_name)
        Base.metadata.create_all(engine)
        Session=sessionmaker(bind=engine)
        session = Session()

        items = select([Room])
        result = session.execute(items)

        database_rooms_list = [item.room_name for item in result]
        for room in self.all_rooms:
            if room.room_name not in database_rooms_list:
                new_room = Room(room_name=room.room_name,
                                room_type=room.room_type,
                                occupants=room.occupants,
                                max_occupants=room.max_occupants)
                session.add(new_room)
                session.commit()

        people = select([Employee])
        response = session.execute(people)

        dbpersons_list = [item.person_name for item in response]
        print("saving state....")
        for person in self.all_people:
            list_index=self.all_people.index(person)
            name = self.all_people[list_index].person_name
            if name not in dbpersons_list:
                office_allocated = self.check_allocated_room(name.upper(), 'OFFICE')
                if office_allocated is None:
                    office_allocated = 'N'
                lspace_allocated = self.check_allocated_room(name.upper(), 'LSPACE')
                if lspace_allocated is None:
                    lspace_allocated = 'N'
                person_description = self.all_people[list_index].person_description
                wants_accommodation = self.all_people[list_index].wants_accommodation
                new_person = Employee(person_name=name,
                                      person_description=person_description,
                                      wants_accommodation=wants_accommodation,
                                      lspace_allocated=lspace_allocated,
                                      office_allocated=office_allocated)
                session.add(new_person)
                session.commit()

    def load_state(self, dbname='amitydb'):
        engine = create_engine('sqlite:///'+dbname)
        Session = sessionmaker(bind=engine)
        session = Session()

        people = session.query(Employee).all()
        rooms = session.query(Room).all()
        all_rooms_names = [room.room_name for room in self.all_rooms]
        for room in rooms:
            if room.room_name not in all_rooms_names:
                    self.all_rooms.append(room)
        all_people_names = [person.person_name for person in self.all_people]
        for person in people:
            if person.person_name not in all_people_names:
                    self.all_people.append(person)
                    try:
                        self.office_allocations[person.office_allocated].append(person.person_name)
                        self.lspace_allocations[person.lspace_allocated].append(person.person_name)
                    except:
                        pass
