from random import randint

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []
 class TestDataUniqueValues(object):

    data = set()
    while len(data) < 10:
        data.add(randint(0, 100))

    @staticmethod
    def get_array():
        # complete this function
        data = TestDataUniqueValues.data
        return list(data)

