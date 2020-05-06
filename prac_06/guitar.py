CURRENT_YEAR = 2020
VINTAGE_YEAR = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Sort details of a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a representation of guitar information"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of a guitar based on CURRENT_YEAR"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is either vintage or not"""
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        """To sort guitars based on year released"""
        return self.year < other.year
