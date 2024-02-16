class TC:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    @classmethod
    def __checkval(cls, x):
        if type(x) in (int, float):
            return True
        else:
            raise ValueError("ЭТО НЕ ЧИСЛА, ДЭБ!")
    
    @classmethod
    def __checkz(cls, x):
        if x > 0:
            return True
        else:
            raise ValueError("ЗАМЕЧАНО ОТРИЦАТЕЛЬНОЕ ЗНАЧЕНИЕ IQ!!!")
    
    def itr(self, x, y, z):
        if self.__checkval(x) and self.__checkval(y) and self.__checkval(z) and self.__checkz(x) and self.__checkz(y) and self.__checkz(z) and (x + y > z) and (x + z > y) and (z + y > x):
            print("УРАААААА, ПОБЕДА!!!")
        else:
            raise ValueError("АБОБА, ПОПРОБУЙ ДРУГИЕ ЧИСЛА")

trig = TC(0, 0, 0)
trig.itr(3, 4, 5)