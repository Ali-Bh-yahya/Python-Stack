#######################
#Python's unit testing#
#######################
# .----------------.  .----------------.  .----------------. 
#| |      __      | || |   _____      | || |     _____    | |
#| |     /  \     | || |  |_   _|     | || |    |_   _|   | |
#| |    / /\ \    | || |    | |       | || |      | |     | |
#| |   / ____ \   | || |    | |   _   | || |      | |     | |
#| | _/ /    \ \_ | || |   _| |__/ |  | || |     _| |_    | |
#| ||____|  |____|| || |  |________|  | || |    |_____|   | |
#| |              | || |              | || |              | |
#| '--------------' || '--------------' || '--------------' |
# '----------------'  '----------------'  '----------------' 

import unittest

def sum_two_values( num_1 , num_2):
   sum = num_1 + num_2
   return sum

class SumTests (unittest.TestCase): 
    def testFiveTwo(self):
        self.assertEqual(sum_two_values(5,2), 7)
    def testThreeEleven(self):
        self.assertEqual(sum_two_values(3,11), 14)

if __name__ == '__main__':
    unittest.main()
