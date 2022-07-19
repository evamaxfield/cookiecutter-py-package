from determine_cuteness import determine_cuteness

def test_maja():
    assert determine_cuteness("Maja") == "Extremely"
def test_obi():
    assert determine_cuteness("Obi") == "Extremely"

def test_turtle():
    assert determine_cuteness("turtle") == "Very"

def test_bear():
    assert determine_cuteness("bear") == "Danger-cute"

def test_other():
    assert determine_cuteness("axolotl") == "Probably"