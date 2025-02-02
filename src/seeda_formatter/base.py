import argparse
import abc
from dataclasses import dataclass
import glob
import re
import json


class SEEDAFormatterBase(abc.ABC):
    @dataclass
    class Config:
        base_path: str = "SEEDA/data/EditEval_Step1"
        annotator: int = 1

    # Compatible with errant Edit class
    @dataclass
    class Edit:
        o_start: int = 0
        o_end: int = 0
        o_str: str = ""
        c_str: str = ""
        is_correct: str = None

    def __init__(self, config: Config):
        self.config = config
        self.base_path = self.config.base_path
        self.data = self.load()

    def load(self):
        base_path = self.config.base_path
        annotator_id = self.config.annotator
        paths = glob.glob(f"{base_path}/annotator{annotator_id}/*.txt")
        paths = sorted(paths)
        data = []
        for path in paths:
            content = open(path).read().rstrip().split("\n")
            d = self.load_an_example(content, path)
            if d != -1:
                data.append(d)
        return data

    def load_an_example(self, content, path):
        _id = path.split("/")[-1].replace(".txt", "")
        pattern = re.compile(r"\[(.*?)\]")
        data = {"id": int(_id)}
        data["previous"] = content[1]
        data["following"] = content[3]
        # [3:-4] is to remove <t> and </t>
        # Keep in mind: the symbol of [] still remains
        errors = []
        source = content[2][3:-4]
        for match in pattern.finditer(source):
            d = dict()
            phrase = match.group(1)
            before_phrase_text = source[: match.start()]
            start_index = len(before_phrase_text.split())
            phrase_word_count = len(phrase.split())
            end_index = start_index + phrase_word_count
            d["o_start"] = start_index
            d["o_end"] = end_index
            errors.append(self.Edit(**d))
        data["errors"] = errors
        data["source"] = source.replace("[", "").replace("]", "")
        corrections = content[6:]
        data["edits"] = []
        for c in corrections:
            # [4:-5] is to remove <s*> and </s*>
            c = c[4:-5]
            edits = []
            offset = 0
            ignore = False
            for match in pattern.finditer(c):
                d = dict()
                content = match.group(1)
                try:
                    edit, is_correct = content.split("|")
                except ValueError:
                    # If it includes an invalid format, ignore this sentence
                    print(_id, content)
                    print("Error in content.split('|')", f"{_id=}", f"{content=}")
                    ignore = True
                    continue
                is_correct = True if is_correct == "True" else False
                try:
                    o_str, c_str = edit.split("→")
                except ValueError:
                    # If it includes an invalid format, ignore this sentence
                    print("Error in edit.split(→)", f"{_id=}", f"{edit=}")
                    ignore = True
                    continue
                d["is_correct"] = is_correct
                d["o_str"] = o_str
                d["c_str"] = c_str
                before_phrase_text = c[: match.start()]
                start_index = len(before_phrase_text.split()) + offset
                phrase_word_count = len(o_str.split())
                end_index = start_index + phrase_word_count
                d["o_start"] = start_index
                d["o_end"] = end_index
                edits.append(self.Edit(**d))

                if o_str == "":
                    # insert edit
                    offset -= len(c_str.split(" "))
                else:
                    offset -= len(c_str.split()) - 1
            if not ignore:
                data["edits"].append(edits)
        return data

    # def save(self, path, **args):
    #     with open(path, 'w') as f:
    #         json.dump(self.data, f, indent=2, **args)
