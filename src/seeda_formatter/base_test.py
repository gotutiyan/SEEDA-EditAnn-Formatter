from .base import SEEDAFormatterBase

def test_loading():
    seeda = SEEDAFormatterBase(
        SEEDAFormatterBase.Config(base_path="SEEDA/data/EditEval_Step1", annotator=1)
    )
    edit_cls = SEEDAFormatterBase.Edit
    data = seeda.data[0]
    assert (
        data["previous"]
        == "Genetic risk does carry its consequences and should not be taken lightly within the family circle ."
    )
    assert (
        data["following"]
        == "In cases where an individual has gotten to know of a genetic disorder , disclosing or otherwise , to his or her relative is solely a matter of preference within the indivdial moral system ."
    )
    assert (
        data["source"]
        == "Afterall , what affects one family may or may not affect another although the families has a common genetic make up , shared by either of the parents ."
    )
    assert data["errors"] == [edit_cls(o_start=15, o_end=16)]
    assert data["edits"][0] == [
        edit_cls(o_start=0, o_end=1, o_str="Afterall", c_str="After all", is_correct=True),
        edit_cls(o_start=12, o_end=12, o_str="", c_str=",", is_correct=True),
        edit_cls(o_start=14, o_end=15, o_str="families", c_str="family", is_correct=True),
        edit_cls(o_start=20, o_end=20, o_str="", c_str="-", is_correct=False),
    ]
    assert data["edits"][2] == [
        edit_cls(o_start=0, o_end=1, o_str="Afterall", c_str="After all", is_correct=True),
        edit_cls(o_start=12, o_end=12, o_str="", c_str=",", is_correct=True),
        edit_cls(o_start=15, o_end=16, o_str="has", c_str="have", is_correct=True),
        edit_cls(o_start=19, o_end=21, o_str="make up", c_str="make-up", is_correct=False),
    ]
