# Replace string

letter = '''Dear <|Name|>,
You are selected!
<|Date - |>'''

print(letter.replace("<|Name|>", "Max").replace("<|Date - |>","24 September 2030"))
