import unittest
from custom_exceptions import customer_excpetions


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = customer_excpetions.Customer(1001, 'Morishita', 'Elijah', '111-222-3456')

    def tearDown(self):
        del self.customer

    def test_valid_customer_id(self):
        self.assertEqual(self.customer._customer_id, 1001)

    def test_valid_last_name(self):
        self.assertEqual(self.customer._last_name, 'Morishita')

    def test_valid_first_name(self):
        self.assertEqual(self.customer._first_name, 'Elijah')

    def test_valid_phone_number(self):
        self.assertEqual(self.customer._phone_number, '111-222-3456')

    def test_invalid_customer_id(self):
        self.assertEqual(self.customer._customer_id, 888)

    def test_invalid_last_name(self):
        self.assertEqual(self.customer._last_name, 'Johnson')

    def test_invalid_first_name(self):
        self.assertEqual(self.customer._first_name, 'Adam')

    def test_invalid_phone_number(self):
        self.assertEqual(self.customer._phone_number, '888-888-8888')

    def test_customer_str(self):
        test_string = str("Customer ID: " + self.customer._customer_id + "\n"\
        + self.customer._last_name + ', ' + self.customer._first_name + "\n"\
        + self.customer._phone_number + "\n"\
        + self.customer._address)
        self.assertEqual(self.customer.__str__(), test_string)


if __name__ == '__main__':
    unittest.main()
