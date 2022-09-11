import dict


def replacing(new_script):
    for key in dict.dictionary:
        new_script = new_script.replace(key, dict.dictionary[key])
    return new_script
