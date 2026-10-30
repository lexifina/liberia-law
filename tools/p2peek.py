import hashlib, html, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ts, orig, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
u = f"https://web.archive.org/web/{ts}id_/{orig}"
t = (HERE / '.cache' / hashlib.sha256(u.encode()).hexdigest()).read_bytes().decode('utf-8', 'replace')
t = t[t.find('<!--make_database header end-->'):]
t = re.sub(r'<br\s*/?>|</p>|</h\d>|</li>', '\n', t); t = html.unescape(re.sub(r'<[^>]+>', '', t))
t = re.sub(r'\n\s*\n+', '\n', t)
print(t[:n])
for m in re.finditer(r'(?i)(approved|effective|took effect|take effect|published)[^\n]{0,160}', t):
    print('>>', m.group(0)[:200])
