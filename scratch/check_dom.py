with open('scratch/dom_test.html', 'r', encoding='utf-16', errors='ignore') as f:
    t = f.read()
print('Length of dumped DOM (UTF-16 decoded):', len(t))
print('Has btn-admin-panel:', 'btn-admin-panel' in t)
print('Has admin-hidden:', 'admin-hidden' in t)
print('Has Sarabun font:', 'Sarabun' in t)
print('Has bot welcome greeting in DOM:', 'ยินดีต้อนรับ' in t or 'สวัสดี' in t)
