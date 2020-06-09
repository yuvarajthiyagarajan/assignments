import unittest
import resourceallocator


class TestResalloc(unittest.TestCase):

# Test case 1 : Capacity of 1150 units for 1 Hour
	def test_resourceAllocator(self):
		self.assertEqual(resourceallocator.resourceAllocator(1, 1150),{"Output": [{"region": "New York", "total_cost": "$10150", "machines": "[('8XLarge', 7), ('XLarge', 1), ('Large', 1)]"}, 
																				{"region": "India", "total_cost": "$9520", "machines": "[('8XLarge', 7), ('Large', 3)]"}, 
																				{"region": "China", "total_cost": "$8570", "machines": "[('8XLarge', 7), ('XLarge', 1), ('Large', 1)]"}]})

# Test case 2 : 100 units for 24 Hours
	def test_resourceAllocator_two(self):
		self.assertEqual(resourceallocator.resourceAllocator(24, 100),{'Output': [{'region': 'New York', 'total_cost': '$24096', 'machines': "[('4XLarge', 1), ('XLarge', 1)]"}, 
																				{'region': 'India', 'total_cost': '$26544', 'machines': "[('2XLarge', 2), ('Large', 2)]"}, 
																				{'region': 'China', 'total_cost': '$20880', 'machines': "[('4XLarge', 1), ('XLarge', 1)]"}]})

# Test case 3 : 230 units for 5 Hours
	def test_resourceAllocator_three(self):
		self.assertEqual(resourceallocator.resourceAllocator(5, 230),{'Output': [{'region': 'New York', 'total_cost': '$11050', 'machines': "[('8XLarge', 1), ('2XLarge', 1), ('Large', 3)]"}, 
																				{'region': 'India', 'total_cost': '$10665', 'machines': "[('8XLarge', 1), ('2XLarge', 1), ('Large', 3)]"}, 
																				{'region': 'China', 'total_cost': '$9450', 'machines': "[('8XLarge', 1), ('XLarge', 3), ('Large', 1)]"}]})

# Test case 4 : 1100 units for 12 Hours
	def test_resourceAllocator_four(self):
		self.assertEqual(resourceallocator.resourceAllocator(12, 1100),{'Output': [{'region': 'New York', 'total_cost': '$118368', 'machines': "[('8XLarge', 6), ('4XLarge', 1), ('XLarge', 3)]"}, 
																				{'region': 'India', 'total_cost': '$114360', 'machines': "[('8XLarge', 6), ('4XLarge', 1), ('Large', 6)]"}, 
																				{'region': 'China', 'total_cost': '$100200', 'machines': "[('8XLarge', 6), ('4XLarge', 1), ('XLarge', 3)]"}]})


if __name__ == '__main__':
	unittest.main()