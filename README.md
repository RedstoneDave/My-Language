# Kratoma - A Constructed Language for an Isekai

Kratoma is a constructed “natural” language rather than a programming language. The language part of this repository is published under [CC BY-SA 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode), and if one day the author writes some code about the language, that code will be published under MIT License.

## Idea

Kratoma is a language used by people in an isekai where exists “krin”, a power people in our world may consider as magic. Some people are born with the ability to master krin (called “krink”), the others are born without the power (called “krinaf”).

Kratoma reflects the views of the people in the world, and ultimately reflects some thoughts of the author itself (yes, the author uses “it” as its pronoun).

There are no words that correspond to “good” or “bad”, “right” or “wrong”, “must” or “forbid”, instead, more specific feeling describing, logic or value describing and conditional expressions are used.

## Phonology

### Consonants

The table below shows the consonant phonemes of Kratoma.

|             | Bilabial | Labialdental | Alveolar | PastAlveolar | Palatal | Velar | Glottal |
| ----------- | -------- | ------------ | -------- | ------------ | ------- | ----- | ------- |
| Plosive     | pʰ b     |              | tʰ d     |              |         | kʰ ɡ  |         |
| Nasal       | m        |              | n        |              |         |       | N/A     |
| Fricative   |          | f v          | s z      | ʃ(c) ʒ(l)    |         |       | h       |
| Tap or flap |          |              | ɾ        |              |         | N/A   | N/A     |
| Approximant | w        |              |          |              | j(y)    |       | N/A     |

and the list here shows some variations:

- /p\b/ = \[ɸ\] (`\b` here means the end of a word, the same below)
- /m(a)/ = \[β(a)\]
- /m(fv)/ = \[ɱ(fv)\]
- /n(kɡ)/ = \[ŋ(kɡ)\]
- /n\b/ = \[ɴ\]
- /sʲ/ = \[ɕ\]
- /zʲ/ = \[ʑ\] or \[d͡ʑ\]
- /(ptk)ɾ(a)/ = \[(ptk)χ(ɑ)\]
- /ɾ\b/ = \[l\]

### Vowels

The table below shows the vowel phonemes of Kratoma. The schwa here is pronounced only when it's hard to pronounce two consonants successively.

|        | Front | Mid | Back |
| ------ | ----- | --- | ---- |
| Top    | i     |     | ɯ    |
| Middle | e̞     | (ə) | o̞    |
| Bottom |       | ä   |      |

and the list here shows some variations:

- /(j)ɯ/ = \[(j)ɨ\]

## Orthography

There are two writing systems in Kratoma, one is called `hwancuma` (lit. common writing) and the other is called `krincuma` (lit. krin(magic) writing).

the file of the fonts are to be stored in the repository.

## Grammar

Kratoma is an agglutinative language highly relying on case particals and auxiliary words. Basic grammar forms can be found in the file `grammar.ebnf`.

Kratoma has five parts of speech, `sokan` (nouns), `burab` (verbs), `mosrab` (stative verbs), `garasu` (adjectives), `unekin` (numerals).

### Nouns

In Kratoma, nouns are called `sokan`, `sokan` is the only type of word that can have case particals after one. An example of `sokan` is `fesa` (meaning “human”), here are the forms of the word `fesa`:

- `fesazu`
  - `zu` indecates the topic, a similar example is the partical “は” in Japanese.
  - e.g. `fozu raez`, means “I'm tall”, where `fo` is the pronoun “me” and `raez` is the adjective “tall”.
- `fesasu`
  - `su` indecates the subject (or nominative), a similar example is the partical “が” in Japanese.
  - In dependent clauses, `su` is more frequently used than `zu`
  - e.g. `fesazu kasasu udaz` means “Human have long legs” (lit. humans (are of which) legs (are) long), where `kasa` means “leg” and `udaz` is the adjective “long”.
- `fesasem`
  - `sem` indecates the instrumental (ie. the tool), and the manner of an action
