# Kratoma - A Constructed Language for an Isekai

Kratoma is a constructed “natural” language rather than a programming language.

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
  - and `fozu beuye nociken` means “I'm abandoned by the society” where `beu` means “the world” and “the society” and `noc` means “to abandon; to desert”, `-iken` makes a verb passive
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
- `vebiken`
  - `-iken` means “to be done” and `vebiken` is a `burab`
  - Just in case you forgot this, “by ...” is represented using `ye`
  - e.g. `fozu beuye nociken` means “I'm abandoned by the society”
- `vebikaz`
  - `-ikaz` means “to let do” and `vebikaz` is a `burab`
  - e.g. `fozu zedo mupikaz` means “I let him sleep”, notice that “him” here is represented with `do` instead of `bu`
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
