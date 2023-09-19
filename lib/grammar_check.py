def grammar_check(str):
    if str == "":
        raise Exception("Please provide sentence")
    ending_chars = [".", "!", "?"]
    if str[0].isupper() and str[-1] in ending_chars:
        return "It's grammatically correct"
    elif str[0].islower() and str[-1] in ending_chars:
        return "Check your Capital Letters"
    elif str[0].isupper() and str[-1] not in ending_chars:
        return "Check your ending punctuation"
    else:
        return "Please revise basic grammar"