class PersonClass(object):

    """
    should have person_id, person attribute, person name
    """
    def __init__(self, person_name, person_description, wants_accomodation):
        self.person_name = person_name
        self.person_description = person_description
        self.wants_accommodation = wants_accomodation

class Fellow(PersonClass):
    def __init__(self, person_name, person_description, wants_accomodation='N'):
        super(Fellow, self).__init__(person_name, person_description, wants_accomodation)


class Staff(PersonClass):
    def __init__(self, person_name, person_description, wants_accomodation='N'):

        super(Staff, self).__init__(person_name, person_description, wants_accomodation)

#create person here
