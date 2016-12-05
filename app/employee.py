class Person:

    """
    should have person_id, person attribute, person name
    """
    def __init__(self, person_id, person_name, person_description):
        self.person_id = person_id
        self.person_name = person_name
        self.person_description = person_description


class Fellow(Person):
    def __init__(self, person_id, person_name):
        super(Fellow, self).__init__(person_id, person_name,
                                     person_description="fellow")


class Staff(Person):
    def __init__(self, person_id, person_name, description):

        super(Staff, self).__init__(person_id, person_name,
                                    person_description="staff")
