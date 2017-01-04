class PersonClass(object):

    """
    should have person_id, person description, person name
    """
    def __init__(self, person_name, person_description, wants_accommodation):
        self.person_name = person_name
        self.person_description = person_description
        self.wants_accommodation = wants_accommodation

class Fellow(PersonClass):
    def __init__(self, person_name, person_description, wants_accommodation='N'):
        super(Fellow, self).__init__(person_name, person_description, wants_accommodation)


class Staff(PersonClass):
    def __init__(self, person_name, person_description, wants_accommodation='N'):

        super(Staff, self).__init__(person_name, person_description, wants_accommodation)


