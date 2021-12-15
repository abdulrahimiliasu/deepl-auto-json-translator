#!usr/bin/env python3
# encoding: utf-8

import deepl
import json


def get_words_from_json_file(filepath: str):
    words = []
    keys = []

    with open(filepath, 'r') as file:
        data = json.load(file)
        pairs = data.items()
        for key, value in pairs:
            words.append(value)
            keys.append(key)

    return words, keys


def get_words_from_json_string(json_string: str):
    words = []
    keys = []

    if json_string:
        data = json.loads(json_string)
        pairs = data.items()
        for key, value in pairs:
            words.append(value)
            keys.append(key)

    return words, keys


def export_translated_word_with(result, keys: []):
    i = 0
    json_dict = {}
    for translated_word in result:
        json_dict[keys[i]] = translated_word.text
        print(f"'{keys[i]}':'{translated_word.text}'")
        i += 1
    export = json.dumps(json_dict, ensure_ascii=False)

    with open('export.json', 'w') as file:
        file.write(export)
    print(export)


def main():
    translator = deepl.Translator("API KEY")

    # words, keys = get_words_from_json_file('')
    words, keys = get_words_from_json_string('{}')

    result = translator.translate_text(words, target_lang="HU")

    export_translated_word_with(result, keys)

    # Check account usage
    usage = translator.get_usage()
    if usage.character.limit_exceeded:
        print("Character limit exceeded.")
    else:
        print(f"Character usage: {usage.character}")


####################################################################################################
if __name__ == '__main__':
    main()
