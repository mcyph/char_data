from char_data.data_sources.internal.importers.Write import WriteBase, add
from char_data.data_paths import data_path

from .NamesList import NamesList


class NamesListImport(WriteBase):
    def __init__(self):
        WriteBase.__init__(self, 'unidata/nameslist.pyini')
        self.open_names_list()

    @add
    def open_names_list(self):
        current_D_block = None
        current_D_sub_block = None

        nl = NamesList(
            data_path('chardata', 'unidata/source/NamesList.txt')
        )

        for kind, D in nl:
            if kind == 'information':
                # Copyright info etc
                # Will implement this at a different level, so will ignore here
                pass

            elif kind == 'block':
                # Information that pertains to the entire block (e.g. Basic Latin etc)
                current_D_block = D
                current_D_sub_block = None

            elif kind == 'subblock':
                # Information about part of a block
                current_D_sub_block = D

            elif kind == 'character':
                # Info about specific characters
                ord_ = int(D['codepoint'])

                if current_D_block:
                    for key, value in list(current_D_block.items()):
                        if key in ('block name', 'block description'):
                            yield key, ord_, value
                        elif key == 'has separator':
                            yield key, ord_, str(value) # HACK: PLEASE MAKE WORK WITH ENUMS!!!! ====================================

                if current_D_sub_block:
                    for key, value in list(current_D_sub_block.items()):
                        if key in ('subblock heading', 'subblock technical notice'):
                            yield key, ord_, value
                        elif key == 'subblock see also':
                            yield key, ord_, [sa_codepoint for sa_codepoint, _ in value]
                        else:
                            raise KeyError("Unknown subblock key: %s" % key)

                for key in D:
                    if key in ('codepoint', 'name', 'compatibility mapping', 'decomposed form'):
                        pass
                    elif key == 'see also':
                        yield 'see also', ord_, [sa_codepoint for sa_codepoint, _ in D['see also']]
                    elif key in ('also called', 'formally also called', 'technical notice', 'comments'):
                        yield key, ord_, D[key]
                    else:
                        raise KeyError("Unknown codepoint key: %s" % key)
            else:
                raise Exception("Unknown kind: %s" % kind)


if __name__ == '__main__':
    nli = NamesListImport()
    nli.write(data_path('chardata', 'unidata/nameslist'))
