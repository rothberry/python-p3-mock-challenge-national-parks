from ipdb import set_trace
class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Hi")

    def trips(self):
        from classes.trip import Trip
        # set_trace()
        return [trip for trip in Trip.all if trip.national_park == self] 
    
    def visitors(self):
        visitors = [trip.visitor for trip in self.trips()] 
        return [*set(visitors)]
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        counter = dict()
        for trip in self.trips():
            try: 
                counter[trip.visitor.name][0] += 1
            except KeyError:
                counter[trip.visitor.name] = [1, trip.visitor]
        return counter[max(counter)][1]
        
        