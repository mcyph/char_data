from ExternalBase import ExternalBase
from char_data.data_sources.external.property_formatters.hanzi_variants import JaSimplified
from char_data.data_sources.external.property_formatters.hanzi_variants import CEDictVariants


class HanziVariants(ExternalBase):
    def __init__(self):
        ExternalBase.__init__(self, 'hanzi_variants')

        self.japanese_simplified = JaSimplified(self, 'japanese_simplified')
        self.chinese_traditional = JaSimplified(self, 'chinese_traditional')   ## ??? What should I call these variants???

        self.erhua_variant = CEDictVariants(self, 'Erhua variant')
        self.non_erhua_variant = CEDictVariants(self, 'non-Erhua variant')

        self.japanese_variant = CEDictVariants(self, 'Japanese variant')
        self.non_japanese_variant = CEDictVariants(self, 'non-Japanese variant')

        self.prc_variant = CEDictVariants(self, 'PRC variant')
        self.non_prc_variant = CEDictVariants(self, 'non-PRC Variant')

        self.more_common_variant = CEDictVariants(self, 'more common variant')
        self.less_common_variant = CEDictVariants(self, 'less common variant')

        self.archaic_form = CEDictVariants(self, 'archaic form')
        self.modern_form = CEDictVariants(self, 'modern form')

        self.archaic_variant = CEDictVariants(self, 'archaic variant')
        self.modern_variant = CEDictVariants(self, 'modern variant')

        self.correct_form = CEDictVariants(self, 'correct form')
        self.erroneous_form = CEDictVariants(self, 'erroneous form')

        self.antonym = CEDictVariants(self, 'antonym')

        self.abbreviated_form = CEDictVariants(self, 'abbreviated form')
        self.unabbreviated_form = CEDictVariants(self, 'unabbreviated form')

        self.variant_of = CEDictVariants(self, 'variant of')
        self.other_variant = CEDictVariants(self, 'other variant')
        self.obscure_variant = CEDictVariants(self, 'obscure variant')
        self.popular_variant = CEDictVariants(self, 'popular variant')

        self.same_as = CEDictVariants(self, 'same as')
        self.see_also = CEDictVariants(self, 'see also')

        self.chinese_classifier = CEDictVariants(
            self, 'Chinese classifier'
        )
        self.words_which_can_use_classifier = CEDictVariants(
            self, 'words which can use classifier'
        )




