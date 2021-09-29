class Singleton:
    class __impl:

        def __init__(self):
            pass

        def spam(self):
            return id(self)

        # storage of the instance reference

    __instance = None

    def __init__(self):
        if Singleton.__instance is None:
            # Create and remember instance
            Singleton.__instance = Singleton.__impl()

            # Store instance reference as the only memeber in the handle

            # self.__dict__['_Singleton__instance'] = Singleton.__instance

    def __getattr__(self, attr):
        """Delegate access to implementation"""
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """Delegate accesss to implementation"""
        return setattr(self.__instance, attr, value)


sing1 = Singleton()
sing2 = Singleton()

print(id(sing1), sing1.spam())
print(id(sing2), sing2.spam())

sing1.x = 5
print(sing1.x)
