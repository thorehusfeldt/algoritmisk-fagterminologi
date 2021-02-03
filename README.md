# Algoritmisk fagterminologi 

## Udvikling

Byg og kør med

```bah
python3 build.py
```

som sønderklipper `_data/words.yml` i enkelte lemmaer (og validerer mod cue-specifikationen)
og lægger de resulterende `.md`-stumper i `_words`. 

Derefter:

```bash
bundle exec jekyll serve -w
```

## Licens

Attribution-NonCommercial-ShareAlike 4.0 International [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
