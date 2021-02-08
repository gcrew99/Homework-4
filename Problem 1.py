import unittest 

def calculate_value(x,y,z):
  if (type(x) == int and type(y) == int and type(z) == int):
    return x*y*z
  else:
      return "Undefined"

x_in = input("Input x value ")
y_in = input("Input Y value ")
z_in = input("Input Z value ")

class TestCase(unittest.TestCase):
  def test1(self): self.assertEqual(calculate_value(2,1,7),14)
  def test2(self): self.assertEqual(calculate_value(2,0,7),14)
  def test3(self): self.assertEqual(calculate_value(-2,1,7),-14)
  def test4(self): self.assertEqual(calculate_value(-2,1,-7),-14)
  def test5(self): self.assertEqual(calculate_value(6,'f',1),"Undefined")
  def test6(self): self.assertEqual(calculate_value(6,9,1),"Undefined")



if __name__ == '__main__':
  unittest.main()