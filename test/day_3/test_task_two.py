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

# test contains dont

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
    input_list = ["mul(1,2)////123!@£$£mul(3,4)", "mul(1,2)////1mul(100,100)23!@£$£mul(3,4)" "mul(1,2)////123!@£$£mul(3,4)"]
    actual = get_pair_products_and_total(input_list)
    expected = 10042
    assert actual == expected