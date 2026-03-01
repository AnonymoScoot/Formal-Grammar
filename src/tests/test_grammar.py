import unittest
from main.grammar import *


class TestGrammar(unittest.TestCase):

    def test_symbol(self):
        symbol1 = Symbol("A")
        symbol2 = Symbol("A")
        symbol3 = Symbol("B")

        self.assertEqual(symbol1, symbol2)
        self.assertNotEqual(symbol1, symbol3)

        self.assertEqual(str(symbol1), "A")

    def test_rule(self):
        symbol1 = Symbol("A")
        rule1 = Rule(symbol1, ("a", symbol1))

        symbol2 = Symbol("A")
        rule2 = Rule(symbol2, ("a", symbol2))

        symbol3 = Symbol("B")
        rule3 = Rule(symbol3, ("a", symbol3))

        symbol4 = Symbol("A")
        rule4 = Rule(symbol4, ("b", symbol4))

        symbol5 = Symbol("A")
        rule5 = Rule(symbol5, ("a", "b", "c"))

        symbol6 = Symbol("C")
        rule6 = Rule(symbol6, ("a", Symbol("B"), Symbol("C")))

        self.assertEqual(rule1, rule2)
        self.assertNotEqual(rule1, rule3)
        self.assertNotEqual(rule1, rule4)

        self.assertEqual(str(rule1), "A -> 'a'A")
        self.assertEqual(str(rule2), "A -> 'a'A")
        self.assertEqual(str(rule3), "B -> 'a'B")
        self.assertEqual(str(rule4), "A -> 'b'A")
        self.assertEqual(str(rule5), "A -> 'a''b''c'")
        self.assertEqual(str(rule6), "C -> 'a'BC")

    def test_ruleset(self):
        symbol1 = Symbol("A")
        rule1 = Rule(symbol1, ("a", symbol1))
        rule2 = Rule(symbol1, ("a", "b", "c"))
        ruleset1 = RuleSet(rule1, rule2)

        symbol2 = Symbol("A")
        rule3 = Rule(symbol2, ("a", symbol2))
        rule4 = Rule(symbol2, ("a", "b", "c"))
        ruleset2 = RuleSet(rule3, rule4)

        symbol3 = Symbol("B")
        rule5 = Rule(symbol3, ("a", symbol3))
        rule6 = Rule(symbol3, ("a", "b", "c"))
        ruleset3 = RuleSet(rule5, rule6)

        symbol4 = Symbol("A")
        rule7 = Rule(symbol4, ("b", symbol4))
        rule8 = Rule(symbol4, ("a", "b", "c"))
        ruleset4 = RuleSet(rule7, rule8)

        symbol5 = Symbol("A")
        rule9 = Rule(symbol5, ("a", symbol5))
        rule10 = Rule(symbol5, ("a", "b", "d"))
        ruleset5 = RuleSet(rule9, rule10)

        self.assertEqual(ruleset1, ruleset2)
        self.assertNotEqual(ruleset1, ruleset3)
        self.assertNotEqual(ruleset1, ruleset4)
        self.assertNotEqual(ruleset1, ruleset5)

        self.assertEqual(str(ruleset1), "(A -> 'a'A, A -> 'a''b''c')")
        self.assertEqual(str(ruleset2), "(A -> 'a'A, A -> 'a''b''c')")
        self.assertEqual(str(ruleset3), "(B -> 'a'B, B -> 'a''b''c')")
        self.assertEqual(str(ruleset4), "(A -> 'b'A, A -> 'a''b''c')")
        self.assertEqual(str(ruleset5), "(A -> 'a'A, A -> 'a''b''d')")

    def test_grammar(self):
        symbol1 = Symbol("A")
        rule1 = Rule(symbol1, ("a", symbol1))
        rule2 = Rule(symbol1, ("a", "b", "c"))
        ruleset1 = RuleSet(rule1, rule2)
        grammar1 = Grammar("G", symbol1, ruleset1)

        symbol2 = Symbol("A")
        rule3 = Rule(symbol2, ("a", symbol2))
        rule4 = Rule(symbol2, ("a", "b", "c"))
        ruleset2 = RuleSet(rule3, rule4)
        grammar2 = Grammar("G", symbol2, ruleset2)

        symbol3 = Symbol("B")
        rule5 = Rule(symbol3, ("a", symbol3))
        rule6 = Rule(symbol3, ("a", "b", "c"))
        ruleset3 = RuleSet(rule5, rule6)
        grammar3 = Grammar("G", symbol3, ruleset3)

        symbol4 = Symbol("A")
        rule7 = Rule(symbol4, ("b", symbol4))
        rule8 = Rule(symbol4, ("a", "b", "c"))
        ruleset4 = RuleSet(rule7, rule8)
        grammar4 = Grammar("G", symbol4, ruleset4)

        symbol5 = Symbol("A")
        rule9 = Rule(symbol5, ("a", symbol5))
        rule10 = Rule(symbol5, ("a", "b", "d"))
        ruleset5 = RuleSet(rule9, rule10)
        grammar5 = Grammar("G", symbol5, ruleset5)

        symbol6 = Symbol("A")
        rule11 = Rule(symbol6, ("a", symbol6))
        rule12 = Rule(symbol6, ("a", "b", "c"))
        ruleset6 = RuleSet(rule11, rule12)
        grammar6 = Grammar("F", symbol6, ruleset6)

        self.assertEqual(grammar1, grammar2)
        self.assertNotEqual(grammar1, grammar3)
        self.assertNotEqual(grammar1, grammar4)
        self.assertNotEqual(grammar1, grammar5)
        self.assertNotEqual(grammar1, grammar6)

        self.assertEqual(
            str(grammar1), "Grammar: G, A, (A -> 'a'A, A -> 'a''b''c')")
        self.assertEqual(
            str(grammar2), "Grammar: G, A, (A -> 'a'A, A -> 'a''b''c')")
        self.assertEqual(
            str(grammar3), "Grammar: G, B, (B -> 'a'B, B -> 'a''b''c')")
        self.assertEqual(
            str(grammar4), "Grammar: G, A, (A -> 'b'A, A -> 'a''b''c')")
        self.assertEqual(
            str(grammar5), "Grammar: G, A, (A -> 'a'A, A -> 'a''b''d')")
        self.assertEqual(
            str(grammar6), "Grammar: F, A, (A -> 'a'A, A -> 'a''b''c')")

if __name__ == "__main__":
    unittest.main()
