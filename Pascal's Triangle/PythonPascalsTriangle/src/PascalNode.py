class PascalNode:
    
    __previousLeft = None
    __previousRight = None
    __nextLeft = None
    __nextRight = None
    
    def __init__(self, value):
        self.value = value

    def get_previous_left(self):
        return self.__previousLeft


    def get_previous_right(self):
        return self.__previousRight


    def get_next_left(self):
        return self.__nextLeft


    def get_next_right(self):
        return self.__nextRight


    def get_value(self):
        return self.__value


    def set_previous_left(self, value):
        self.__previousLeft = value


    def set_previous_right(self, value):
        self.__previousRight = value


    def set_next_left(self, value):
        self.__nextLeft = value


    def set_next_right(self, value):
        self.__nextRight = value


    def set_value(self, value):
        self.__value = value


    def del_previous_left(self):
        del self.__previousLeft


    def del_previous_right(self):
        del self.__previousRight


    def del_next_left(self):
        del self.__nextLeft


    def del_next_right(self):
        del self.__nextRight


    def del_value(self):
        del self.__value

    previousLeft = property(get_previous_left, set_previous_left, del_previous_left, "previousLeft's docstring")
    previousRight = property(get_previous_right, set_previous_right, del_previous_right, "previousRight's docstring")
    nextLeft = property(get_next_left, set_next_left, del_next_left, "nextLeft's docstring")
    nextRight = property(get_next_right, set_next_right, del_next_right, "nextRight's docstring")
    value = property(get_value, set_value, del_value, "value's docstring")
    
        