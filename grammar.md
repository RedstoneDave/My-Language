# Special Kratoma Grammar

This document is for the pieces of grammar that are hard to be put into `grammar.ebnf`.

## Reflexive Prefix

A reflexive prefix could be added to a verb or stative verb to indecate the accusative or dative of the verb to be a reflexive pronoun. The rule of the prefix is shown below:

- accusative:
  - if the word begins with a consonant, then an `a` is added to the beginning;
  - if the word begins with a vowel, then an `ak` is added to the beginning;
- dative:
  - if the word begins with a consonant, then an `aw` is added to the beginning;
  - if the word begins with a vowel, then an `ab` is added to the beginning.

## “Plug-in” Clause

This consept is similar to the “noun clause” in English, however, “plug-in” clauses can take place of any part of speech. This allows speakers to refer to some uncertain actions or properties without the form of auxiliary verbs with nouns.

The “plug-in” words are `bru` for `sokan` and `unekin`, `brub` for `burab`, `bruk` for `mosrab` and `bruva` for `gasaru`. A clause with a “plug-in” word can change the predicate into the “complex type” (the one used in the conditional clause) and add an `-m` to it to modify the same “plug-in” word.

## Numeral Combination Rule

As one of the characteristic pieces of grammar, `unekin`s take a special rule to combine together.

For numbers less than a hundred thousand, distinct words are used, these words are formed using a rule similar to that of Chinese, each decimal digit joins with the power of ten and those are connected together. For example: the number `1926` is `ukegumunedari` (1-thousand-9-hundred-2-ten-6), each syllable stands for a part.

Along with “pure” numerals that can stand alone, there are “operating” numerals that need one or more numbers to form complete structures. For example, in order to represent lare numbers like `998244353`, the operator `to` is used, this operator takes two numbers `x` and `y` and returns `x*100000+y`, and `998244353` is `gukegumufedane dodedokekimutadaki to`. Other operating numerals include “plus”, “multiply”.

## Verb Paradigms

A verb paradigm (`tondosma baros`) describes a set of verbs sharing a same argument format. Kratoma has following verb paradigms.

- `hat baros`
  - \*AGEN
- `zit baros`
  - \*AGEN PAT
- `ep baros`
  - \*AGEN ALLA/TERM
- `kodes baros`
  - \*AGEN ALLA
- `retar baros`
  - AGEN
- `tom baros`
  - \*AGEN PAT=“speech”
- `latam baros`
  - \*DAT AGEN PAT=“speech”
- `muk baros`
  - \*AGEN
- `tesam baros`
  - \*PAT AGEN
- `nyak baros`
  - \*AGEN PAT

Yet there are still several isolated cases, which are:

- `usat`
  - \*AGEN DAT PAT
- `ivak`
  - \*DAT AGEN PAT
- `der`
  - \*PAT ALLA AGEN
