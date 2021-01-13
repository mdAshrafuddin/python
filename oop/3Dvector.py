class MutableVector3D:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
    
    def sum(self, delta_x, delta_y, delta_z):
        self.__x += delta_x
        self.__y += delta_y
        self.__z += delta_z
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x += x
    
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y
    
    @property
    def z(self):
        return self.__z
    
    @z.setter
    def z(self, z):
        self.__z = z

    @classmethod
    def equal_elements_vector(cls, value):
        return cls(value, value, value)

    @classmethod
    def origin_vector(cls):
        return cls.equal_elements_vector(1)

object = MutableVector3D.origin_vector()
object.sum(5, 10, 15)
print(object.x, object.y, object.z)