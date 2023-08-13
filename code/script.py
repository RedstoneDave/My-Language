import argparse
from itertools import zip_longest
import random

from constants import *


def to_entity(s: str) -> str:
    return "".join(f"&#x{hex(ord(i))[2:]};" for i in s)


def rand_syll() -> str:
    return random.choice(b_chars)\
        + random.choice(g_chars)\
        + random.choice(v_chars)\
        + random.choice(t_chars)


def syll_is_valid(s: str) -> bool:
    '''
    the parameter `s` is assumed to be a Jaketo syllable in Jaketo writing,
    returns `True` if `s` is a valid syllable in Jaketo, `False` otherwise. 
    '''
    if (glide["j"] in s) + (vowel["i"] in s) + (terminal["j"] in s) > 1:
        # a valid syllable does not contain more than one of /j/ or /i/
        return False
    if (glide["w"] in s) + (vowel["u"] in s) + (terminal["w"] in s) > 1:
        # similar to the one above
        return False
    if vowel["e"] in s and terminal["j"] in s:
        # ej is an invalid sequence
        return False
    if len(s) == 1:
        # an input with length 1 can only be valid
        # stopping here to avoid unexpected errors later
        return True
    if s[-2] == vowel["q"]:
        # q (the silence mark) can only be seen at the end
        return False
    if (s[0] in (base["m"], base["n"])) and (s[1] in (glide["l"], glide["r"])):
        # nasal start combined with l/r glide is invalid
        return False
    if s[0] == base["z"] and s[1] == glide["r"]:
        # zr is an invalid sequence
        return False
    return True


def rand_valid_sylls(n: int, get_HTML_entities: bool = True) -> list[str]:
    i = 0
    invalid_count = 0
    ret = []
    while i < n:
        syll = rand_syll()
        if syll_is_valid(syll):
            if get_HTML_entities:
                syll = to_entity(syll)
            ret.append(syll)
            i += 1
        else:
            invalid_count += 1
    print(f"{n} valid syllable(s) generated while encountering {invalid_count} invalid syllable(s)")
    return ret


class JaketoWord:
    '''
    A class containing the spelling, Romanisation of a Jaketo word, supports
    Jaketo lexicographical comparison, `s` is a Romanisation of some Jaketo word

    illegal parts will be omitted with no warning.
    '''

    def __init__(self, s: str):
        self.s = s
        self.sylls = syll_re.findall(s)
        self.ord = []
        script = []
        for i in self.sylls:
            o, scr = self.get_ord_and_script(i)
            self.ord.append(o)
            script.append(scr)
        self.script = "".join(script)

    @classmethod
    def get_ord_and_script(cls, s: str) -> tuple[int, str]:
        '''
        `s` is a Romanisation of a Jaketo syllable, returns a tuple of

        - an order of the corresponding Jaketo script that allows comparison
          with other orders from this function
        - the corresponding Jaketo script (in the Private Use Area)

        raises AssertionError if receiving an illegal syllable
        '''
        s = s.translate(alias)
        if s[0] not in base:
            s = "'" + s
        assert (l := len(s)) > 1, f"string {s} is too short!"
        ret_s = base[s[0]]
        ret_o = b_ord[s[0]] << 4
        i = 1
        if s[i] in glide:
            assert l > 2, f"Illegal Jaketo syllable {s}, no vowel sign"
            ret_s += glide[s[i]]
            ret_o += g_ord[s[i]]
            i = 2
        assert s[i] in vowel, f"Illegal Jaketo syllable {s}, no vowel sign"
        ret_o <<= 4
        ret_s += vowel[s[i]]
        ret_o = (ret_o + v_ord[s[i]]) << 4
        if l == i + 1:
            return ret_o, ret_s
        assert l == i + 2 and s[-1] in terminal, f"Illegal Jaketo syllable {s}, too long"
        ret_s += terminal[s[-1]]
        ret_o += t_ord[s[-1]]
        return ret_o, ret_s

    def compare(self, other: "JaketoWord") -> int:
        '''
        returns -1 if `self` comes before `other` according to the Jaketo
        lexicographic order, 0 if `self` and `other` are lexicographically
        the same, 1 otherwise.
        '''
        for i, j in zip_longest(self.ord, other.ord, fillvalue=-1):
            if i < j:
                return -1
            elif i > j:
                return 1
        return 0

    __cmp__ = compare

    def __eq__(self, other) -> bool:
        return self.compare(other) == 0

    def __ne__(self, other) -> bool:
        return self.compare(other) != 0

    def __lt__(self, other) -> bool:
        return self.compare(other) < 0

    def __gt__(self, other) -> bool:
        return self.compare(other) > 0

    def __le__(self, other) -> bool:
        return self.compare(other) <= 0

    def __ge__(self, other) -> bool:
        return self.compare(other) >= 0

    def __repr__(self) -> str:
        return f"JaketoWord({repr(self.s)})"

    def __getstate__(self) -> dict:
        return self.s

    def __setstate__(self, s: str):
        self.__init__(s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--fromtex", "store_true")
