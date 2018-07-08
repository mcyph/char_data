class NamesList:
    def __init__(self):
        self.also_called = NoFormatStrings(
            self, HEADER_FIXME, 'also called', 'Also Called',
            LISOs=None, index=None
        )
        self.block_description = StringEnum(
            self, HEADER_FIXME, 'block description', 'Block Description',
            LISOs=None, index=None
        )
        self.block_name = StringEnum(
            self, HEADER_FIXME, 'block name', 'Block Name',
            LISOs=None, index=None
        )
        self.comments = NoFormatStrings(
            self, HEADER_FIXME, 'comments', 'Comments',
            LISOs=None, index=None
        )
        self.formally_also_called = NoFormatStrings(
            self, HEADER_FIXME, 'formally also called', 'Formally Also Called',
            LISOs=None, index=None
        )
        self.has_separator = StringEnum(
            self, HEADER_FIXME, 'has separator', 'Has Separator',
            LISOs=None, index=None
        )
        self.see_also = MappingLink(
            self, HEADER_FIXME, 'see also', 'See Also',
            LISOs=None, index=IntegerKeys
        )
        self.subblock_heading = StringEnum(
            self, HEADER_FIXME, 'subblock heading', 'Subblock Heading',
            LISOs=None, index=None
        )
        self.subblock_see_also = MappingLink(
            self, HEADER_FIXME, 'subblock see also', 'Subblock See Also',
            LISOs=None, index=IntegerKeys
        )
        self.subblock_technical_notice = StringEnum(
            self, HEADER_FIXME, 'subblock technical notice', 'Subblock Technical Notice',
            LISOs=None, index=None
        )
        self.technical_notice = NoFormatStrings(
            self, HEADER_FIXME, 'technical notice', 'Technical Notice',
            LISOs=None, index=None
        )
