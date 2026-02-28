class Symbol:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Rule:
    def __init__(self, symbol: Symbol, product: tuple):
        self.symbol = symbol
        self.product = product

    def apply(self):
        return self.product


class RuleSet:
    rules = set()

    def __init__(self, rules: set = set()):
        self.rules = rules

    def add_rule(self, rule: Rule):
        self.rules.add(rule)


class Grammar:
    def __init__(self, name: str, start_symbol: Symbol, rules: RuleSet):
        self.name = name
        self.start_symbol = start_symbol
        self.rules = rules


if __name__ == "__main__":
    print("main")
