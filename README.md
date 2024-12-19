# SEEDA-EditAnn-Formatter
Scripts for easy handling of SEEDA edit-level annotations

# Install
```sh
pip install git+https://github.com/gotutiyan/SEEDA-EditAnn-Formatter
git clone https://github.com/tmu-nlp/SEEDA.git
```

Use out API.
```python
from seeda_formatter import SEEDAFormatterBase
import pprint
seeda = SEEDAFormatterBase(
    SEEDAFormatterBase.Config(
        base_path='SEEDA/data/EditEval_Step1',
        annotator=1
    )
)

# The order is sorted by file path: 0.txt, 1.txt, 10.txt ...
pprint.pprint(seeda.data[0])
# {'edits': [[Edit(o_start=0,
#                  o_end=1,
#                  o_str='Afterall',
#                  c_str='After all',
#                  is_correct=True),
#             Edit(o_start=12,
#                  o_end=12,
#                  o_str='',
#                  c_str=',',
#                  is_correct=True),
#             Edit(o_start=14,
#                  o_end=15,
#                  o_str='families',
#                  c_str='family',
#                  is_correct=True),
#             Edit(o_start=20,
#                  o_end=20,
#                  o_str='',
#                  c_str='-',
#                  is_correct=False)],
#            [Edit(o_start=12,
#                  o_end=12,
#                  o_str='',
#                  c_str=',',
#                  is_correct=True),
#             Edit(o_start=15,
#                  o_end=16,
#                  o_str='has',
#                  c_str='have',
#                  is_correct=True)],
#            [Edit(o_start=0,
#                  o_end=1,
#                  o_str='Afterall',
#                  c_str='After all',
#                  is_correct=True),
#             Edit(o_start=12,
#                  o_end=12,
#                  o_str='',
#                  c_str=',',
#                  is_correct=True),
#             Edit(o_start=15,
#                  o_end=16,
#                  o_str='has',
#                  c_str='have',
#                  is_correct=True),
#             Edit(o_start=19,
#                  o_end=21,
#                  o_str='make up',
#                  c_str='make-up',
#                  is_correct=False)],
#            [Edit(o_start=0,
#                  o_end=1,
#                  o_str='Afterall',
#                  c_str='Afterwards',
#                  is_correct=False),
#             Edit(o_start=12,
#                  o_end=12,
#                  o_str='',
#                  c_str=',',
#                  is_correct=True),
#             Edit(o_start=20,
#                  o_end=20,
#                  o_str='',
#                  c_str='-',
#                  is_correct=False)],
#            [Edit(o_start=13,
#                  o_end=13,
#                  o_str='',
#                  c_str='',
#                  is_correct=False),
#             Edit(o_start=21,
#                  o_end=21,
#                  o_str='',
#                  c_str='-',
#                  is_correct=False)]],
#  'errors': [Edit(o_start=15,
#                  o_end=16,
#                  o_str='',
#                  c_str='',
#                  is_correct=None)],
#  'following': 'In cases where an individual has gotten to know of a genetic '
#               'disorder , disclosing or otherwise , to his or her relative is '
#               'solely a matter of preference within the indivdial moral system '
#               '.',
#  'id': 0,
#  'previous': 'Genetic risk does carry its consequences and should not be taken '
#              'lightly within the family circle .',
#  'source': 'Afterall , what affects one family may or may not affect another '
#            'although the families has a common genetic make up , shared by '
#            'either of the parents .'}
```