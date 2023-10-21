from module_1 import function_1
# only 'function_1' has been impported from 'module_1'
function_1()

from module_1 import function_2
# only 'function_2' has been impported from 'module_1'
function_2()

from module_2 import function_1
# only 'function_1' has been impported from 'module_2'
# this import will overwrite the first import from 'module_1' as both fucntions have the same name
function_1()