#Gabriel Crew
import unittest 

def calculate_value(list):
  if sum(list) == 0 or len(list) == 0:
    return "Undefined"
  else:
      return sum(list)/len(list)


class TestCase(unittest.TestCase):
  def test1(self): self.assertEqual(calculate_value([2,7,4,8]),5.25)
  def test2(self): self.assertEqual(calculate_value([2,7,4,8]),5)
  def test3(self): self.assertEqual(calculate_value([-2,7,-4,1]),0.5)
  def test4(self): self.assertEqual(calculate_value([-2,7,-4,1]),-0.5)
  def test5(self): self.assertEqual(calculate_value([0,0,0]),"Undefined")
  def test6(self): self.assertEqual(calculate_value([2,7,4,8]),"Undefined")



if __name__ == '__main__':
  unittest.main()