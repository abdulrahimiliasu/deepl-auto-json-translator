# DeepL Auto Translator

Uses 18n json files as input or a json string as input.

```python

# Using Json File
words, keys = get_words_from_json_file('file path')

# Using Json String
words, keys = get_words_from_json_string('{}')
```

And Of course
```python
#Your DeepL API Key Here
translator = deepl.Translator("API KEY")

# Change target language here
result = translator.translate_text(words, target_lang="HU")
```

Illo Abdulrahim Iliyasu.