def get_L_rad_lines():
    # HACK: Get both the radkfile and radkfile2 data and return them together
    with codecs.open('Chars/Data/radkfile', 'rb', 'euc-jp') as f1:
        with codecs.open('Chars/Data/radkfile2', 'rb', 'euc-jp') as f2:
            L = f1.read().split('\n')+f2.read().split('\n')
    return L
