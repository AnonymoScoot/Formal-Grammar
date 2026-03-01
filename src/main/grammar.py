class Symbol:
    def __init__(self, name: str):
        self.__name = name

    def __eq__(self, value):
        if not isinstance(value, Symbol):
            return False

        return self.__name == value.name

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name


class Rule:
    def __init__(self, symbol: Symbol, product: tuple):
        self.symbol = symbol
        self.product = product

    def __eq__(self, value):
        if not isinstance(value, Rule):
            return False

        if self.symbol != value.symbol:
            return False

        if len(self.product) != len(value.product):
            return False

        for i in range(len(self.product)):
            if self.product[i] != value.product[i]:
                return False

        return True

    def __str__(self):
        return f"{self.symbol} -> {''.join([x.name if isinstance(x, Symbol) else f"'{x}'" for x in self.product])}"


class RuleSet:
    def __init__(self, *rules: Rule):
        self.rules = rules

    def __eq__(self, value):
        if not isinstance(value, RuleSet):
            return False

        if len(self.rules) != len(value.rules):
            return False

        for i in range(len(self.rules)):
            if self.rules[i] != value.rules[i]:
                return False

        return True

    def __str__(self):
        return "(" + ", ".join([str(x) for x in self.rules]) + ")"


class Grammar:
    def __init__(self, name: str, start_symbol: Symbol, rules: RuleSet):
        self.name = name
        self.start_symbol = start_symbol
        self.rules = rules

    def __eq__(self, value):
        if not isinstance(value, Grammar):
            return False

        if self.name != value.name:
            return False

        if self.start_symbol != value.start_symbol:
            return False

        if self.rules != value.rules:
            return False

        return True

    def __str__(self):
        return f"Grammar: {self.name}, {self.start_symbol}, {self.rules}"


if __name__ == "__main__":
    print("main")
