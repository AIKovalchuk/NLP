
from yargy                  import rule, and_, not_, or_
from yargy.interpretation   import fact
from yargy.pipelines        import morph_pipeline
from yargy.predicates       import gram, eq, type, in_, length_eq

AddressInformation = fact(
    'AddressInformation',
    ['city', 'street', 'house', 'part', 'building', 'office', 'appartament']
)

ADJF = gram('ADJF')
NOUN = gram('NOUN')
GEOX = gram('Geox')
SURN = gram('Surn')
NAME = gram('Name')
ANIM = gram('anim')
APRO = gram('Apro')
INT = type('INT')
SLASH = eq('/')
DASH = eq('-')
DOT = eq('.')
COMMA = eq(',')

city_type_pipeline = morph_pipeline(['город', 'гор', 'г'])

street_type_pipeline = morph_pipeline([
    'аллея', 'аллее', 'аллеи', 'ал', 'алея', 'алее', 'алеи',
    'бульвар', 'бульвара', 'бульваре', 'бул', 'б'
    'микрорайон', 'микрорайона', 'микрорайоне', 'мкр',
    'набережная', 'набережой', 'наб', 'нб',
    'переулок', 'переулке', 'переулка', 'пер',
    'площадь', 'площади', 'пл',
    'поселок', 'пос', 'п',
    'проезд', 'проезде', 'проезда', 'пр', 'пр-д',
    'проспект', 'просп', 'пр-т', 'пр-кт',
    'тупик', 'тупике', 'тупика', 'туп',
    'улица', 'улице', 'улицы', 'ул',
    'шоссе', 'ш',
])

house_pipeline = morph_pipeline(['д', 'дом'])

part_pipeline = morph_pipeline(['корпус', 'корп', 'к'])

building_pipeline = morph_pipeline(['строение', 'ст'])

APPARTAMENT_pipeline = morph_pipeline(['квартира', 'кв'])

CITY_RULE = rule(
    city_type_pipeline.optional(),
    DOT.optional(),
    and_(
        ADJF,
        not_(APRO) 
    ).optional(),
    GEOX
).interpretation(AddressInformation.city)


STREET_NAME = or_(
    and_(
        ADJF,
        not_(APRO) 
    ),
    GEOX,
    SURN 
)

STREET_NAME_WITH_NOUN = or_(
    and_(
        ADJF,
        not_(APRO) # некоторые прилагательные еще и местоимения (ex. 'мой')
    ),
    NOUN,
    GEOX,
    SURN 
)

STREET_RULE = or_(
    # улица с существительным и фамилией (ex. космонавта Комарова)
    rule(
        street_type_pipeline.optional(),     # 'улица'
        DOT.optional(),                      # '.'
        and_(
            NOUN, ANIM                       # должность/звание (любые существительные не подходят - должно быть одушевленное)
        ),                              
        SURN                                 # фамилия
    ),
    # улица с существительным и именем (ex. мусы Джалиля)
    rule(
        street_type_pipeline.optional(),     # 'улица'
        DOT.optional(),                      # '.'
        and_(
            NOUN, ANIM                       # должность/звание (любые существительные не подходят - должно быть одушевленное)
        ),                               
        NAME                                 # имя
    ),
    # улица с должностью, существительным и фамилией (ex. героя труда Егорова)
    rule(
        street_type_pipeline.optional(),     # 'улица'
        DOT.optional(),                      # '.'
        and_(
            NOUN, ANIM                       # должность/звание (любые существительные не подходят - должно быть одушевленное)
        ), 
        and_(
            NOUN, gram('gent')               # существительное
        ),                             
        SURN                                 # фамилия
    ),
    rule(
        street_type_pipeline.optional(),   # 'ул'
        DOT.optional(),                    # '.'
        in_('БМ').optional(),              # 'Б'
        DOT.optional(),                    # '.'
        ADJF.optional(),                   # 'Большая'
        STREET_NAME,                       # 'Покровская'/'Арбат'/'Ленина'
        NOUN.optional()                    # 'вал'
    ),
    rule(
        in_('БМ').optional(),               # 'Б'
        DOT.optional(),                     # '.'
        ADJF.optional(),                    # 'Большая'
        STREET_NAME,                        # 'Грузинская'
        street_type_pipeline,               # 'ул'/'пер'
        DOT.optional(),                     # '.'
    ),
    # улица только с существительным (чаще всего родительный падеж и множественное число)
    # ex. 'улица Романтиков', 'проспект Героев'
    rule(
        street_type_pipeline.optional(),   # 'ул'
        DOT.optional(),                    # '.'
        and_(
            NOUN, gram('gent'), gram('plur')
        )      
    ),
    # улица с числом и существительным
    rule(
        street_type_pipeline.optional(),     # 'улица'
        DOT.optional(),                      # '.'
        INT,                                 # '30'
        NOUN.optional(),                     # 'лет'
        STREET_NAME_WITH_NOUN                # 'Победы'
    ),
    # улица с числом и прилагательным
    rule(
        street_type_pipeline.optional(),     # 'улица'
        DOT.optional(),                      # '.'
        INT,                                 # '30'
        and_(
            ADJF,                            # 'Почтовое'
            not_(APRO)                       # некоторые прилагательные еще и местоимения (ex. 'мой') 
        ),
        STREET_NAME_WITH_NOUN                # 'отделение'
    ),
    # улица с именем и фамилией
    rule(
        street_type_pipeline.optional(),     # 'улица'
        DOT.optional(),                      # '.'
        NAME,                                # имя 
        SURN                                 # фамилия
    ),
    
).interpretation(AddressInformation.street)

