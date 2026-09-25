# Rebuild index.html WORDS array from wordlist_full.json + examples_progress.json
# Crash-safe: examples_progress.json is the source of truth for ex/exZh.
import re, json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)

full = json.load(open(os.path.join(BASE, 'wordlist_full.json'), encoding='utf-8'))['words']
prog = json.load(open(os.path.join(BASE, 'examples_progress.json'), encoding='utf-8'))

words = []
missing = []
for w in full:
    k = w['word'].lower()
    ex = prog.get(k, {})
    entry = {
        'word': w['word'], 'pos': w['pos'], 'zh_tw': w['zh_tw'],
        'level': w.get('level', 1), 'topic': w.get('topic', 'daily'),
        'ex': ex.get('ex', ''), 'exZh': ex.get('exZh', ''),
    }
    words.append(entry)
    if not ex.get('ex'):
        missing.append(w['word'])

done = len(words) - len(missing)
print(f'total={len(words)} with_examples={done} missing={len(missing)}')

if len(sys.argv) > 1 and sys.argv[1] == '--write':
    html_path = os.path.join(ROOT, 'index.html')
    html = open(html_path, encoding='utf-8').read()
    new_arr = 'const WORDS = ' + json.dumps(words, ensure_ascii=False) + ';'
    html2 = re.sub(r'const WORDS = \[.*?\];', lambda m: new_arr, html, count=1, flags=re.S)
    if html2 == html:
        print('WARN: WORDS array not replaced!'); sys.exit(1)
    open(html_path, 'w', encoding='utf-8').write(html2)
    print(f'wrote {html_path} ({len(words)} words, {done} with examples)')
