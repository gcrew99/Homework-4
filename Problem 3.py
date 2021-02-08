#Gabriel Crew
import unittest 

def calculate_value(first_name,last_name):
  if type(first_name) == int or type(last_name) == int:
    return "Error"
  x = first_name + " " + last_name
  return x


class TestCase(unittest.TestCase):
  def test1(self): self.assertEqual(calculate_value("Gabriel","Crew"),"Gabriel Crew")
  def test2(self): self.assertEqual(calculate_value("Gabriel ","Crew"),"Gabriel Crew")
  def test3(self): self.assertEqual(calculate_value("hello","there"),"hello there")
  def test4(self): self.assertEqual(calculate_value("hello ","there"),"hello there")
  def test5(self): self.assertEqual(calculate_value("One","Jones"),"One Jones")
  def test6(self): self.assertEqual(calculate_value(1,"Jones"),"1 Jones")


if __name__ == '__main__':
  unittest.main()