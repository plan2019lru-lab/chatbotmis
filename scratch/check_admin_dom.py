import re

with open('scratch/dom_admin.html', 'r', encoding='utf-16', errors='ignore') as f:
    t = f.read()

m = re.search(r'<button[^>]*id="btn-admin-panel"[^>]*>', t)
if m:
    print('Button HTML with ?admin=1:', m.group(0))
    print('Is admin-hidden absent?', 'admin-hidden' not in m.group(0))
else:
    print('Button not found')
