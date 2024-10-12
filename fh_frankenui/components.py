"""Components that are the building blocks to the UI"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../lib_nbs/02_components.ipynb.

# %% auto 0
__all__ = ['NavP', 'SpacedPP', 'SpacedPPs', 'SpacedTxtIcon', 'LAlignedTxtIcon', 'LAlignedIconTxt', 'HelpText']

# %% ../lib_nbs/02_components.ipynb
from fasthtml.common import *
from fasthtml.svg import Svg
from enum import Enum
from fasthtml.components import Uk_select,Uk_input_tag
from functools import partial
from itertools import zip_longest
from .core import *

# %% ../lib_nbs/02_components.ipynb
def NavP(*c, cls=TextFont.muted_sm): return P(cls=cls)(*c)

# %% ../lib_nbs/02_components.ipynb
def SpacedPP(left, right=None): return FullySpacedDiv(NavP(left),NavP(right) if right else '')

# %% ../lib_nbs/02_components.ipynb
def SpacedPPs(*c): return [SpacedPP(*tuplify(o)) for o in c]

# %% ../lib_nbs/02_components.ipynb
def SpacedTxtIcon(txt, icon, ratio, icon_right=True):
    c = (NavP(txt),UkIcon(icon,ratio))
    if not icon_right: c = reversed(c)
    return FullySpacedDiv(*c)  

# %% ../lib_nbs/02_components.ipynb
def LAlignedTxtIcon(txt, icon='play-circle', cls='space-x-2', ratio=1, icon_right=True, txt_cls=None):
    # Good for navbards
    c = (txt if isinstance(txt, FT) else NavP(txt,cls=ifnone(txt_cls,TextFont.muted_sm)),UkIcon(icon,ratio))
    if not icon_right: c = reversed(c)
    return LAlignedDiv(*c, cls=cls)

# %% ../lib_nbs/02_components.ipynb
def LAlignedIconTxt(txt, icon, cls='space-x-2', ratio=1, txt_cls=None):
    # Good for navbars
    return LAlignedTxtIcon(txt, icon, ratio=ratio, txt_cls=txt_cls, icon_right=False)

# %% ../lib_nbs/02_components.ipynb
def HelpText(c):
    # Rename to MinorInfoText, AuxiliaryText, SecondaryDetailText, SmallMutedText?
    return P(c,cls=TextFont.muted_sm)
