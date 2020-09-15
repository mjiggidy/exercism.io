import re

class PhoneNumber:
    """Parse a phone number following the NANP system"""

    pat_phone = re.compile(r"^\D*(?P<country>1)?\D*(?P<area_code>[2-9]\d{2})\D*(?P<exchange>[2-9]\d{2})\D*(?P<subscriber>\d{4})$")

    def __init__(self, number):

        number = str(number).strip()
        
        # Validate number against NANP pattern
        if (m := self.__class__.pat_phone.match(number)) is None:
            raise ValueError(f"Not a valid NANP phone number: {number}")
        
        # Store number as 10-digit string
        self._number = str().join(m.group(x) for x in ("area_code","exchange","subscriber"))
    
    def pretty(self):
        """Format number as (xxx) xxx-xxxx"""
        return f"({self.area_code}) {self.exchange}-{self.subscriber}"

    @property
    def number(self):
        return self._number
    
    @property
    def area_code(self):
        return self._number[0:3]
    
    @property
    def exchange(self):
        return self._number[3:6]
    
    @property
    def subscriber(self):
        return self._number[6:10]