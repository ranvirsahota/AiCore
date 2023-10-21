import time
print('import time: ' + str(time.time()))

from time import time as time_time
print('from time import time as time_time: ' + str(time_time()))

from datetime import time
# print(time.time())
# ^returns: AttributeError:type object 'datetime.time' has no attribute time
# This is because both time calls are trying to call different functions with the same name.
# The first time you were calling time.time(), which is a function that returns the current timestamp.
# The second time you were calling the time() class, which returns an object with the time you specified. If you want to tell them apart, you can give them aliases. 
print('from datetime import time: ' + str(time()))

from datetime import time as datetime_time
print('from datetime import time as datetime_time: ' + str(datetime_time()))