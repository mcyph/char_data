from char_data.data_paths import data_path


__unicode_set_utils = None


def UnicodeSetUtils(char_data):
    global __unicode_set_utils
    if __unicode_set_utils is None:
        __unicode_set_utils = __UnicodeSetUtils(char_data=char_data)
    return __unicode_set_utils


def _cache(fn):
    cached = [None]

    def new_fn(*args, **kw):
        if cached[0] is None:
            cached[0] = fn(*args, **kw)
        return cached[0]

    return new_fn


class __UnicodeSetUtils:
    def __init__(self, char_data):
        self.char_data = char_data

    #=========================================================#
    #                       Properties                        #
    #=========================================================#

    @_cache
    def get_D_props(self):
        D = {}
        for key in list(self.char_data.index_keys()):
            D[key.partition('.')[-1]] = key
        return D

    @_cache
    def get_D_prop_aliases(self):
        """
        Get a map of Unicode property aliases,
        e.g. {'ccc': 'Canonical_Combining_Class', ...}
        """
        D = {}
        with open(
            data_path(
                'chardata',
                'unidata/source/PropertyAliases.txt'),
            'r',
            encoding='utf-8'
        ) as f:

            for line in f:
                line = line.split('#')[0].strip()
                L = [i.strip() for i in line.split(';') if i.strip()]
                if not L:
                    continue

                prop = L[1]
                LAliases = [L[0]]+L[2:]

                for alias in LAliases:
                    assert not alias in D
                    D[alias.lower()] = prop

        # HACKS!
        D['canonical_combining_class'] = D['ccc'] = 'canonical_combining_classes'
        return D

    #=========================================================#
    #                         Values                          #
    #=========================================================#

    @_cache
    def get_D_values(self):
        D = {}
        for key in list(self.char_data.index_keys()):
            D[key] = D[key.partition('.')[-1]] = self._get_D_values(key)
        return D

    def _get_D_values(self, key):
        """
        Get a map from the stringified, lowercased property value
        to the property

        TODO: support property value aliases!
        """
        L = self.char_data.index_values(key)
        #print key, type(L)
        if not L:
            return {} # WARNING! =============================================

        D = {}
        for i in self.char_data.index_values(key):
            k = str(i).lower()
            assert not k in D
            D[k] = i
        return D

    def get_D_value_aliases(self):
        pass

    @_cache
    def get_D_general_cat_aliases(self):
        D = {}
        with open(data_path('chardata', 'GeneralCatAliases.txt'), 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split('#')[0].strip()
                if not line:
                    continue

                prop, alias = line.split('\t')
                alias = alias.lower()
                if alias in D:
                    assert D[alias] == prop

                D[alias.lower()] = prop
        return D

    #=========================================================#
    #                         Other                           #
    #=========================================================#

    @_cache
    def get_D_default_props(self):
        """
        Get the default [:xxx:] and \p{xxx} mappings

        TODO: Add posix values, e.g. [:alnum:] etc!
        """

        L = [
            'general category',
            'script',
            'property list'
        ]

        D = {}
        D['l&'] = [('general category', i) for i in (
            'Ll',
            'Lu',
            'Lt'
        )]

        for key in self.char_data.index_values('general category'):
            # make it so that e.g. "L"/"l" finds all letters
            D.setdefault(key[0].lower(), []).append(('general category', key))

        for idx_key in L:
            i_D = self._get_D_values(idx_key)
            for key, value in list(i_D.items()):
                D.setdefault(key, []).append((idx_key, value))

        for key, value in list(self.get_D_general_cat_aliases().items()):
            #print value
            if value == 'Cn':
                continue # UNASSIGNED HACK! ========================================

            for i_key, i_value in D[value.lower()]:
                assert i_key == 'general category'
                D.setdefault(key, []).append(('general category', i_value))

        #print 'DDefaultProps:', D
        #from pprint import pprint
        #pprint(D)
        return D
