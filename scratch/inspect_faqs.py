import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('mis-budget-chatbot-app.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const DIRECT_FAQS = (\[.*?\]);\s*\n\s*/\*', text, re.DOTALL)
if m:
    print('DIRECT_FAQS length in chars:', len(m.group(1)))
    # count items
    ids = re.findall(r'id:\s*[\'"]([^\'"]+)[\'"]', m.group(1))
    print('Total DIRECT_FAQS:', len(ids))
    print('IDs:', ids[:20])
else:
    print('DIRECT_FAQS regex not matched, checking line numbers')
    for i, line in enumerate(text.splitlines()):
        if 'const DIRECT_FAQS' in line:
            print(f'Found on line {i+1}')
