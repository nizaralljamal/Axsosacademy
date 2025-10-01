from Library import Library

class DVD(Library):
    def __init__(self, title, director, release_date, late_fee_rate):
        super().__init__(title, director, release_date, late_fee_rate)
        self.type = "DVD"
