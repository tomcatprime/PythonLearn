import re
log = "Jule 2024 This is error code [12345]"
regex = r"\[(\d+)\]"
result = re.search(regex, log)

print(result[1])

