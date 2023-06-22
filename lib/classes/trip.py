""" 
    In SQL the Trip Table is the JOIN TABLE
    between the NationalParks and Visitors
    If we need to go from the Visitors to the NationalParks,
    we need to go THROUGH the Trips table/class/model

 """

class Trip:

    # The cls.all is representing all the rows on our potential table
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        from classes.visitor import Visitor
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("Not a Visitor")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        from classes.national_park import NationalPark
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("Not a NationalPark")

    def get_start(self):
        return self._start_date

    def set_start(self, start_date):
        self._start_date = start_date

    def get_end(self):
        return self._end_date

    def set_end(self, end_date):
        self._end_date = end_date

    start_date = property(get_start, set_start)
    end_date = property(get_end, set_end)