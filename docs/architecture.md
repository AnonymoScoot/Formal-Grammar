# Architecture

The Python Formal Language library is designed to provide a simple and extensible way of working with formal grammars.

## Grammar

The `Grammar` class is the core component of the library. It represents a formal grammar and provides methods for defining the grammar, generating derivations, validating strings and converting grammars.

Supporting classes:

- `Rule` represents a rule. It is a mapping from a symbol to an ordered set of symbols.
- `RuleSet` represents a set of rules. One of the inputs to grammar.
- `Symbol` represents a terminal or nonterminal symbol. Terminal symbols are represented as strings. Non-terminal symbols do not terminate into strings.

Example Grammar:
- Nonterminals: {A}
- Terminals: {'a', 'b', 'c'}
- Production rules: A → aA, A → abc
- Start symbol: A

### Process of constructing a grammar

Create symbols: `A`
Create rules:
- Rule 1:
    - Symbol: `A`
    - Product: `["a", A]`
- Rule 2:
    - Symbol: `A`
    - Product: `["a", "b", "c"]`
Create a rule set:
- Add Rule 1 and Rule 2 into the rule set.
Create a grammar:
- Give a name, add a starting symbol `A`, add the rule set.

## Parser



## Derivation



## Validation



## Interactions


## Testing

The library is tested using the `unittest` framework. Unit tests are written for each component of the library and are placed in the `src/test` directory.
