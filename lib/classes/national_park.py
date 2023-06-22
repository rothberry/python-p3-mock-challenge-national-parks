from ipdb import set_trace

class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        # # self._trips = []
        # # self._visitors = []
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Nice try foo")

    # @property
    def trips(self):
        from classes.trip import Trip
        return [ trip  for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        visitors = [ trip.visitor for trip in self.trips()]
        return [*set(visitors)]

    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        from classes.visitor import Visitor
        # return the visitor instance with the most amount of trips to this park
        # create a dict counter to store the name/visitor and the freq
        counter = dict()
        for trip in self.trips():
            # for each loop, 
            # if there is NO key of this visitor's name
            #   then set the key of name and value to 1
            # if the IS a key of the visitor's name
            #   then increase the value of that key by 1
            v_name = trip.visitor.name
            try:
                counter[v_name] += 1
            except KeyError:
                counter[v_name] = 1
        # if just needed to return the name
        # return max(counter)
        return [vis for vis in Visitor.all if vis.name == max(counter)][0]


            