from yargy                  import rule, and_, not_, or_
from yargy.interpretation   import fact
from yargy.relations        import gnc_relation
from yargy.predicates       import gram, caseless, eq, custom

gnc = gnc_relation() 

PersonInformation = fact(
    'PersonInformation',
    ['first', 'last', 'middle']
)

FIRST = gram('Name').interpretation(PersonInformation.first).match(gnc)

LAST = gram('Surn').interpretation(PersonInformation.last).match(gnc)

MIDDLE = gram('Patr').interpretation(PersonInformation.middle).match(gnc)

PREPOSITION = rule(
          caseless('по'),
          not_(eq(gram('NOUN').interpretation(PersonInformation.first.inflected('datv'))))
    )


def is_surname(name):
  if ((name.endswith('ов') == True or name.endswith('ова') == True) or
     (name.endswith('ев') == True or name.endswith('ева') == True) or
     (name.endswith('ин') == True or name.endswith('ина') == True) or
     (name.endswith('ын') == True or name.endswith('ына') == True) or
     (name.endswith('их') == True) or (name.endswith('ых') == True) or
     (name.endswith('ский') == True or name.endswith('ская') == True) or
     (name.endswith('цкий') == True or name.endswith('цкая') == True)):
    return name

SURNAME_LIKE_NAME = gram('Name').interpretation(PersonInformation.last.custom(is_surname))

SURNAME_LIKE_NOUN = gram('NOUN').interpretation(PersonInformation.last.custom(is_surname))

SURNAME_LIKE_NOUN_WITHOUT = rule(
    and_(  
        gram('NOUN'), gram('sing'), gram('nomn')
    ).interpretation(PersonInformation.last)
)
SURNAME_LIKE_ADVB_WITHOUT = rule(
    and_(
        gram('ADVB'), gram('ADJS')
    ).interpretation(PersonInformation.last)
)
PERSON_INFO = or_(
    rule(FIRST, LAST, MIDDLE),
    rule(LAST, FIRST, MIDDLE),
    rule(FIRST, MIDDLE, LAST),
    rule(SURNAME_LIKE_NOUN_WITHOUT, FIRST, MIDDLE),
    rule(SURNAME_LIKE_NAME, FIRST, MIDDLE),
    rule(SURNAME_LIKE_NOUN, FIRST, MIDDLE),  
    rule(SURNAME_LIKE_ADVB_WITHOUT, FIRST, MIDDLE),
    rule(FIRST, LAST),
    rule(LAST, FIRST),
    rule(FIRST, MIDDLE),
    rule(SURNAME_LIKE_NAME, FIRST),
    rule(FIRST, SURNAME_LIKE_NAME),
    PREPOSITION,
    rule(FIRST),
    rule(LAST),
    rule(MIDDLE)
).interpretation(PersonInformation)