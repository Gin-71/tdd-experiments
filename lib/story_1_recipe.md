1. Desctibe the Problem
    As a user
    So that I can manage my time
    I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature:
    called = estimation
    fixed data = 200 words -> 1 min
    argument = text
    returns = time in seconds (float)

3. Tests:
    - empty string
    - less than 200 words
    - 200 words precisely
    - more than 200 words
    - Each word is a long word (open door for next improvement)
