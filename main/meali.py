class code_meali:

    def __init__(self, Code):
        self.code = Code

    def nano(code):

        code = str(code)
        if not code.isnumeric() or len(code) != 10:
            return "The national code is incorrect"

        total = 0
        count = int(code[-1])
        for d, index in zip(code, range(10, 1, -1)):
            total += int(d) * index

        remis = total % 11
        if remis < 2:
            if remis == count:
                return "The national code is correct"
        else:
            if 11 - remis == count:
                return "The national code is correct"

            return "The national code is incorrect"

