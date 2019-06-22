from char_data.data_processors.external.ExternalSourceBase import ExternalBase
from char_data.data_processors.external.hanzi_variants import JaSimplified
from char_data.data_processors.external.hanzi_variants import CEDictVariantsFormatter


class HanziVariants(ExternalBase):
    def __init__(self):
        ExternalBase.__init__(self, 'hanzi_variants')

        self.japanese_simplified = JaSimplified(self, 'japanese_simplified')
        self.chinese_traditional = JaSimplified(self, 'chinese_traditional')   ## ??? What should I call these variants???

        self.erhua_variant = CEDictVariantsFormatter(self, 'Erhua variant')
        self.non_erhua_variant = CEDictVariantsFormatter(self, 'non-Erhua variant')

        self.japanese_variant = CEDictVariantsFormatter(self, 'Japanese variant')
        self.non_japanese_variant = CEDictVariantsFormatter(self, 'non-Japanese variant')

        self.prc_variant = CEDictVariantsFormatter(self, 'PRC variant')
        self.non_prc_variant = CEDictVariantsFormatter(self, 'non-PRC Variant')

        self.more_common_variant = CEDictVariantsFormatter(self, 'more common variant')
        self.less_common_variant = CEDictVariantsFormatter(self, 'less common variant')

        self.archaic_form = CEDictVariantsFormatter(self, 'archaic form')
        self.modern_form = CEDictVariantsFormatter(self, 'modern form')

        self.archaic_variant = CEDictVariantsFormatter(self, 'archaic variant')
        self.modern_variant = CEDictVariantsFormatter(self, 'modern variant')

        self.correct_form = CEDictVariantsFormatter(self, 'correct form')
        self.erroneous_form = CEDictVariantsFormatter(self, 'erroneous form')

        self.antonym = CEDictVariantsFormatter(self, 'antonym')

        self.abbreviated_form = CEDictVariantsFormatter(self, 'abbreviated form')
        self.unabbreviated_form = CEDictVariantsFormatter(self, 'unabbreviated form')

        self.variant_of = CEDictVariantsFormatter(self, 'variant of')
        self.other_variant = CEDictVariantsFormatter(self, 'other variant')
        self.obscure_variant = CEDictVariantsFormatter(self, 'obscure variant')
        self.popular_variant = CEDictVariantsFormatter(self, 'popular variant')

        self.same_as = CEDictVariantsFormatter(self, 'same as')
        self.see_also = CEDictVariantsFormatter(self, 'see also')

        self.chinese_classifier = CEDictVariantsFormatter(
            self, 'Chinese classifier'
        )
        self.words_which_can_use_classifier = CEDictVariantsFormatter(
            self, 'words which can use classifier'
        )




