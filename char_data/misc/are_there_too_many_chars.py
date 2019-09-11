def are_there_too_many_chars(L):
    Total = 0

    for i in L:
        if type(i) == tuple:
            From, To = i
            Total += To - From
        else:
            Total += 1

        if Total > 15000:
            return True

    return False
