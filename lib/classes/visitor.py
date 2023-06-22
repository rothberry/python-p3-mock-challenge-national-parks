from ipdb import set_trace

class Visitor:
    # all = []

    def __init__(self, name):
        self._name = name
        # Visitor.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # set_trace()
        if isinstance(name, str) and len(name) in range(1, 15) and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Hi")
    
    def trips(self):
        from classes.trip import Trip
        return [ trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        parks = [trip.national_park for trip in self.trips() ]
        return [*set(parks)]
