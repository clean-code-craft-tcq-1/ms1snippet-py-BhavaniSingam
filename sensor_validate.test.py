import unittest
import sensor_validate

class SensorValidatorTest(unittest.TestCase):
  def test_reports_error_when_soccurr_jumps(self):
    self.assertFalse(
      sensor_validate.validate_soccurr_reading([0.0, 0.01, 0.5, 0.51],'soc'),
      sensor_validate.validate_soccurr_reading([0.03, 0.03, 0.03, 0.33],'curr'),
      sensor_validate.validate_soccurr_reading(None,'None') 
    )   
if __name__ == "__main__":
  unittest.main()
