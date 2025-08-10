import sys
class CustomException(Exception):
    pass 

class YourException(ValueError):
    pass

try:
    print('Statement #1')
    raise YourException('No value Passed')
    print('Statement #2')
except (CustomException, ValueError) as e:
    print(f'1. Exception {e}--> {sys.exc_info()[1]}')
except Exception as ve:
    print(f'3. {ve} --> {sys.exc_info()[1]}')

