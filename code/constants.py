import re

base = {
    "'": '\ue700',
    "s": '\ue701',
    "z": '\ue702',
    "p": '\ue703',
    "b": '\ue704',
    "m": '\ue705',
    "t": '\ue706',
    "d": '\ue707',
    "n": '\ue708',
    "k": '\ue709',
    "g": '\ue70a',
}
glide = {
    "l": '\ue70c',
    "r": '\ue70d',
    "j": '\ue70e',
    "w": '\ue70f',
}
alias_raw = {
    "f": "pl",
    "v": "bl",
    "c": "sl",
    "h": "kl",
}
alias = str.maketrans(alias_raw)
vowel = {
    "a": '',
    "y": '\ue710',
    "i": '\ue711',
    "e": '\ue712',
    "u": '\ue713',
    "o": '\ue714',
    "q": '\ue715',
}
terminal = {
    "n": '\ue716',
    "m": '\ue717',
    "j": '\ue718',
    "w": '\ue719',
    "s": '\ue71a',
    "z": '\ue71b',
    "x": '\ue71c',
    "l": '\ue71d',
}


syll_re = re.compile(
    r"""((?:['szpbmtdnkg]?[lrjw]?|[cfvh])[aieouyq](?:[szmn](?![lrjw]?[aeiouyq])|[ljw](?![aeiouyq])|x)?)"""
)


b_chars = list(base.values())
g_chars = list(glide.values())
g_chars.append("")
v_chars = list(vowel.values())
v_chars.remove(vowel["q"])
t_chars = list(terminal.values())
t_chars.append("")


b_ord = {
    "'": 0, "s": 1, "z": 2,
    "p": 3, "b": 4, "m": 5,
    "t": 6, "d": 7, "n": 8,
    "k": 9, "g": 10,
}
g_ord = {
    "" : 0,
    "l": 1, "r": 2,
    "j": 3, "w": 4,
}
v_ord = {
    "a": 0, "y": 1,
    "i": 2, "e": 3,
    "u": 4, "o": 5,
    "q": 6,
}
t_ord = {
    "" : 0,
    "n": 1, "m": 2,
    "j": 3, "w": 4,
    "s": 5, "z": 6,
    "x": 7, "l": 8,
}