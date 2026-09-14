import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('mis-budget-chatbot-app.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('=== FETCH & NETWORK CALLS ===')
fetches = re.findall(r'fetch\([^\)]+\)', text)
print(f'fetch calls count: {len(fetches)}')
for f in fetches:
    print(' ', f)

print('Google script references:', re.findall(r'script\.google\.com[^\s\'\"\`]*', text))

print('\n=== DIRECT FAQS ANALYSIS ===')
direct_faqs_match = re.search(r'const DIRECT_FAQS\s*=\s*(\[.*?\]);\s*const OUT_OF_SCOPE_TERMS', text, re.DOTALL)
if direct_faqs_match:
    # let's count FAQs
    faq_blocks = re.findall(r'id:\s*[\'"]([^\'"]+)[\'"]', direct_faqs_match.group(1))
    print(f'Total DIRECT_FAQS: {len(faq_blocks)}')
    print('Sample FAQ IDs:', faq_blocks[:10])

print('\n=== QUESTION CATEGORIES ===')
cat_match = re.search(r'const QUESTION_CATEGORIES\s*=\s*(\{.*?\n\};)', text, re.DOTALL)
if cat_match:
    cats = re.findall(r'category:\s*[\'"]([^\'"]+)[\'"]', cat_match.group(1))
    print(f'Total question categories: {len(cats)}')
    print('Categories:', cats)

print('\n=== RETRIEVAL LOGIC SNIPPET ===')
retr_match = re.search(r'function retrieveContext\(.*?\n\}', text, re.DOTALL)
if retr_match:
    print(retr_match.group(0)[:400])

print('\n=== ANSWER GENERATOR SNIPPET ===')
ans_match = re.search(r'function generateAnswer\(.*?\n\}', text, re.DOTALL)
if ans_match:
    print(ans_match.group(0)[:600])

print('\n=== ADMIN / STORAGE LOGIC ===')
admin_funcs = ['getCustomFaqs', 'saveCustomFaqsToStorage', 'logUserQuestion', 'handleAdminLogin']
for af in admin_funcs:
    m = re.search(r'function ' + af + r'\(.*?\n\}', text, re.DOTALL)
    if m:
        print(f'--- {af} ---')
        print(m.group(0)[:250])
