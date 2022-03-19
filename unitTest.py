import unittest
from main import MovingZeros

class TestMovingZeros(unittest.TestCase):

    def test_random_array(self):
        array1 = [0,1,0,3,0,0,10,2,1,0]
        array2 = [0,1]
        array3 = [0,0,0,0]
        array4 = [1,2,3]
        self.assertEqual(MovingZeros(array1), [1, 3, 10, 2, 1, 0, 0, 0, 0, 0])
        self.assertEqual(MovingZeros(array2), [1, 0])
        self.assertEqual(MovingZeros(array3), [0, 0, 0, 0])
        self.assertEqual(MovingZeros(array4), [1, 2, 3])

    def test_empty_array(self):
        self.assertEqual(MovingZeros([]), [])


if __name__ == '__main__':
    unittest.main()
