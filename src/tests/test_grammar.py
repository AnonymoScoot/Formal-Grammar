import unittest
from main.grammar import *


class TestGrammar(unittest.TestCase):

    def test_symbol(self):
        symbol = Symbol("A")
        self.assertEqual(symbol.name, "A")

    def test_rule(self):
        symbol = Symbol("A")
        rule = Rule(symbol, ("a", symbol))
        product = rule.apply()

        self.assertEqual(product, ("a", symbol))

    def test_ruleset(self):
        symbol = Symbol("A")
        rule1 = Rule(symbol, ("a", symbol))
        rule2 = Rule(symbol, ("a", "b", "c"))
        ruleset1 = RuleSet(set((rule1, rule2)))

        self.assertEqual(ruleset1.rules, set((rule1, rule2)))

        ruleset2 = RuleSet()
        ruleset2.add_rule(rule1)
        ruleset2.add_rule(rule2)

        self.assertEqual(ruleset2.rules, set((rule1, rule2)))

    def test_grammar(self):
        symbol = Symbol("A")
        rule1 = Rule(symbol, ("a", symbol))
        rule2 = Rule(symbol, ("a", "b", "c"))
        ruleset = RuleSet((rule1, rule2))
        grammar = Grammar("G", symbol, ruleset)

        self.assertEqual(grammar.name, "G")
        self.assertEqual(grammar.start_symbol, symbol)
        self.assertEqual(grammar.rules, ruleset)


if __name__ == "__main__":
    unittest.main()