HOUSE_RULE = or_(
    rule(
        COMMA.optional(),
        house_pipeline.optional(),
        DOT.optional(),
        INT,
        or_(
             and_(
                 gram('Abbr'),
                 length_eq(1)
             ),
            and_(
                type('RU'),
                length_eq(1),
            )
        ).optional()
    ).interpretation(AddressInformation.house),
    rule(
        house_pipeline,
        rule(
             COMMA.optional(),
             house_pipeline.optional(),
             DOT.optional(),
            INT,
            or_(
                and_(
                    gram('Abbr'),
                    length_eq(1)
                ),
                and_(
                    type('RU'),
                    length_eq(1),
                )
            ).optional()
         ).interpretation(AddressInformation.house)
    )
)

PART_RULE = rule(
    COMMA.optional(),
    part_pipeline.optional(),
    DOT.optional(),
    SLASH.optional(),
    INT
).interpretation(AddressInformation.part)

BUILDING_RULE = rule(
    COMMA.optional(),
    building_pipeline.optional(),
    DOT.optional(),
    INT
).interpretation(AddressInformation.building)

OFFICE_RULE = rule(
    COMMA.optional(),
    eq('офис'),
    DOT.optional(),
    INT
).interpretation(AddressInformation.office)

APPARTAMENT_RULE = rule(
    COMMA.optional(),
    APPARTAMENT_pipeline.optional(),
    DOT.optional(),
    INT
).interpretation(AddressInformation.appartament)

ADDRESS_RULE = or_(
    rule(CITY_RULE),
    rule(CITY_RULE, STREET_RULE, HOUSE_RULE, PART_RULE),
    rule(CITY_RULE, STREET_RULE, HOUSE_RULE, PART_RULE, APPARTAMENT_RULE),
    rule(CITY_RULE, STREET_RULE, HOUSE_RULE, PART_RULE, OFFICE_RULE),
    rule(CITY_RULE, STREET_RULE, HOUSE_RULE, BUILDING_RULE, APPARTAMENT_RULE),
    rule(CITY_RULE, STREET_RULE, HOUSE_RULE, BUILDING_RULE, OFFICE_RULE),
    rule(CITY_RULE, STREET_RULE, HOUSE_RULE, APPARTAMENT_RULE),
    rule(CITY_RULE, STREET_RULE, HOUSE_RULE, OFFICE_RULE),
    rule(CITY_RULE, STREET_RULE, HOUSE_RULE, BUILDING_RULE),
    rule(CITY_RULE, STREET_RULE, HOUSE_RULE),
    rule(CITY_RULE, STREET_RULE),
    rule(STREET_RULE, CITY_RULE, HOUSE_RULE),
    rule(STREET_RULE, CITY_RULE, HOUSE_RULE, PART_RULE, APPARTAMENT_RULE),
    rule(STREET_RULE, CITY_RULE, HOUSE_RULE, PART_RULE, OFFICE_RULE),
    rule(STREET_RULE, CITY_RULE, HOUSE_RULE, BUILDING_RULE, APPARTAMENT_RULE),
    rule(STREET_RULE, CITY_RULE, HOUSE_RULE, BUILDING_RULE, OFFICE_RULE),
    rule(STREET_RULE, CITY_RULE, HOUSE_RULE, APPARTAMENT_RULE),
    rule(STREET_RULE, CITY_RULE, HOUSE_RULE, OFFICE_RULE),
    rule(STREET_RULE, CITY_RULE, HOUSE_RULE, PART_RULE),
    rule(STREET_RULE, CITY_RULE, HOUSE_RULE, BUILDING_RULE),
    rule(STREET_RULE, HOUSE_RULE),
    rule(STREET_RULE, HOUSE_RULE, PART_RULE, APPARTAMENT_RULE, CITY_RULE),
    rule(STREET_RULE, HOUSE_RULE, PART_RULE, OFFICE_RULE, CITY_RULE),
    rule(STREET_RULE, HOUSE_RULE, BUILDING_RULE, APPARTAMENT_RULE, CITY_RULE),
    rule(STREET_RULE, HOUSE_RULE, BUILDING_RULE, OFFICE_RULE, CITY_RULE),
    rule(STREET_RULE, HOUSE_RULE, APPARTAMENT_RULE, CITY_RULE),
    rule(STREET_RULE, HOUSE_RULE, OFFICE_RULE, CITY_RULE),
    rule(STREET_RULE, HOUSE_RULE, PART_RULE, CITY_RULE),
    rule(STREET_RULE, HOUSE_RULE, BUILDING_RULE, CITY_RULE),
    rule(STREET_RULE, HOUSE_RULE, CITY_RULE),
    rule(STREET_RULE, HOUSE_RULE, PART_RULE, APPARTAMENT_RULE),
    rule(STREET_RULE, HOUSE_RULE, PART_RULE, OFFICE_RULE),
    rule(STREET_RULE, HOUSE_RULE, BUILDING_RULE, APPARTAMENT_RULE),
    rule(STREET_RULE, HOUSE_RULE, BUILDING_RULE, OFFICE_RULE),
    rule(STREET_RULE, HOUSE_RULE, APPARTAMENT_RULE),
    rule(STREET_RULE, HOUSE_RULE, OFFICE_RULE),
    rule(STREET_RULE, HOUSE_RULE, PART_RULE),
    rule(STREET_RULE, HOUSE_RULE, BUILDING_RULE),
    rule(HOUSE_RULE, APPARTAMENT_RULE, STREET_RULE),
).interpretation(AddressInformation)
