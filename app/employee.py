class PersonClass:

    """
    should have person_id, person attribute, person name
    """
    def __init__(self, person_name, person_description):
        self.person_name = person_name
        self.person_description = person_description


class Fellow(PersonClass):
    def __init__(self, person_name):
        super(Fellow, self).__init__(person_name,
                                     person_description="fellow")


class Staff(PersonClass):
    def __init__(self, person_name):

        super(Staff, self).__init__(person_name,
                                    person_description="staff")
