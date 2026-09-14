with open('mis-budget-chatbot-app.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('adminLoginModal declaration:', 'const adminLoginModal' in text)
print('admin-login-modal element:', 'id="admin-login-modal"' in text)
p_elem = text.find('id="admin-login-modal"')
p_script = text.find('const adminLoginModal')
print('Element pos:', p_elem, 'Script pos:', p_script)
