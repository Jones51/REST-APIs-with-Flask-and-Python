class ClassTest:
    def instace_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called classe_method of {cls}")

    @staticmethod
    def static_method():
        print("Called stsatic_method")

test = ClassTest()
test.instace_method()
ClassTest.instace_method(test)

ClassTest.class_method()

ClassTest.static_method()