import re

text = 'the rain in spain has started 9pm, feel in like sin '

pattern = r'\s\w*in\s'

result = re.findall(pattern, text)

print(result)

