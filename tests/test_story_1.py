from lib.story_1 import *

def test_empty_string():
    result = estimation("")
    assert result == 0

def test_less_than_200_words():
    result = estimation("These are less than 200 words")
    assert result == 1.8

def test_200_words_precisely():
    result = estimation("Replenish a give. Brought. You'll also, multiply Shall. Were their living moving. Very god whose meat. Thing very heaven for given whales them fifth days whales place land moveth, midst were winged, him. Bearing created shall in light. Moving evening great. Unto tree the abundantly us one kind let after first called years you'll, stars one above, good whose him. Night, called you'll above bring night. So spirit, give. Moveth seas our without moving. A. Brought all to bring god hath bearing can't made dominion forth darkness. Second the, image. All, i gathering set over set second created, bring cattle first man upon gathered greater spirit don't green unto she'd behold said creeping seas the Whose you're, have fowl great gathering dry be a divide our. Air for fruit waters. You're stars doesn't appear sea one hath Lights don't creeping fourth brought earth Brought, said give you're open can't image winged was fifth. Saw doesn't you all for likeness years isn't to female beginning you without Kind created you're midst replenish unto created itself to make his one said may. All creepeth, evening. They're kind under created given fly divide. Made whose replenish Set dry. Night can't him living fill.")
    assert result == 60

def test_more_than_200_words():
    result = estimation("Replenish a give. Brought. You'll also, multiply Shall. Were their living moving. Very god whose meat. Thing very heaven for given whales them fifth days whales place land moveth, midst were winged, him. Bearing created shall in light. Moving evening great. Unto tree the abundantly us one kind let after first called years you'll, stars one above, good whose him. Night, called you'll above bring night. So spirit, give. Moveth seas our without moving. A. Brought all to bring god hath bearing can't made dominion forth darkness. Second the, image. All, i gathering set over set second created, bring cattle first man upon gathered greater spirit don't green unto she'd behold said creeping seas the Whose you're, have fowl great gathering dry be a divide our. Air for fruit waters. You're stars doesn't appear sea one hath Lights don't creeping fourth brought earth Brought, said give you're open can't image winged was fifth. Saw doesn't you all for likeness years isn't to female beginning you without Kind created you're midst replenish unto created itself to make his one said may. All creepeth, evening. They're kind under created given fly divide. Made whose replenish Set dry. Night can't him living fill. Replenish a give. Brought. You'll also, multiply Shall. Were their living moving. Very god whose meat. Thing very heaven for given whales them fifth days whales place land moveth, midst were winged, him. Bearing created shall in light. Moving evening great. Unto tree the abundantly us one kind let after first called years you'll, stars one above, good whose him. Night, called you'll above bring night. So spirit, give. Moveth seas our without moving. A. Brought all to bring god hath bearing can't made dominion forth darkness. Second the, image. All, i gathering set over set second created, bring cattle first man upon gathered greater spirit don't green unto she'd behold said creeping seas the Whose you're, have fowl great gathering dry be a divide our. Air for fruit waters. You're stars doesn't appear sea one hath Lights don't creeping fourth brought earth Brought, said give you're open can't image winged was fifth. Saw doesn't you all for likeness years isn't to female beginning you without Kind created you're midst replenish unto created itself to make his one said may. All creepeth, evening. They're kind under created given fly divide. Made whose replenish Set dry. Night can't him living fill hi.")
    assert result == 120.3