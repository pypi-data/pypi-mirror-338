import re

RE_LTCC = re.sub(r"\s+", '|', ('('+
'''
เy?cีt?ยะ?r?p?f?

เy?cืt?อะ?r?p?f?

เy?cิt?r?cf?

ก็
y?c็t?อr?cf?

[เแ]c?c็t?r?cf?

[เ-ไ]หltf?x
[เ-ไ]mbtf?x
[เ-โ]y?ct?ะ?r?p?f?
[เ-ไ]y?ct?r?p?f?

y?ct?[ะาำ]r?p?f?

yc[ิ-ู]t?r?p?f?
c[ิ-ฺํ๎]t?r?f?

y?cืt?r?cf?

y?cัt?cิf?
y?cัt?r?cf?

y?cัt?วะf?

บ่
y?ctr?cf?

y?ฤๅ
y?ฦๅ

cรรc์
y?cr?cf
y?c?p?
[\s+฿ๆ๏๚๛]
'''.replace('f', '(?:cc?[ุิ]?[์])')
    .replace('x', '($|(?=[\s+เ-ไๆ๏๚๛]|c[ะ-ฺ]))')
    .replace('r', '(?:c์)')
    .replace('y', '(?:cฺ|c๎)')
    .replace('p', '(?:cฺ)')
    .replace('c', '[ก-ฮ]')
    .replace('t', '[่-๋]')
    .replace('m', '[กจฏฎดตบปอ]')
    .replace('l', '[งญณนมย-วฬ]')
    .replace('b', '[ร-ว]')
    .strip()
+')'))

PATTERN = re.compile(RE_LTCC)

def segment(text: str) -> list[str]:
    '''
    Segments text into Large Thai Character Clusters (LTCCs)
    '''
    return [token for token in PATTERN.split(text) if token]