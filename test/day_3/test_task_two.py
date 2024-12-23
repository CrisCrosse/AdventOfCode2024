from day_3.task_two import get_valid_muls, contains_dont, get_pair_products_and_total


def test_split_by_modifiers_do_last():
    input_string = "Ido()trydon't()todo()bedon't()notdo()horrible"
    actual = get_valid_muls(input_string)
    expected = ['I', 'try', 'be', 'horrible']
    assert actual == expected


def test_split_by_modifiers_dont_last():
    input_string = "Ido()trydo()horribledon't()generally"
    actual = get_valid_muls(input_string)
    expected = ['I', 'try', 'horrible']
    assert actual == expected


def test_split_by_modifiers_dont_first():
    input_string = "theydon't()Ido()trydon't()generally"
    actual = get_valid_muls(input_string)
    expected = ['they', 'try']
    assert actual == expected


def test_split_by_modifiers_only_do():
    input_string = "theydo()trydo()bedo()horrible"
    actual = get_valid_muls(input_string)
    expected = ['they', 'try', 'be', 'horrible']
    assert actual == expected


def test_split_by_modifiers_only_dont():
    input_string = "theydon't()trydon't()bedon't()horrible"
    actual = get_valid_muls(input_string)
    expected = ['they']
    assert actual == expected


def test_split_by_modifiers_no_end_string():
    input_string = "theydo()trydon't()"
    actual = get_valid_muls(input_string)
    expected = ['they', 'try']
    assert actual == expected


def test_split_by_modifiers_real_string_start():
    input_string = "mul(333,889)+/$}mul(307,370)[?mul(293,832)who()~why()]how()^>select()]don't()<,'mul(942,587)why()}what()&]-? (!mul(74,836)(,when()what() {*(mul(860,687)mul(50,589)mul(70,389)<{how()/where()]'mul(703,164)/>mul(421,905){/)^]mul(951,314)when()why()mul(958,595)when()]+#)@!!;[do()mul(704,757)"
    actual = get_valid_muls(input_string)
    expected = ["mul(333,889)+/$}mul(307,370)[?mul(293,832)who()~why()]how()^>select()]", "mul(704,757)"]
    assert actual == expected


def test_split_by_modifiers_real_string_end():
    input_string = "mul(682,330)what()do()>~'#}/mul(665,248)mul(483,311)~+:,(how()mul(824,825)(}<why()(,*who()(why()don't()who();^<&;++mul(34,885),mul(295,956)mul(277,622) select()$%{mul(20,610)'#when()]~ >mul(342,735)from()+/&what()mul(903,919) ()%from()'(why()mul(556,22)@#what()!mul(544,701)when()*>+'$$&'[mul(811,773)-,~~mul(701,85)::-/-do():when(318,3)how()&%who()mul(759,372)>+why(),/)~mul(796,407){mul(101,955)select(){mul(429,479)who()]->}@mul(174,416);when()!what(): '[{-mul(909,460)@&who()^/;@!mul(517,830)mul(809,577)},#why()how()+ how()&mul(813,555)/( from()'*"
    actual = get_valid_muls(input_string)
    expected = [
        "mul(682,330)what()",
        ">~'#}/mul(665,248)mul(483,311)~+:,(how()mul(824,825)(}<why()(,*who()(why()",
        ":when(318,3)how()&%who()mul(759,372)>+why(),/)~mul(796,407){mul(101,955)select(){mul(429,479)who()]->}@mul(174,416);when()!what(): '[{-mul(909,460)@&who()^/;@!mul(517,830)mul(809,577)},#why()how()+ how()&mul(813,555)/( from()'*"
    ]
    assert actual == expected


def test_contains_dont_matches():
    input_string = "trydon't()"
    actual = contains_dont(input_string)
    expected = True
    assert actual == expected


def test_contains_dont_matches_many_dont():
    input_string = "theydon't()trydon't()bedon't()horrible"
    actual = contains_dont(input_string)
    expected = True
    assert actual == expected


def test_contains_dont_returns_false():
    input_string = "try"
    actual = contains_dont(input_string)
    expected = False
    assert actual == expected


# test multiply products and total

def test_get_pair_products_and_total():
    input_list = ["mul(1,2)////123!@£$£mul(3,4)"]
    actual = get_pair_products_and_total(input_list)
    expected = 14
    assert actual == expected


def test_get_pair_products_and_total_multiple():
    input_list = ["mul(1,2)////123!@£$£mul(3,4)",
                  "mul(1,2)////1mul(100,100)23!@£$£mul(3,4)" "mul(1,2)////123!@£$£mul(3,4)"]
    actual = get_pair_products_and_total(input_list)
    expected = 10042
    assert actual == expected
