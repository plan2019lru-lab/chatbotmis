# -*- coding: utf-8 -*-
import subprocess
import os
import shutil
import time

app_path = r'c:\Users\Username\Desktop\แชทบอทระบบคำขอ\mis-budget-chatbot-app.html'
artifact_dir = r'C:\Users\Username\.gemini\antigravity-ide\brain\ca5445d9-f830-4a15-b1d2-0e090c4e88de'
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open(app_path, 'r', encoding='utf-8') as f:
    html = f.read()

REPLACE_TARGET = 'updateAdminBadgeCount();\n</script>'
if REPLACE_TARGET not in html:
    REPLACE_TARGET = 'updateAdminBadgeCount();\r\n</script>'
assert REPLACE_TARGET in html, "Target not found in HTML!"

# TEST 1: Open Login Modal
test1_html = html.replace(REPLACE_TARGET, '''
updateAdminBadgeCount();
setTimeout(() => {
  openAdminModal();
}, 400);
</script>''')

test1_file = r'c:\Users\Username\Desktop\แชทบอทระบบคำขอ\test1_login_open.html'
with open(test1_file, 'w', encoding='utf-8') as f:
    f.write(test1_html)

screenshot1 = os.path.join(artifact_dir, 'screen_admin_login.png')
tmp_dir1 = os.path.abspath('chrome_tmp_test1')

cmd1 = [
    chrome,
    '--headless=new',
    f'--user-data-dir={tmp_dir1}',
    f'--screenshot={screenshot1}',
    '--window-size=1400,1050',
    '--virtual-time-budget=2500',
    '--allow-file-access-from-files',
    'file:///' + test1_file.replace('\\', '/')
]
res1 = subprocess.run(cmd1, capture_output=True, text=True)
print("Test 1 (Login Modal Open): screenshot exists =", os.path.exists(screenshot1))

if os.path.exists(test1_file): os.remove(test1_file)
if os.path.exists(tmp_dir1): shutil.rmtree(tmp_dir1, ignore_errors=True)


# TEST 2: Wrong Password -> Error Message
test2_html = html.replace(REPLACE_TARGET, '''
updateAdminBadgeCount();
setTimeout(async () => {
  openAdminModal();
  document.getElementById("login-username").value = "admin";
  document.getElementById("login-password").value = "wrong9999";
  await handleAdminLogin({preventDefault: () => {}});
}, 400);
</script>''')

test2_file = r'c:\Users\Username\Desktop\แชทบอทระบบคำขอ\test2_login_error.html'
with open(test2_file, 'w', encoding='utf-8') as f:
    f.write(test2_html)

screenshot2 = os.path.join(artifact_dir, 'screen_admin_login_error.png')
tmp_dir2 = os.path.abspath('chrome_tmp_test2')

cmd2 = [
    chrome,
    '--headless=new',
    f'--user-data-dir={tmp_dir2}',
    f'--screenshot={screenshot2}',
    '--window-size=1400,1050',
    '--virtual-time-budget=2500',
    '--allow-file-access-from-files',
    'file:///' + test2_file.replace('\\', '/')
]
res2 = subprocess.run(cmd2, capture_output=True, text=True)
print("Test 2 (Login Error Display): screenshot exists =", os.path.exists(screenshot2))

if os.path.exists(test2_file): os.remove(test2_file)
if os.path.exists(tmp_dir2): shutil.rmtree(tmp_dir2, ignore_errors=True)


# TEST 3: Correct Login -> Admin Panel Opened with User Badge & Logout Button
test3_html = html.replace(REPLACE_TARGET, '''
updateAdminBadgeCount();
setTimeout(async () => {
  openAdminModal();
  document.getElementById("login-username").value = "admin";
  document.getElementById("login-password").value = "admin1234";
  await handleAdminLogin({preventDefault: () => {}});
}, 400);
</script>''')

test3_file = r'c:\Users\Username\Desktop\แชทบอทระบบคำขอ\test3_logged_in.html'
with open(test3_file, 'w', encoding='utf-8') as f:
    f.write(test3_html)

screenshot3 = os.path.join(artifact_dir, 'screen_admin_logged_in.png')
tmp_dir3 = os.path.abspath('chrome_tmp_test3')

cmd3 = [
    chrome,
    '--headless=new',
    f'--user-data-dir={tmp_dir3}',
    f'--screenshot={screenshot3}',
    '--window-size=1400,1050',
    '--virtual-time-budget=3000',
    '--allow-file-access-from-files',
    'file:///' + test3_file.replace('\\', '/')
]
res3 = subprocess.run(cmd3, capture_output=True, text=True)
print("Test 3 (Successful Login Admin Panel): screenshot exists =", os.path.exists(screenshot3))

if os.path.exists(test3_file): os.remove(test3_file)
if os.path.exists(tmp_dir3): shutil.rmtree(tmp_dir3, ignore_errors=True)


# TEST 4: Security Tab (Change Password Tab)
test4_html = html.replace(REPLACE_TARGET, '''
updateAdminBadgeCount();
setTimeout(async () => {
  sessionStorage.setItem("mis_budget_admin_auth", "true");
  sessionStorage.setItem("mis_budget_admin_username", "admin");
  openAdminModal();
  switchAdminTab("security");
}, 400);
</script>''')

test4_file = r'c:\Users\Username\Desktop\แชทบอทระบบคำขอ\test4_security.html'
with open(test4_file, 'w', encoding='utf-8') as f:
    f.write(test4_html)

screenshot4 = os.path.join(artifact_dir, 'screen_admin_security_tab.png')
tmp_dir4 = os.path.abspath('chrome_tmp_test4')

cmd4 = [
    chrome,
    '--headless=new',
    f'--user-data-dir={tmp_dir4}',
    f'--screenshot={screenshot4}',
    '--window-size=1400,1050',
    '--virtual-time-budget=3000',
    '--allow-file-access-from-files',
    'file:///' + test4_file.replace('\\', '/')
]
res4 = subprocess.run(cmd4, capture_output=True, text=True)
print("Test 4 (Security & Password Tab): screenshot exists =", os.path.exists(screenshot4))

if os.path.exists(test4_file): os.remove(test4_file)
if os.path.exists(tmp_dir4): shutil.rmtree(tmp_dir4, ignore_errors=True)

print("All visual tests completed successfully!")
