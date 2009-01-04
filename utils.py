import re

def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)
