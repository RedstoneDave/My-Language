# Kratoma Grammar

This is a complete grammar document for Jaketo.

Jaketo has five parts of speech, `sokan` (nouns), `buraj` (verbs), `mosraj` (stative verbs), `garasu` (adjectives), `unekin` (numerals).

## Nouns

In Jaketo, nouns are called `sokan`, `sokan` is the only type of word that can have case particals after one. An example of `sokan` is `fesa` (meaning “human”).

Here are the forms of the word `fesa`:

- `fesazu`
  - `zu` indecates the topic, a similar example is the partical “は” in Japanese.
  - e.g. `prazu raezy`, means “I’m tall”, where `pra` is the pronoun “me” and `raezy` is the adjective “tall”.
- `fesasu`
  - `su` indecates the subject (or the “direct case”), a similar example is the partical “が” in Japanese.
  - In dependent clauses, `su` is more frequently used than `zu`
  - e.g. `fesazu kasasu udazy` means “Human have long legs” (lit. humans (are of which) legs (are) long), where `kasa` means “leg” and `udaz` is the adjective “long”.
  - To avoid ambiguity, the sentence above can also be said as `fesazu bruma kasasu udazy`, the `bru-ma` here indecates which part the topic belongs to, specifically the genitive for the word `kasa`.
- `fesa'je`
  - `je` indecates the ablative, meaning “from”, and the ergative in non-ergative trigger forms (as “by ...” in English)
  - e.g. `prazu zeke'je vepq` means “I come from there” where `zeke` means “there” and `vep` means “to come”
  - and `prazu bew'je nocinsq` means “I’m abandoned by the society” where `bew` means “the world” and “the society” and `noc` means “to abandon; to desert”, `-insq` makes a verb passive
- `fesabu`
  - `bu` indecates the accusative (i.e. direct object)
  - e.g. `prazu ki'jabu zazitq` means “I eat fish”
