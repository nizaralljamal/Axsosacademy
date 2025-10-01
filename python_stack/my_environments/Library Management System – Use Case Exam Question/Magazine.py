from Library import Library
class Magazine(Library):
    def __init__(self, title, issue_number, publication_date, late_fee_rate):
        super().__init__(title, issue_number, publication_date, late_fee_rate)
        self.type = "Magazine"
