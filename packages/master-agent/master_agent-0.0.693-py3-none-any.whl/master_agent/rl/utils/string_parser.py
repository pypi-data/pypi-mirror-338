# function to extract object and predicate
def extract_pred_obj(s) -> tuple[str, str]:
    pred = ""
    obj = ""

    i = 0

    while i < len(s):
        if (s[i] == "("):
            i += 1
            while (i < len(s)):
                if (s[i] == ")"):
                    break
                obj += s[i]
                i += 1
        if (s[i] == ")"):
            break
        pred += s[i]
        i += 1

    return pred.lower(), obj