- `fesako`
  - `ko` indecates the allative (ie. the direction)
  - This is also the case meaning “become”
  - e.g. `fozu zekeko kasep` means “I walk to there” and `fozu fesako der` means “I become a human”
- `fesabu`
  - `bu` indecates the direct object (or accusative)
  - e.g. `fozu kilabu zazit` means “I eat fish”
- `fesado`
  - `do` indecates the dative, as “me” in “you give me the book”, and purpose is also indecated by `do`, though the latter usually appears earlier
  - e.g. `fozu zedo lavbu usat` means “I give them a book” where `ze` is a singular, sexually neutral pronoun, and `lav` means “book”
  - and `fozu kado ocom` means “I sing for you” where `ka` means “you”.
- `fesacu`
  - `cu` indecates the position, also time.
  - e.g. `fozu fokecu muk` means “I am here” (lit. I exist at here)
- `fesaye`
  - `ye` indecates the ablative, meaning “from”, and the ergative in passive forms (as “by ...” in English)
  - e.g. `fozu zekeye vep` means “I come from there” where `zeke` means “there” and `vep` means “to come”
  - and `fozu beuye nocins` means “I'm abandoned by the society” where `beu` means “the world” and “the society” and `noc` means “to abandon; to desert”, `-ins` makes a verb passive
- `fesawe`
  - `we` indecates the terminative, meaning “until”
  - e.g. `zezu rusyawe furvusk` means “He has been young until today” where `rusya` means “today” and `furva` means “young” and `-usk` means “have been”

Forms above are the “adverbial” forms that directly modifies the predicate (ie. the center of a sentence), while the ones below go to other positions.

- `fesama`
  - `ma` indecates the genetive case (ie. belonging)
  - e.g. `fesama kasazu udaz` means “Human's legs are long”, in which “leg” is the subject and the topic.
- `fesanuva`
  - `-nuva` after a noun transforms it into an adjective, meaning “like ...” or say “-(l)y” as in “friendly”
  - Examples will be given in the section about adjectives.
- `fesaluva`
  - `-luva` after a noun also transforms it into an adjective, meaning “about”
  - Examples will be given in the section about adjectives.

And `sokan`s can take the part of predicate, such as `fozu fesa`, meaning “I'm human”.

### Verbs

There are two parts of speech correspond to verbs in English, `burab` and `mosrab`, this section is about `burab`, verbs that can tell apart “before” and “after”. An example of `burab` is `veb`(meaning “to do”). Here are the forms of the word `veb`.

- `vebu`
  - `u` after a `burab` enables it to join with other words, to modify the predicate, and to form a dependent clause.
  - Most conjugations are formed by the form `vebu-` with an auxiliary word (in the file `auxiliary words.yaml`).
- `vebem`
  - `-em` basically means “to un(do)” and `vebem` is also a `burab`.
- `veben`
  - `-en` means “not to do” and `veben` is a `mosrab`.
  - e.g. `fozu mupen` means “I don't sleep” where `mup` means “to sleep”.
- `vebins`
  - `-ins` means “to be done” and `vebins` is a `burab`
  - Just in case you forgot this, “by ...” is represented using `ye`
  - e.g. `fozu beuye nocins` means “I'm abandoned by the society”
- `vebiks`
  - `-iks` means “to let do” and `vebiks` is a `burab`
  - e.g. `fozu zedo mupiks` means “I let him sleep”, notice that “him” here is represented with `do` instead of `bu`
- `vebod`
  - `-od` means “in order to do” and `vebod` is a `mosrab`
- `veba`
  - `-a` transforms a `burab` to a noun, as “-ing” or “to -” or “-ion” or “-ment”
- `vebin` / `vebwa`
  - these two transform a `burab` to a noun, as “-er” in English
  - `-in` indecates a human executor, and `-wa` indecates non-human executor.
- `vebas`
  - `-as` is similar to “-ee” in English
  - It gives the absolutive (ie. the object of a transive verb and the subject of an intransive verb)
- `vebo`
  - `-o` enables a `burab` to modify a noun
  - e.g. `kasepo fesa` means “running person” where `kasep` means “to run”.
