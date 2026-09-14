import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('mis-budget-chatbot-app.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect scorePage, retrieveContext, generateAnswer, and respond
funcs = ['normalizeThai', 'cleanQueryIntent', 'ngrams', 'scorePage', 'retrieveContext', 'generateAnswer', 'respond']
for fn in funcs:
    m = re.search(r'function ' + fn + r'\([^)]*\)\s*\{[\s\S]*?\n\}', text)
    if m:
        content = m.group(0)
        lines = content.splitlines()
        print(f'=== {fn} ({len(lines)} lines) ===')
        print('\n'.join(lines[:35]))
        if len(lines) > 35:
            print(f'... [{len(lines)-35} lines omitted] ...')
        print()