- `fesako`
  - `ko` indecates the allative (ie. the direction)
  - This is also the case meaning “become”, and actions that creates something (i.e. it didn't exist before, may be vague in some sences), which is similar to the translative case.
  - e.g. `prazu zekeko kasepq` means “I walk to there”
  - and `prazu fesako derq` means “I become a human”
  - and `prazu ewrawko tlamukq` means “I wrote a letter” while `prazu ewrawbu majsukq` means “I read a letter”
- `fesado`
  - `do` indecates the dative, as “me” in “you give me the book”, and purpose is also indecated by `do`, though the latter usually appears earlier
  - e.g. `prazu zedo lawbu usatq` means “I give them a book” where `ze` is a singular, sexually neutral pronoun, and `law` means “book”
  - and `prazu kado ocomq` means “I sing for you” where `ka` means “you”.
- `fesasem`
  - `sem` indecates the instrumental (ie. the tool), and the manner of an action
- `fesacu`
  - `cu` indecates the locative (i.e. position or time).
  - e.g. `prazu prakecu mjukq` means “I am here” (lit. I exist at here)
- `fesakaw`
  - `kaw` indecates the comitative, as “with me” in “He went on a walk with me”, used in neutral cases or cases where the candidates are of the same attention.
  - e.g. `prakaw kasepq` means “to walk with me”
- `fesanow`
  - `now` indecates the “anti-comitative”, as “against me” in “He fought against me”, used in cases there the candidates are of the opposite attention.
  - e.g. `awrova bewnow wakitq` means “to fight against the old world”
- `fesa'we`
  - `we` indecates the terminative, meaning “until”
  - e.g. `zezu rusya'we fujvusykq` means “He has been young until today” where `rusya` means “today” and `fuj(vu)` means “young” and `-sykq` means “have been”
- `fesa'ja`
  - `ja` indecates the identical (or say adverbial), meaning “as”
  - e.g. `kazu pra'ja wamizy` means “you are the same as me”.

The particals of the first six forms can be omitted if the words are in a proper order (more shown in the [verb paradigms section](#verb-paradigms)).

Forms above are the “adverbial” forms that directly modifies the predicate (ie. the center of a sentence), while the ones below go to other positions.

- `fesama`
  - `ma` indecates the genetive case (ie. belonging)
  - e.g. `fesama kasazu udazy` means “Human’s legs are long”, in which “leg” is the subject and the topic.
- `fesanuva`
  - `-nuva` after a noun transforms it into an adjective, meaning “like ...” or say “-(l)y” as in “friendly”
  - Examples will be given in the section about adjectives.
- `fesaluva`
  - `-luva` after a noun also transforms it into an adjective, meaning “about”
  - Examples will be given in the section about adjectives.

And `sokan`s can take the part of predicate, such as `prazu fesa`, meaning “I’m human”.

## Verbs

There are two parts of speech correspond to verbs in English, `buraj` and `mosraj`, this section is about `buraj`, verbs that can tell apart “before” and “after”. An example of `buraj` is `vebq`(meaning “to do”). Here are the forms of the word `vebq`.

- `vebu`
  - `u` after a `buraj` enables it to join with other words, to modify the predicate, and to form a dependent clause.
  - Most conjugations are formed by the form `vebu-` with an auxiliary word (in the file `auxiliary words.yaml`).
- `vebenq`
  - `-enq` means “not to do” and `vebenq` is a `mosraj`.
  - e.g. `prazu mupenq` means “I don’t sleep” where `mupq` means “to sleep”.
- `vebelhq`
  - `-elhq` means “before doing” and `vebelhq` is a `mosraj`
  - e.g.
- `vebodq`
  - `-odq` means “in order to do” and `vebodq` is a `mosraj`
- `veba`
  - `-a` transforms a `buraj` to a noun, as “-ing” or “to -” or “-ion” or “-ment”
- `vebin`
  - these two transform a `buraj` to a noun, as “-er” in English
- `vebas`
  - `-as` is similar to “-ee” in English
  - It gives the accusative
- `vebo`
  - `-o` enables a `buraj` to modify a noun
  - e.g. `kasepo fesa` means “running person” where `kasep` means “to run”.
- `vebaj`
  - `-ai` means will or wish, or a urgent request.
  - e.g. `kasaj` means “Arise!”, and `retaraj` means “Please rain!”
- `veban`
  - `-an` means negative will or wish.
  - e.g. `retaran` means “Please don’t rain!”

there are five triggers for the [symmetrical voice system](https://en.wikipedia.org/wiki/Symmetrical_voice), which are

- `-insq`
  - the accusative trigger, meaning “to be done”.
  - e.g. `prazu bew'ye nocinsq` means “I’m abandoned by the society”
- `-inasq`
  - the allative trigger, but almost always used for the becoming and creating sence.
  - e.g. `ewrawzu pra'je tlaminasq` means “The letter is written by me”
- `-ispq`
  - the instrumental trigger, meaning “to be used to do”.
  - e.g. `ovizu praje cazobu kawakispq` means “the knife is used to cut the fruit by me”, where `ovi` means “knife”, `cazo` “fruit” and `kawakq` “to cut”.
- `-iztq`
  - the dative trigger voice.
  - e.g. `zezu pra'je lawbu usatiztq` means “He is given a book by me”.
- `-ikesq`
  - the ergative trigger, used where the verb has a default trigger other than the ergative.
  - therefore `vebiks` is invalid.

for `mosraj`s, the `i` becomes `u`

## Stative Verbs

This section is about `mosraj`, the stative verbs that cannot tell apart “before” or “after”. An example of `mosraj` is `mjukq` (meaning “to be; to exist”). Here are the forms of the word `mjukq`.

- `mjuke`
  - `e` after a `mosraj` enables it to join with other words, to modify the predicate and to form a dependent clause, just like `u` after a `buraj`
- `onq`
  - `onq` means “not to be”, and with words other than `mjukq`, its straightly used after the word, yet `onq` is used instead of `mjukonq`. `onq` is a `mosraj`.
  - e.g. `prazu kavonq` means “I’m not standing” where `kavq` means “to be standing”
- `mjukas`
  - this is the same as the `as` above, representing the accusative.
- `mjukiw`
  - `-iw` transforms a `mosraj` to a noun, the same as `veba` above.
- `mjukumva`
  - `-umva` transforms a `mosraj` to an adjective, this allows it to use comparison.
- `mjuki`
  - `-i` enables a `mosraj` to modify a noun, just like `o` after a `buraj`.
  - e.g. `mjuki fesa` means “existing person”

## Adjectives

Adjectives in Jaketo are called `gasaru`, the semantic division between `gasaru` and `mosraj` is not clear, and these two can transform to each other. An example of `gasaru` is `krava` (meaning “blue; azure; cute”).

Adjectives have two basic forms, one is the modifier form, the other is the predicative form. In dictionaries, adjectives are shown in the first form, which ends in `-va`, the second form is obtained by replacing the `-va` with `-zy`. For example, the modifier form `krava` has a corresponding predicative form `krazy`. Other variants are shown below.

- `kravu`
  - this form is the same as the `mjuke` and `vebu` form.
  - e.g. `luvu kasepq` means “to walk fast” where `luva` means “fast” and `kasepq` means “to walk”
- `kranava`
  - `-nava` is the negative suffix, and `kranava` means “not blue”
  - e.g. `prazu fujnazy` means “I’m not young”
- `kraheva`
  - `-kseva` is the comparative suffix, and `kraheva` means “more blue”
  - e.g. `krinzu kreye krahezy` means “Krin is more blue than water”, a proverb which means “the younger generation have more energy and opportunities”
- `krarava`
  - `-rava` is the superlative suffix, and `krarava` means “most blue”
  - e.g. `prazu luravu kasepq` means “I walk the fastest”.
- `kravan`
  - `-van` makes the adjective an abstract noun, yet `kra` it self is the noun “blue” so `kravan` is basically never used.
- `kravel`
  - `-vel` makes the adjective an instance noun, and `kravel` means “something blue”
  - e.g. `prazu kravelbu tesinq` means “I like blue things” or “I like cute things”

## Numerals

Numerals in Jaketo are called `unekin`, this word is formed from the words for 1, 2 and 3. However, `unekin` has more words than numbers, concepts like “many” `mo`, “part” `ecu`, “same” `wa`, “common” `yfa` are also `unekin`s. Let’s take the word `u` (meaning “one”) for example. Here are the forms of the word.

An `unekin` can directly modify a noun, for example, `u fesa` means “one person”.

- `uke`
  - `-k` transforms an `unekin` into a noun
  - e.g. `pranzu woke` means “this is all”, where `pran` means “this” and `wo` means “all”.
- `uceva`
  - `-ceva` transforms an `unekin` into an adjective
  - e.g. `moceheva` means “more”

More information about Numerals is shown in the section `Numeral Combination Rule`.

## Adverbials

Technically, there is no unique word class “adverb” in Jaketo, the role of adverbs is mostly played by adverbial form of adjectives and partially the stative verbs (such as “always” can be represented using the auxiliary stative verb `vekycq`). Yet, some particals can be attached to adverbial forms to adjust their meaning. The topic partical `zu` is usually omitted when having these suffixes. Let’s take the adverbial form `kravu` of the adjective `krava` as an example:

- `kravul` or `kravu la`
  - `-l` and `la` means “also; even”, similar to “も” in Japanese. The latter meaning is more often used in (semantically) affirmative expressions.
  - e.g. `pra law tesinq. ze la law tesinq` means “I like books, and he also likes books”.
- `kravu si`
  - `si` means “even; as long as”, similar to “さえ” in Japanese. The first meaning is more often used in (semantically) negative expressions.
  - When used in conditional clauses, `si` takes the latter meaning “as long as”.
  - e.g. `pra si zenbu majverenq` means “Even I don’t understand that”, where `maiver-` means “to understand”;
    - implies that “I’m understand a lot of things, but even it’s me, that is too hard to understand”
  - `pra zenbu si maiverenq` means “I don’t even understand that”.
    - implies that “That is easy, but I’m too stupid to understand such easy thing”.
- `kravu daj`
  - `da` means “while”, similar to “…うちに” in Japanese. This implies suitable and optimal circumstances for some action.
  - e.g. `emipene daj, epaj` means “Set out before it has vanished” (lit. While it doesn’t vanish, go!)
- `kravu mi`
  - `mi` means “only”, similar to “だけ” in Japanese.
  - e.g. `pra mi pran vebutezq` means “Only I can do this”; `pra pran mi vebutezq` means “I can only do this”, the difference is as it’s shown in the example in the `si` particle.
- `kravu ci`
  - `ci` means “(as ...) as ...”, similar to “のように” in Japanese.
  - e.g. `prazu zesu teze ci vebutezq` means “I can do this as he can”; `prazu zesu raevu ci raezy` means “I’m as tall as he is”.

## Clauses

Jaketo is predicate-based, every other component in a sentence is analysed to be an adverbial (ie. modifier) of the predicate. The predicate of a clause could be a `sokan`, `buraj`, `mosraj` or `-zy` form of `gasaru`, as for `unekin`, just add a `-ke` to it to form a `sokan`.

the predicate form of a word will be marked `<any.PRED>`

### Independent Clause

A complete sencense has one independent clause, the predicate of which is in the predicate form, and any other component takes some adverbial form to modify the predicate (or some adjective form to modify some noun, but usually, noun phrases are analysed as a whole component).

The order of the components are rather free, and could change as the emphasized component varies, yet the most common order is “SOV”.

### Adjective Clause

Different from independent clauses, dependent clauses could only have their predicate at the end to avoid potential ambiguity.

Adjective clauses modify nouns, they come directly before the modified nouns with the predicate part adjacent to it. In case you forgot this, the adjective forms of the parts of speech above are:

- `(sokan)-ma`
- `(buraj)-o`
- `(mosraj)-i`
- `(gasaru stem)-va`
- `(unekin)`

such form of a word will be marked `<any.ADJ>`

### Simple Adverbial Clause

the simple adverbial clause is just a dependent clause whose predicate is in the adverbial form

### Compound Clause

“Compound clause”s are something that forms a compund sentence together with a independent clause.

To form a compound clause, different parts of speech takes different forms:

- `(sokan)-'ja`, notice that this is the same as the identical case.
- `(buraj)-uj`
- `(mosraj)-el`
- `(gasaru stem)-ze`

such form of a word will be marked `<any.CMP>`

### Complex Adverbial Clause

This section is about clauses for complex usages such as conditions. Such clauses are mostly based on the compound clause form.

currently, there are two items in this section:

- `<any.CMP> vi`
  - this means “if”
  - e.g. `tasjacu retaruj vi, nasko eputasonq.` means “If it rains tomorrow, I won't go outside.”
- `<any.CMP> vo`
  - this means “given”, similar to “because”, but `A vo, B` only implies that `(A -> B) & A` logically.
  - e.g. `rusjacu retaruj vo, nasko eputasonq.` means “Since it rains today, I won't go outside.”

## Quotation and Parentheses

Jaketo has parentheses that could be read aloud. For normal parentheses, the left part (beginning) and the right part (ending) read `pa` and `sa`; and for quotation marks, they read `pa` and `syta` (for the sake of simplicity, one can omit the left part of the quotation mark, and only read `ta` for the right part).

Parentheses are used to quote everything in a clause but the center, and Quotation marks are used to quote anything possible for a quote. Quotes are marked `Q`, more in the [section of verb paradigms](#verb-paradigms).

## Reflexive Prefix

A reflexive prefix could be added to a verb or stative verb to indecate the accusative or dative of the verb to be a reflexive pronoun. The rule of the prefix is shown below:

- accusative:
  - if the word begins with a consonant, then an `aw` is added to the beginning;
  - if the word begins with a vowel (i.e. void base and void glide), then an `ab` is added to the beginning;
- dative:
  - if the word begins with a consonant, then an `ax` is added to the beginning;
  - if the word begins with a vowel, then an `ad` is added to the beginning.

## Numeral Combination Rule

As one of the characteristic pieces of grammar, `unekin`s take a special rule to combine together.

For numbers less than a hundred thousand, distinct words are used, these words are formed using a rule similar to that of Chinese, each decimal digit joins with the power of ten and those are connected together. For example: the number `1926` is `ukegumunedari` (1-thousand-9-hundred-2-ten-6), each syllable stands for a part.

Along with “pure” numerals that can stand alone, there are “operating” numerals that need one or more numbers to form complete structures. For example, in order to represent lare numbers like `998244353`, the operator `to` is used, this operator takes two numbers `x` and `y` and returns `x*100000+y`, and `998244353` is `gukegumufedane dodedokekimutadaki to`. Other operating numerals include “plus”, “multiply”.

## Verb Paradigms

(Awaiting completion)

A verb paradigm (`tondosma baros`) describes a set of verbs sharing a same argument format. Kratoma has following verb paradigms.

- `mjuka baros`
  - \*ERG
- `zita baros`
  - \*ERG ACC
- `epa baros`
  - \*ERG ALL/TERM
- `kodesa baros`
  - \*ERG ALL
- `retara baros`
  - ERG
- `toma baros`
  - \*ERG ACC/Q
- `latama baros`
  - \*DAT ERG ACC
  - \*DAT (DIR ...).CMP
- `tesama baros`
  - \*ACC ERG

Yet there are still several isolated cases, which are:

- `usatq`
  - \*ERG DAT ACC
- `ivakq`
  - \*DAT ERG ACC
- `derq`
  - \*ACC ALL ERG
