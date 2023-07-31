from abc import ABC, abstractmethod
import argparse
import os
import pickle
from dataclasses import asdict, dataclass, field

import BTrees
import BTrees.Interfaces as BTI
import yaml
from script import *


yaml.Dumper.org_represent_str = yaml.Dumper.represent_str


def repr_str_for_yaml(dumper: yaml.Dumper, data: str):
    if '\n' in data:
        return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')
    return dumper.org_represent_str(data)


yaml.add_representer(str, repr_str_for_yaml, Dumper=yaml.Dumper)


@dataclass(order=True)
class Entry:
    pos: str = ""
    usage: str = ""
    trans: dict[str, str] = field(default_factory=dict)
    note: str = ""


class Manager(ABC):
    @property
    @abstractmethod
    def prompt(self) -> str:
        return '> '

    def multiple_lines_input(self) -> str:
        print("Please input multiple lines, input a '%' to end:")
        l = []
        while True:
            s = input()
            if s == "%":
                break
            l.append(s)
        return "\n".join(l)

    def single_line_input(self, prompt: str = "item") -> str:
        print(f"Please input the {prompt}:")
        return input()


class WordManager(Manager):
    def __init__(self, spelling, dm: "DictManager", w: Entry | None = None):
        self.spelling = spelling
        self.dm = dm
        if w is None:
            self.w = Entry()
        else:
            self.w = w

    @property
    def prompt(self) -> str:
        return f"word {self.spelling} > "

    def set_pos(self, s: str):
        self.w.pos = s

    def set_usage(self):
        self.w.usage = self.multiple_lines_input()

    def set_trans(self, form: str = "s"):
        if form == "s" or form == "single":
            s = self.single_line_input("translation")
        elif form == "m" or form == "multiple":
            s = self.multiple_lines_input()
        else:
            raise ValueError(
                f"Unexpected input form {form}, "
                "which could only be one in 's', 'single', 'm', 'multiple'"
            )
        self.w.trans[self.dm.default_lang] = s

    def set_trans_l(self, lang: str, form: str = "s"):
        if form == "s" or form == "single":
            s = self.single_line_input("translation")
        elif form == "m" or form == "multiple":
            s = self.multiple_lines_input()
        else:
            raise ValueError(
                f"Unexpected input form {form}, "
                "which could only be one in 's', 'single', 'm', 'multiple'"
            )
        self.w.trans[lang] = s

    def set_note(self):
        self.w.note = self.multiple_lines_input()

    def del_trans_l(self, lang: str):
        del self.w.trans[lang]

    def dump(self) -> "DictManager":
        self.dm.cur_dict[JaketoWord(self.spelling)] = self.w
        return self.dm

    def back(self) -> "DictManager":
        return self.dm

    def display(self):
        print(yaml.dump(
            asdict(self.w),
            allow_unicode=True,
            default_flow_style=False,
        ))

    # alias

    sp = set_pos
    su = set_usage
    st = set_trans
    sn = set_note
    stl = set_trans_l
    dt = del_trans_l


class DictManager(Manager):
    cur_dict: BTI.IBTree

    def __init__(self):
        self.default_lang = "en"

    @property
    def prompt(self):
        return "DictManager > "

    def new_dict(self):
        self.cur_file = self.single_line_input("name of the file")
        self.cur_dict: BTI.IBTree = BTrees.OOBTree.OOBTree()

    def quit(self):
        exit()

    def load(self):
        self.cur_file = self.single_line_input("name of the file")
        with open(self.cur_file, "rb") as f:
            self.cur_dict: BTI.IBTree = pickle.load(f)

    def load_word(self, spelling: str) -> WordManager:
        w = self.cur_dict[JaketoWord(spelling)]
        self.cur_w = WordManager(spelling, self, w)
        return self.cur_w

    def generate(self):
        to_file = self.single_line_input("yaml you want to generate")
        l = []
        for i in self.cur_dict:
            j = self.cur_dict[i]
            d = asdict(j)
            d["spelling"] = i.s
            if d["usage"] == "":
                del d["usage"]
            if d["note"] == "":
                del d["note"]
            l.append(d)
        with open(to_file, "w", encoding="utf-8") as f:
            yaml.dump(l, f, allow_unicode=True, default_flow_style=False)
        print("Notice that this is a function with high cost")

    def save(self):
        with open(self.cur_file, "wb") as f:
            pickle.dump(self.cur_dict, f)

    def new_word(self, spelling: str):
        if JaketoWord(spelling) in self.cur_dict:
            print("You can't create a new word because it's already been created")
            return
        self.cur_w = WordManager(spelling, self)
        return self.cur_w

    def del_word(self, spelling: str):
        del self.cur_dict[JaketoWord(spelling)]

    def search(self, start: str, _max_number: str | None = None):
        if _max_number is None:
            max_number = 5
        else:
            if not _max_number.isdigit():
                print(f"the second parameter must be a digit, but received {_max_number}")
                return
            max_number = int(_max_number)
        it = self.cur_dict.iteritems(JaketoWord(start))
        for _ in range(max_number):
            try:
                item = next(it)
            except StopIteration:
                break
            print(yaml.dump(
                {item[0].s: asdict(item[1])},
                allow_unicode=True,
                default_flow_style=False,
            ))
    # alias

    open = load
    nd = new_dict
    nw = new_word
    lw = load_word
    dw = del_word


if __name__ == "__main__":
    psr = argparse.ArgumentParser()

    psr.add_argument(
        '-f', '--folder',
        default="D:/study/My Language/vocabulary"
    )

    args = psr.parse_args()

    os.chdir(os.path.expanduser(args.folder))

    cur_mng = DictManager()
    while True:
        cmd = input(cur_mng.prompt)
        s = cmd.split()
        try:
            cur_m = getattr(cur_mng, s[0])
        except AttributeError:
            print(f"Current manager has no command {repr(s[0])}")
            continue
        except IndexError:
            continue
        try:
            ret = cur_m(*s[1:])
        except TypeError as e:
            print(f"the number of parameters wrong: {e}")
            continue
        except KeyError as e:
            print(f"the word not found: {e}")
            continue
        except Exception as e:
            print(f"An unknown exception {type(e)} occured: {e}")
            continue
        if isinstance(ret, Manager):
            cur_mng = ret
