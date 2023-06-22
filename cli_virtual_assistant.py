from collections import UserDict


class Field:
    """Base class for fields in a record."""

    def __init__(self, value: str) -> None:
        """
        Initialize a new field.

        Args:
            value (str): The value of the field.
        """

        self.value = value


class Name(Field):
    """Name field in a record."""


class Phone(Field):
    """Phone number field in a record."""


class Record:
    """Record representing a contact in the address book."""

    def __init__(self, name: Name, phone: Phone = None) -> None:
        """
        Initialize a new record.

        Args:
            name (Name): The name of the contact.
            phone (Phone, optional): The phone number of the contact. Defaults to None.
        """

        self.name = name
        self.phones = []
        if phone:        
            self.phones.append(phone)

    def add_phone(self, phone: Phone) -> None:
        """
        Add a phone number to the record.

        Args:
            phone (Phone): The phone number to add.
        """

        self.phones.append(phone)

    def remove_phone(self, phone: Phone) -> None:
        """
        Remove a phone number from the record.

        Args:
            phone (Phone): The phone number to remove.
        """

        for existing_phone in self.phones:
            if phone.value == existing_phone.value:
                self.phones.remove(existing_phone)


    def edit_phone(self, old_phone: Phone, new_phone: Phone) -> None:
        """
        Edit a phone number in the record.

        Args:
            old_phone (Phone): The old phone number to replace.
            new_phone (Phone): The new phone number.
        """


        for idx, phone in enumerate(self.phones):
            if old_phone.value == phone.value:
                self.phones[idx] = new_phone


class AddressBook(UserDict):
    """Address book that extends UserDict."""

    def add_record(self, record: Record) -> None:
        """
        Add a record to the address book.

        Args:
            record (Record): The record to add.
        """

        self.data[record.name.value] = record

    def search(self, search_obj: object) -> str or list[str] or None:
        """
        Find a name by phone or a phone with a name in the address book.

        Args:
            search_obj: The search object representing either a Name or a Phone.

        Returns:
            Optional: The search results. If searching by Name, returns a list of phone numbers.
                If searching by Phone number, returns the name of the contact. Returns None if no match is found.
        """

        results = None

        if isinstance(search_obj, Name):
            for name, record in self.data.items():
                if search_obj.value == name:                    
                    results = list(map(lambda x: x.value, record.phones))

        elif isinstance(search_obj, Phone):
            for name, record in self.data.items():
                for phone in record.phones:
                    if search_obj.value == phone.value:
                        results = name

        return results










  
if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'


    
    print('All Ok)')




    