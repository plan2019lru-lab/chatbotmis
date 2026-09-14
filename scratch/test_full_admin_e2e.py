# -*- coding: utf-8 -*-
import subprocess
import os
import shutil
import json

app_path = r'c:\Users\Username\Desktop\แชทบอทระบบคำขอ\mis-budget-chatbot-app.html'
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open(app_path, 'r', encoding='utf-8') as f:
    html = f.read()

REPLACE_TARGET = 'updateAdminBadgeCount();\n</script>'
if REPLACE_TARGET not in html:
    REPLACE_TARGET = 'updateAdminBadgeCount();\r\n</script>'

e2e_js = '''
updateAdminBadgeCount();

window.testResults = [];
function record(name, pass, detail) {
  window.testResults.push({ name, pass, detail });
}

window.runFullTestSuite = async function() {
  try {
    // 1. Initially logged out
    record("Initial auth is false", !isAdminLoggedIn(), "isAdminLoggedIn() == false");

    // 2. Open modal when logged out -> opens login modal
    openAdminModal();
    const loginModalOpen = adminLoginModal.classList.contains("open");
    const adminModalClosed = !adminModal.classList.contains("open");
    record("openAdminModal opens Login Modal", loginModalOpen && adminModalClosed, "loginModalOpen=" + loginModalOpen);

    // 3. Test invalid login
    document.getElementById("login-username").value = "admin";
    document.getElementById("login-password").value = "wrong_pass_123";
    await handleAdminLogin({preventDefault: () => {}});
    const errShown = document.getElementById("login-error-alert").style.display !== "none";
    record("Wrong password triggers error alert", errShown, "login error shown");
    record("Still logged out after bad pass", !isAdminLoggedIn(), "isAdminLoggedIn() == false");

    // 4. Test valid login
    document.getElementById("login-password").value = "admin1234";
    await handleAdminLogin({preventDefault: () => {}});
    const isAuthed = isAdminLoggedIn();
    const adminModalOpen = adminModal.classList.contains("open");
    const loginModalClosed = !adminLoginModal.classList.contains("open");
    record("Correct password logs in successfully", isAuthed && adminModalOpen && loginModalClosed, "Admin modal open");

    // 5. Verify user display in header
    const userDisplay = document.getElementById("admin-user-display").textContent;
    record("Header shows correct admin user", userDisplay.includes("admin"), userDisplay);

    // 6. Switch to Security Tab
    switchAdminTab("security");
    const secTabActive = document.getElementById("admin-tab-security").classList.contains("active");
    record("Switch to Security Tab", secTabActive, "Security tab active");

    // 7. Test Change Password
    document.getElementById("sec-input-cur-pass").value = "admin1234";
    document.getElementById("sec-input-new-pass").value = "newPass2026";
    document.getElementById("sec-input-confirm-pass").value = "newPass2026";
    await saveNewAdminPassword();
    const secAlert = document.getElementById("sec-alert-msg");
    const passChangeSuccess = secAlert && secAlert.textContent.includes("สำเร็จ");
    record("Change password to newPass2026", passChangeSuccess, secAlert ? secAlert.textContent : "");

    // 8. Test Logout
    logoutAdmin();
    const loggedOutAfter = !isAdminLoggedIn();
    const adminClosedAfterLogout = !adminModal.classList.contains("open");
    record("Logout clears session & closes modal", loggedOutAfter && adminClosedAfterLogout, "Logged out");

    // 9. Test old password fails
    document.getElementById("login-username").value = "admin";
    document.getElementById("login-password").value = "admin1234";
    await handleAdminLogin({preventDefault: () => {}});
    record("Old password rejected", !isAdminLoggedIn(), "Old password rejected");

    // 10. Test new password succeeds
    document.getElementById("login-password").value = "newPass2026";
    await handleAdminLogin({preventDefault: () => {}});
    record("New password accepted", isAdminLoggedIn(), "New password logged in");

    // 11. Reset password to default
    // bypass window.confirm
    window.confirm = () => true;
    resetAdminPasswordDefault();
    const credsAfterReset = getStoredAdminCreds();
    record("Reset credentials back to default", credsAfterReset.passwordHash === DEFAULT_PASSWORD_HASH, "Reset OK");

    // Final result dump
    const div = document.createElement("div");
    div.id = "test-results-dump";
    div.textContent = JSON.stringify(window.testResults);
    document.body.appendChild(div);

  } catch(err) {
    record("Execution Exception", false, err.toString());
    const div = document.createElement("div");
    div.id = "test-results-dump";
    div.textContent = JSON.stringify(window.testResults);
    document.body.appendChild(div);
  }
};

setTimeout(window.runFullTestSuite, 400);
</script>
'''

test_file = r'c:\Users\Username\Desktop\แชทบอทระบบคำขอ\test_e2e_runner.html'
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(html.replace(REPLACE_TARGET, e2e_js))

tmp_dir = os.path.abspath('chrome_tmp_e2e')
output_dom_file = os.path.abspath('dom_dump.txt')

cmd = [
    chrome,
    '--headless=new',
    f'--user-data-dir={tmp_dir}',
    '--dump-dom',
    '--virtual-time-budget=3500',
    '--allow-file-access-from-files',
    'file:///' + test_file.replace('\\', '/')
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
output = res.stdout

if '<div id="test-results-dump">' in output:
    start = output.find('<div id="test-results-dump">') + len('<div id="test-results-dump">')
    end = output.find('</div>', start)
    results_json = output[start:end]
    results = json.loads(results_json)
    print("=" * 60)
    print(f"E2E TEST RESULTS: {len(results)} tests executed")
    print("=" * 60)
    all_pass = True
    for r in results:
        status = "PASSED [✓]" if r['pass'] else "FAILED [X]"
        print(f"{status:12} : {r['name']} ({r['detail']})")
        if not r['pass']:
            all_pass = False
    print("=" * 60)
    print("ALL TESTS PASSED!" if all_pass else "SOME TESTS FAILED!")
else:
    print("Could not find test-results-dump in DOM output!")
    print("Output length:", len(output))

if os.path.exists(test_file): os.remove(test_file)
if os.path.exists(tmp_dir): shutil.rmtree(tmp_dir, ignore_errors=True)
