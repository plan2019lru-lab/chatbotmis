# -*- coding: utf-8 -*-
"""
Removes default credential hint from index.html and mis-budget-chatbot-app.html.
"""

def remove_hint_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Target block to remove
    target_block = """      <div class="login-default-hint">
        <span>💡 <strong>ค่าเริ่มต้นระบบ:</strong> ชื่อผู้ใช้ <code>admin</code> | รหัสผ่าน <code>admin1234</code></span>
      </div>\n\n"""

    if target_block in content:
        content = content.replace(target_block, "", 1)
        print(f"Removed login-default-hint from {filepath}")
    else:
        # Check CRLF
        target_crlf = target_block.replace('\n', '\r\n')
        if target_crlf in content:
            content = content.replace(target_crlf, "", 1)
            print(f"Removed login-default-hint (CRLF) from {filepath}")
        else:
            # Try without double newline
            target_single = """      <div class="login-default-hint">
        <span>💡 <strong>ค่าเริ่มต้นระบบ:</strong> ชื่อผู้ใช้ <code>admin</code> | รหัสผ่าน <code>admin1234</code></span>
      </div>\n"""
            if target_single in content:
                content = content.replace(target_single, "", 1)
                print(f"Removed login-default-hint (single newline) from {filepath}")
            else:
                target_single_crlf = target_single.replace('\n', '\r\n')
                if target_single_crlf in content:
                    content = content.replace(target_single_crlf, "", 1)
                    print(f"Removed login-default-hint (single CRLF) from {filepath}")
                else:
                    raise ValueError(f"Could not find login-default-hint in {filepath}")

    # 2. Clean up placeholder in sec-input-cur-pass
    old_placeholder = 'placeholder="ระบุรหัสผ่านปัจจุบัน (ค่าเริ่มต้น admin1234)"'
    new_placeholder = 'placeholder="ระบุรหัสผ่านปัจจุบัน"'
    if old_placeholder in content:
        content = content.replace(old_placeholder, new_placeholder, 1)
        print(f"Cleaned placeholder in {filepath}")

    # 3. Clean up confirmation in resetAdminPasswordDefault
    old_confirm = 'confirm("คุณแน่ใจหรือไม่ว่าต้องการรีเซ็ตรหัสผ่านกลับเป็นค่าเริ่มต้น (admin1234)?")'
    new_confirm = 'confirm("คุณแน่ใจหรือไม่ว่าต้องการรีเซ็ตรหัสผ่านกลับเป็นค่าเริ่มต้นของระบบ?")'
    if old_confirm in content:
        content = content.replace(old_confirm, new_confirm, 1)
        print(f"Cleaned reset confirm in {filepath}")

    old_reset_msg = 'alertBox.textContent = "✓ รีเซ็ตรหัสผ่านกลับเป็น admin1234 เรียบร้อยแล้ว";'
    new_reset_msg = 'alertBox.textContent = "✓ รีเซ็ตรหัสผ่านกลับเป็นค่าเริ่มต้นเรียบร้อยแล้ว";'
    if old_reset_msg in content:
        content = content.replace(old_reset_msg, new_reset_msg, 1)
        print(f"Cleaned reset message in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    remove_hint_from_file('index.html')
    remove_hint_from_file('mis-budget-chatbot-app.html')

    with open('index.html', 'rb') as f1, open('mis-budget-chatbot-app.html', 'rb') as f2:
        assert f1.read() == f2.read(), "Files must be identical!"
    print("SUCCESS: Both files updated and 100% identical!")
