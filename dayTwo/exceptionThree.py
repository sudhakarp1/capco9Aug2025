import sys
class CustomException(Exception):
    pass 

class YourException(ValueError):
    pass

try:
    print('Statement #1')
    raise YourException('No value Passed')
    print('Statement #2')
except CustomException as e:
    print(f'1. Exception {e}')
except ValueError as ve:
    print(f'3. {ve}')
except Exception as e:
    print(f'2. Exception {e}')
