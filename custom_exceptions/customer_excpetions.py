"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/9/2020
This program is used for testing the use of classes, objects, and exceptions
"""


class InvalidCustomerIdException(Exception):
    """Raised when an invalid customer ID is entered"""
    pass


class InvalidNameException(Exception):
    """Raised when there's an invalid last name"""
    pass


class InvalidNameException(Exception):  # (a duplicate class name?)
    """Raised when there's an invalid first name"""
    pass


class InvalidPhoneNumberFormat(Exception):
    """Raised when the phone number format is invalid"""
    pass


class Customer:

    # The constructor
    def __init__(self, customer_id, last_name="Morishita", first_name="Elijah",
                 phone_number="555-555-5555", address="123 Main St.\nDes Moines, IA 50265"):
        """
        This constructor sets the variables, with the exception of customer_id which is required
        :param customer_id:
        :param last_name:
        :param first_name:
        :param phone_number:
        :param address:
        """

        self._customer_id = customer_id
        self._last_name = last_name
        self._first_name = first_name
        self._phone_number = phone_number
        self._address = address

    def __str__(self):
        """
        A string conversion method
        :return:
        """
        return "Customer ID: " + self._customer_id + "\n"\
        + self._last_name + ', ' + self._first_name + "\n"\
        + self._phone_number + "\n"\
        + self._address

    def display(self):
        """
        This function returns the string of a class object
        :return:
        """
        cust = Customer(str(''))
        return str(cust)


# Driver
customer1 = Customer(900, 12, 13, '123-456-789')  # all invalid possibilities

#  Testing the customer ID
try:
    if customer1._customer_id < 1000 and customer1._customer_id > 9999:
        raise InvalidCustomerIdException()
except InvalidCustomerIdException:
    print("Invalid customer ID")

#  Testing the last name
try:
     lname = isinstance(customer1._last_name, str)
     if lname == False:
         raise  InvalidNameException
except InvalidNameException:
    print("Invalid name entry")

#  Testing the first name
try:
     fname = isinstance(customer1._first_name, str)
     if fname == False:
         raise  InvalidNameException
except InvalidNameException:
    print("Invalid name entry")

try:
    if len(str(customer1._phone_number)) != 12:
        raise InvalidPhoneNumberFormat
    for i in range(12):
        if i in [3,7]:
            if customer1._phone_number[i] != '-':
                raise InvalidPhoneNumberFormat
        elif not customer1._phone_number[i].isalnum():
            raise InvalidPhoneNumberFormat
except InvalidPhoneNumberFormat:
    print("Invalid phone number format")

# Garbage collection
del customer1
