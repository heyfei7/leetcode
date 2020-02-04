
class TestSuite:

    def __init__(self, func):
        self.func = func
        self.tests = []

    def add_test(self, input, output):
        self.tests.append({"input":input, "output":output})

    def run_tests(self):
        passed = 0
        for t in self.tests:
            result = self.func(t["input"])
            if t["output"] == result:
                print("You passed!")
                passed += 1
            else:
                print("You failed!")
            print("Input:", t["input"])
            print("Output:", result)
            print("Expected:", t["output"])
            print("-" * 50)
        print("You passed " + str(passed) + " out of " + str(len(self.tests)) + " tests")