""" 
    Helpful pytest tools

    pytest 
        -x => Stop tests after the first fail
        -s => Will use the ipdb.set_trace()

    Run a specific test file
        => pytest lib/testing/visitor_test.py => runs only this test file
    
    Skip test
        => @pytest.mark.skip
            def test_method()
 """

from ipdb import set_trace

class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # the hasattr() is the way to make sure that we can't write over the same attribute 
        # len(name) in range(1,15) ???
        if isinstance(name, str) and  len(name) in range(1,15) and not hasattr( self, "name"):
            self._name = name
        else:
            # raise TypeError("Not a STRING")
            raise Exception("Not a STRING")

    def trips(self):
        from classes.trip import Trip
        # return is a list of Trips that relate to THIS visitor
        # Iterator with conditional ..... a ..... filter
        # filter the Trip.all for where this self is the visitor
        output = []
        for trip in Trip.all:
            if trip.visitor == self:
                output.append(trip)
        return output
        # return [ trip for trip in Trip.all if trip.visitor == self ]
    
    def national_parks(self):
        parks =  [trip.national_park for trip in self.trips() ]
        return [*set(parks)]