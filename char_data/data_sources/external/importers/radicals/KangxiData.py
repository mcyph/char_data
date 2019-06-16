# -*- coding: utf-8 -*-

# NOTES:
# 1. The 'meat' standing Kangxi is not supported by some fonts
# 2. the 'walk' alternate has a different stroke count for Japanese (辶, 2)

# TODO: Add 197'; 162'; 201' ==================================================================

from re import compile
from collections import namedtuple, defaultdict

from __kangxi_data import _KANGXI_DATA


KANGXI_TRADITIONAL = 0
KANGXI_SIMPLIFIED = 1
KANGXI_BOTH = 2


KangxiItem = namedtuple('KangxiItem', [
    # One of the KANGXI* constants, above
    'kind',
    # The Kangxi numeric ID (the same irrespective of whether Simplified/Traditional)
    'numeric_id',
    # The characters themselves
    'kangxi',
    'num_strokes',
    'definition'
])


PATTERN = compile(
    r'^(?P<num_strokes>[0-9][0-9]?) '
    r'(?P<numeric_id>[0-9][0-9]?[0-9]?)(?P<is_simplified>\'?) '
    r'(?P<kangxi>.*?) '
    r'(?P<definition>.*)$'
)


class KangxiData:
    def __init__(self):
        self.LKangxi = self.get_L_kangxi()

    def get_L_kangxi(self):
        # First, parse the data
        DUnknown = defaultdict(lambda: [])
        DSimplified = defaultdict(lambda: [])

        for line in _KANGXI_DATA.split('\n'):
            if not line.strip():
                continue
            line = line.strip()

            D = PATTERN.match(line).groupdict()
            kangxi_item = KangxiItem(
                kind=KANGXI_BOTH if not D['is_simplified'] else KANGXI_SIMPLIFIED,
                numeric_id=int(D['numeric_id']),
                kangxi=D['kangxi'],
                num_strokes=int(D['num_strokes']),
                definition=D['definition']
            )

            if D['is_simplified']:
                #assert not kangxi_item.numeric_id in DSimplified, kangxi_item.numeric_id
                DSimplified[kangxi_item.numeric_id].append(kangxi_item)
            else:
                #assert not kangxi_item.numeric_id in DUnknown, kangxi_item.numeric_id
                DUnknown[kangxi_item.numeric_id].append(kangxi_item)

        # Then, sort into whether a Kangxi is simplified/traditional only,
        # or the same for both. Entries which have a "'" after the numeric ID
        # will have simplified/traditional variants.

        def as_kind(kangxi_item, kind):
            return KangxiItem(
                kind=kind,
                numeric_id=kangxi_item.numeric_id,
                kangxi=kangxi_item.kangxi,
                num_strokes=kangxi_item.num_strokes,
                definition=kangxi_item.definition
            )

        LOut = []
        for numeric_id, LKangxiItems in DUnknown.items():
            for kangxi_item in LKangxiItems:
                if numeric_id in DSimplified:
                    # Traditional/Simplified variants
                    for simp_kangxi_item in DSimplified[numeric_id]:
                        LOut.append(
                            as_kind(simp_kangxi_item, KANGXI_SIMPLIFIED)
                        )
                    LOut.append(
                        as_kind(kangxi_item, KANGXI_TRADITIONAL)
                    )
                else:
                    # One for both
                    LOut.append(as_kind(kangxi_item, KANGXI_BOTH))
        return LOut

    def get_D_indexed_by_key(self, key, kind=KANGXI_BOTH):
        # Get a dict, indexed by one of the keys of KangxiItem
        # (useful ones being numeric_id, kangxi, num_strokes)
        D = defaultdict(lambda: [])

        for kangxi_item in self.LKangxi:
            if key == 'kangxi':
                # Record for each Kangxi character, if that's the key
                iter_ = getattr(kangxi_item, key)
            else:
                iter_ = [getattr(kangxi_item, key)]

            for i in iter_:
                if kind == KANGXI_BOTH:
                    D[i].append(kangxi_item)
                elif kind == KANGXI_TRADITIONAL and kangxi_item.kind in (
                    KANGXI_BOTH, KANGXI_TRADITIONAL
                ):
                    D[i].append(kangxi_item)
                elif kind == KANGXI_SIMPLIFIED and kangxi_item.kind in (
                    KANGXI_BOTH, KANGXI_SIMPLIFIED
                ):
                    D[i].append(kangxi_item)

        return D


kangxi_data = KangxiData()


if __name__ == '__main__':
    print(kangxi_data.get_D_indexed_by_key('numeric_id'))
    print(kangxi_data.get_D_indexed_by_key('kangxi'))
    print(kangxi_data.get_D_indexed_by_key('num_strokes'))
    print(kangxi_data.get_D_indexed_by_key('num_strokes', kind=KANGXI_TRADITIONAL))
    print(kangxi_data.get_D_indexed_by_key('num_strokes', kind=KANGXI_SIMPLIFIED))

