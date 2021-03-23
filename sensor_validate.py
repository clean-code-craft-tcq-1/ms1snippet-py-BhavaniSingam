
def  isChargeRateExceeds(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_soccurr_reading(values,maxdeltastring):
    if values is not None:
        last_but_one_reading = len(values) - 1
        if  maxdeltastring == 'soc':
            md = 0.05
        else:
            md = 0.1
        for i in range(last_but_one_reading):
            if(not isChargeRateExceeds(values[i], values[i + 1], md)):
                return False
        return True