- `vebai`
  - `-ai` means will or wish.
  - e.g. `kasai` means “Arise!”, and `retarai` means “Please rain!”
- `veban`
  - `-an` means negative will or wish.
  - e.g. `retaran` means “Please don't rain!”

### Stative Verbs

This section is about `mosrab`, the stative verbs that cannot tell apart “before” or “after”. An example of `mosrab` is `muk` (meaning “to be; to exist”). Here are the forms of the word `muk`.

- `muke`
  - `e` after a `mosrab` enables it to join with other words, to modify the predicate and to form a dependent clause, just like `u` after a `burab`
- `on`
  - `on` means “not to be”, and with words other than `muk`, its straightly used after the word, yet `on` is used instead of `mukon`. `on` is a `mosrab`.
  - e.g. `fozu kavon` means “I'm not standing” where `kav` means “to be standing”
- `mukas`
  - this is the same as the `as` above, representing the absolutive.
- `mukyu`
  - `-yu` transforms a `mosrab` to a noun, the same as `veba` above.
- `mukumva`
  - `-umva` transforms a `mosrab` to an adjective, this allows it to use comparison.
- `muki`
  - `-i` enables a `mosrab` to modify a noun, just like `o` after a `burab`.
  - e.g. `muki fesa` means “existing person”

### Adjectives

Adjectives in Kratoma are called `gasaru`, the semantic division between `gasaru` and `mosrab` is not clear, and these two can transform to each other. An example of `gasaru` is `krava` (meaning “blue; azure; cute”).

Adjectives have two basic forms, one is the modifier form, the other is the predicative form. In dictionaries, adjectives are shown in the first form, which ends in `-va`, the second form is obtained by replacing the `-va` into `-z`. For example, the modifier form `krava` has a corresponding predicative form `kraz`. Other variants are shown below.

- `kravu`
  - this form is the same as the `muke` and `vebu` form.
  - e.g. `luvu kasep` means “to walk fast” where `luva` means “fast” and `kasep` means “to walk”
- `kranava`
  - `-nava` is the negative suffix, and `kranava` means “not blue”
  - e.g. `fozu furnava` means “I'm not young”
- `krakseva`
  - `-kseva` is the comparative suffix, and `krakseva` means “more blue”
  - e.g. `krinzu kreye kraksez` means “Krin is more blue than water”, a proverb which means “the younger generation have more energy and opportunities”
- `kragruva`
  - `-gruva` is the superlative suffix, and `kragruva` means “most blue”
  - e.g. `fozu lugruvu kasep` means “I walk the fastest”.
- `kravan`
  - `-van` makes the adjective an abstract noun, yet `kra` it self is the noun “blue” so `kravan` is basically never used.
- `kravei`
  - `-vei` makes the adjective an instance noun, and `kravei` means “something blue”
  - e.g. `fozu kraveibu tesin` means “I like blue things” or “I like cute things”

### Numerals

Numerals in Kratoma are called `unekin`, this word is formed from the words for 1, 2 and 3. However, `unekin` has more words than numbers, concepts like “many” `mo`, “part” `ecu`, “same” `wa`, “common” `hwa` are also `unekin`s. Let's take the word `u` (meaning “one”) for example. Here are the forms of the word.

- `un`
  - `-n` enables an `unekin` to modify a noun.
  - e.g. `un fesa` means “a person”
- `uk`
  - `-k` transforms an `unekin` into a noun
  - e.g. `fonzu wok` means “this is all”, where `fon` means “this” and `wo` means “all”.
- `uceva`
  - `-ceva` transforms an `unekin` into an adjective
  - e.g. `mocekseva` means “more”

### Clauses

Kratoma is predicate-based, every other component in a sentence is analysed to be an adverbial (ie. modifier) of the predicate. The predicate of a clause could be a `sokan`, `burab`, `mosrab` or `-z` form of `gasaru`, as for `unekin`, just add a `-k` after it to transform it into a `sokan`.
