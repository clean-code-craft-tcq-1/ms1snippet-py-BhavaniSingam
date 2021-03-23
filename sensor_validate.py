def isChargeRateExceeds(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def get_parameter(value):
   if value=='soc':
       return 0.05
   return 0.1


def check_none(values):
    if values is None:
        return True
    else:
        return False
    
def isSocCurrInRange(values,md):
    last_but_one_reading = len(values) - 1
    md = get_parameter(md)
    for i in range(last_but_one_reading):
        if(not isChargeRateExceeds(values[i], values[i + 1], md)):
            return False
    return True

def validate_soccurr_reading(values,maxdeltastring):
   if check_none(values)==False:
       return isSocCurrInRange(values,maxdeltastring)
