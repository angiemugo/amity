class PersonClass:

    """
    should have person_id, person attribute, person name
    """
    def __init__(self, person_name, person_description, wants_accomodation):
        self.person_name = person_name
        self.person_description = person_description
        self.wants_accommodation = wants_accomodation


class Fellow(PersonClass):
    def __init__(self, person_name, wants_accommodation):
        super(Fellow, self).__init__(person_name, wants_accommodation,
                                     person_description="fellow")


class Staff(PersonClass):
    def __init__(self, person_name):

        super(Staff, self).__init__(person_name,wants_accomodation=N,
                                    person_description="staff")
#create person here
