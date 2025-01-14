# Regex Basics
import re

text = "Contact me at example@email.com or another@email.com"
emails = re.findall(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", text)
print(emails)