# Match types
#
# NOTE: OPERATOR works on all the items to the
# left of the operator in the current group,
# and only subtracts/intersects the *one* group
# to the right of the operator.
#
# See: http://userguide.icu-project.org/strings/unicodeset
OPERATOR = 0  # (operator, (from, to))
RANGES = 1  # [(from, to), ...]
STRING = 2  # pattern

# Operator types
INTERSECT = 0  # A & B
DIFFERENCE = 1  # A - B
DOperators = {
    '-': DIFFERENCE,
    '&': INTERSECT
}
