# -*- coding: utf-8 -*-
"""
Helper script to apply Admin Login feature to both index.html and mis-budget-chatbot-app.html.
Ensures both files remain 100% identical.
"""

import os
import hashlib

CSS_TO_INSERT = """  /* Admin Login Modal & Security Styles */
  .admin-login-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(15, 23, 42, 0.75);
    backdrop-filter: blur(6px);
    z-index: 1050;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 16px;
  }
  .admin-login-overlay.open {
    display: flex;
  }
  .admin-login-card {
    width: 430px;
    max-width: 94vw;
    background: #ffffff;
    border-radius: 18px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35), 0 0 0 1px rgba(255,255,255,0.1);
    overflow: hidden;
    animation: adminModalFadeIn 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .admin-login-header {
    background: linear-gradient(135deg, var(--navy) 0%, var(--navy-dark) 100%);
    color: #fff;
    padding: 20px 22px;
    display: flex;
    align-items: center;
    gap: 14px;
    position: relative;
  }
  .admin-login-icon {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    background: rgba(255,255,255,0.16);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
  }
  .admin-login-title-wrap {
    flex: 1;
  }
  .admin-login-title {
    font-size: 16px;
    font-weight: 700;
    color: #fff;
    margin: 0;
    line-height: 1.3;
  }
  .admin-login-sub {
    font-size: 11.5px;
    color: #94a3b8;
    margin: 3px 0 0 0;
  }
  .admin-login-close {
    background: rgba(255,255,255,0.12);
    border: none;
    color: #fff;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    font-size: 18px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background .15s ease;
  }
  .admin-login-close:hover {
    background: rgba(255,255,255,0.25);
  }
  .admin-login-body {
    padding: 22px 24px;
  }
  .input-with-icon {
    position: relative;
    display: flex;
    align-items: center;
  }
  .input-lead-icon {
    position: absolute;
    left: 12px;
    font-size: 14px;
    color: #64748b;
    pointer-events: none;
  }
  .form-control-icon {
    padding-left: 36px !important;
    padding-right: 38px !important;
  }
  .btn-toggle-eye {
    position: absolute;
    right: 10px;
    background: none;
    border: none;
    cursor: pointer;
    font-size: 15px;
    padding: 4px;
    border-radius: 4px;
    color: #64748b;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .btn-toggle-eye:hover {
    color: var(--ink);
  }
  .login-remember-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 12px 0 16px 0;
    font-size: 12.5px;
    color: #475569;
  }
  .login-remember-label {
    display: flex;
    align-items: center;
    gap: 7px;
    cursor: pointer;
    user-select: none;
  }
  .login-default-hint {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 8px;
    padding: 9px 12px;
    font-size: 12px;
    color: #166534;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 7px;
    line-height: 1.4;
  }
  .login-actions-bar {
    display: flex;
    gap: 10px;
    justify-content: flex-end;
  }
  .btn-login-submit {
    background: linear-gradient(135deg, var(--navy) 0%, var(--teal) 100%);
    color: #fff;
    font-weight: 600;
    padding: 9px 20px;
    border: none;
    border-radius: 9px;
    cursor: pointer;
    font-size: 13.5px;
    font-family: inherit;
    transition: all .15s ease;
    box-shadow: 0 4px 10px rgba(25, 53, 87, 0.25);
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .btn-login-submit:hover {
    box-shadow: 0 6px 15px rgba(25, 53, 87, 0.35);
    transform: translateY(-1px);
  }
  .btn-login-cancel {
    background: #f1f5f9;
    color: #475569;
    border: 1px solid #cbd5e1;
    padding: 9px 16px;
    border-radius: 9px;
    font-size: 13.5px;
    font-family: inherit;
    cursor: pointer;
    transition: background .15s ease;
  }
  .btn-login-cancel:hover {
    background: #e2e8f0;
  }
  .login-alert-danger {
    background: #fef2f2;
    border: 1px solid #fecaca;
    color: #991b1b;
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 12.5px;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .admin-header-right {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .admin-user-pill {
    background: rgba(255,255,255,0.15);
    color: #e2e8f0;
    font-size: 12px;
    padding: 4px 10px;
    border-radius: 20px;
    font-weight: 500;
    display: inline-flex;
    align-items: center;
    gap: 5px;
  }
  .btn-admin-logout {
    background: rgba(239, 68, 68, 0.22);
    border: 1px solid rgba(239, 68, 68, 0.45);
    color: #fecaca;
    padding: 5px 12px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    font-family: inherit;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    transition: all .15s ease;
  }
  .btn-admin-logout:hover {
    background: #ef4444;
    color: #ffffff;
    border-color: #ef4444;
  }
"""

LOGIN_MODAL_HTML = """<!-- ADMIN LOGIN MODAL -->
<div id="admin-login-modal" class="admin-login-overlay">
  <div class="admin-login-card">
    <div class="admin-login-header">
      <div class="admin-login-icon">🔐</div>
      <div class="admin-login-title-wrap">
        <h3 class="admin-login-title">เข้าสู่ระบบสำหรับผู้ดูแลระบบ</h3>
        <p class="admin-login-sub">แผงจัดการข้อมูลระบบคำของบประมาณ มรภ.เลย</p>
      </div>
      <button type="button" class="admin-login-close" onclick="closeAdminLoginModal()" title="ปิด">&times;</button>
    </div>

    <form id="admin-login-form" class="admin-login-body" onsubmit="handleAdminLogin(event); return false;" autocomplete="off">
      <div id="login-error-alert" class="login-alert-danger" style="display:none;">
        <span>⚠️</span>
        <span id="login-error-text">ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง</span>
      </div>

      <div class="form-group" style="margin-bottom: 14px;">
        <label class="form-label" for="login-username">ชื่อผู้ใช้งาน (Username) <span class="req">*</span></label>
        <div class="input-with-icon">
          <span class="input-lead-icon">👤</span>
          <input type="text" id="login-username" class="form-control form-control-icon" placeholder="admin" value="admin" required>
        </div>
      </div>

      <div class="form-group" style="margin-bottom: 12px;">
        <label class="form-label" for="login-password">รหัสผ่าน (Password) <span class="req">*</span></label>
        <div class="input-with-icon">
          <span class="input-lead-icon">🔑</span>
          <input type="password" id="login-password" class="form-control form-control-icon" placeholder="ระบุรหัสผ่าน" required>
          <button type="button" class="btn-toggle-eye" id="btn-toggle-pass" onclick="togglePasswordVisibility()" title="แสดง/ซ่อนรหัสผ่าน">👁️</button>
        </div>
      </div>

      <div class="login-remember-row">
        <label class="login-remember-label">
          <input type="checkbox" id="login-remember" checked>
          <span>จดจำการเข้าสู่ระบบในเครื่องนี้</span>
        </label>
      </div>

      <div class="login-default-hint">
        <span>💡 <strong>ค่าเริ่มต้นระบบ:</strong> ชื่อผู้ใช้ <code>admin</code> | รหัสผ่าน <code>admin1234</code></span>
      </div>

      <div class="login-actions-bar">
        <button type="button" class="btn-login-cancel" onclick="closeAdminLoginModal()">ยกเลิก</button>
        <button type="submit" class="btn-login-submit" id="btn-submit-login">
          <span>เข้าสู่ระบบ ➔</span>
        </button>
      </div>
    </form>
  </div>
</div>
"""

ADMIN_HEADER_OLD = """    <div class="admin-modal-header">
      <div class="admin-modal-title">
        <div class="admin-header-icon">⚙️</div>
        <div>
          <div class="admin-title-text">แผงจัดการข้อมูลสำหรับผู้ดูแลระบบ (Admin Control Panel)</div>
          <div class="admin-sub-text">เพิ่มคำถาม-คำตอบเพิ่มเติม ดูประวัติคำถาม และสำรองข้อมูลระบบ</div>
        </div>
      </div>
      <button class="admin-close-btn" id="btn-close-admin" onclick="closeAdminModal()">&times;</button>
    </div>"""

ADMIN_HEADER_NEW = """    <div class="admin-modal-header">
      <div class="admin-modal-title">
        <div class="admin-header-icon">⚙️</div>
        <div>
          <div class="admin-title-text">แผงจัดการข้อมูลสำหรับผู้ดูแลระบบ (Admin Control Panel)</div>
          <div class="admin-sub-text">เพิ่มคำถาม-คำตอบเพิ่มเติม ดูประวัติคำถาม และสำรองข้อมูลระบบ</div>
        </div>
      </div>
      <div class="admin-header-right">
        <span class="admin-user-pill" id="admin-user-display">👤 ผู้ดูแล: admin</span>
        <button class="btn-admin-logout" id="btn-admin-logout" onclick="logoutAdmin()" title="ออกจากระบบแอดมิน">
          <span>🚪 ออกจากระบบ</span>
        </button>
        <button class="admin-close-btn" id="btn-close-admin" onclick="closeAdminModal()" title="ปิดหน้าต่าง">&times;</button>
      </div>
    </div>"""

ADMIN_TABS_OLD = """      <button class="admin-tab-btn" data-tab="backup-sync" id="atab-btn-sync" onclick="switchAdminTab('backup-sync')">
        <span>💾 สำรองข้อมูล & Google Sheets</span>
      </button>
    </div>"""

ADMIN_TABS_NEW = """      <button class="admin-tab-btn" data-tab="backup-sync" id="atab-btn-sync" onclick="switchAdminTab('backup-sync')">
        <span>💾 สำรองข้อมูล & Google Sheets</span>
      </button>
      <button class="admin-tab-btn" data-tab="security" id="atab-btn-security" onclick="switchAdminTab('security')">
        <span>🔑 ความปลอดภัย & รหัสผ่าน</span>
      </button>
    </div>"""

ADMIN_TAB4_HTML = """
      <!-- TAB 4: SECURITY & CHANGE PASSWORD -->
      <div class="admin-tab-content" id="admin-tab-security">
        <div class="admin-form-card" style="max-width: 520px; margin: 0 auto;">
          <div class="admin-form-title">
            <span>🔑 เปลี่ยนรหัสผ่านผู้ดูแลระบบ (Change Admin Password)</span>
          </div>
          <div style="font-size: 12.5px; color: var(--muted); margin-bottom: 16px; line-height: 1.5;">
            รหัสผ่านจะถูกเข้ารหัส SHA-256 บันทึกไว้ในอุปกรณ์ของคุณอย่างปลอดภัย เพื่อป้องกันผู้ใช้งานทั่วไปเข้าถึงข้อมูล
          </div>

          <div class="form-group" style="margin-bottom: 14px;">
            <label class="form-label">ชื่อผู้ใช้งาน (Username)</label>
            <input type="text" id="sec-input-username" class="form-control" value="admin" readonly style="background:#f1f5f9;cursor:not-allowed;">
          </div>

          <div class="form-group" style="margin-bottom: 14px;">
            <label class="form-label">รหัสผ่านปัจจุบัน <span class="req">*</span></label>
            <input type="password" id="sec-input-cur-pass" class="form-control" placeholder="ระบุรหัสผ่านปัจจุบัน (ค่าเริ่มต้น admin1234)">
          </div>

          <div class="form-group" style="margin-bottom: 14px;">
            <label class="form-label">รหัสผ่านใหม่ <span class="req">*</span></label>
            <input type="password" id="sec-input-new-pass" class="form-control" placeholder="ระบุรหัสผ่านใหม่ (อย่างน้อย 4 ตัวอักษร)">
          </div>

          <div class="form-group" style="margin-bottom: 16px;">
            <label class="form-label">ยืนยันรหัสผ่านใหม่ <span class="req">*</span></label>
            <input type="password" id="sec-input-confirm-pass" class="form-control" placeholder="กรอกรหัสผ่านใหม่อีกครั้งเพื่อยืนยัน">
          </div>

          <div id="sec-alert-msg" style="display:none;padding:10px 14px;border-radius:8px;font-size:12.5px;margin-bottom:16px;"></div>

          <div style="display: flex; gap: 10px; justify-content: flex-end; align-items: center; border-top: 1px solid var(--line); padding-top: 16px;">
            <button type="button" class="btn-outline-primary" onclick="resetAdminPasswordDefault()">🔄 รีเซ็ตเป็นค่าเริ่มต้น</button>
            <button type="button" class="btn-primary" onclick="saveNewAdminPassword()">💾 บันทึกรหัสผ่านใหม่</button>
          </div>
        </div>
      </div>
"""

ADMIN_JS_CODE = """/* =========================================================
   ADMIN AUTHENTICATION & SECURITY CONTROLLER
   ========================================================= */
const STORAGE_KEY_ADMIN_AUTH = "mis_budget_admin_auth";
const STORAGE_KEY_ADMIN_USER = "mis_budget_admin_username";
const STORAGE_KEY_ADMIN_CREDS = "mis_budget_admin_creds";
const DEFAULT_ADMIN_USERNAME = "admin";
const DEFAULT_PASSWORD_HASH = "ac9689e2272427085e35b9d3e3e8bed88cb3434828b43b86fc0596cad4c6e270"; // SHA-256 for "admin1234"

async function sha256Hex(text) {
  try {
    if (window.crypto && window.crypto.subtle) {
      const msgUint8 = new TextEncoder().encode(text);
      const hashBuffer = await crypto.subtle.digest("SHA-256", msgUint8);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      return hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
    }
  } catch(e) {
    console.warn("Subtle crypto error, using fallback:", e);
  }
  let h = 0;
  for (let i = 0; i < text.length; i++) {
    h = ((h << 5) - h) + text.charCodeAt(i);
    h |= 0;
  }
  return "fb_" + Math.abs(h);
}

function getStoredAdminCreds() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY_ADMIN_CREDS);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed && parsed.passwordHash) return parsed;
    }
  } catch(e) {
    console.warn("Error reading admin creds:", e);
  }
  return {
    username: DEFAULT_ADMIN_USERNAME,
    passwordHash: DEFAULT_PASSWORD_HASH
  };
}

function isAdminLoggedIn() {
  const sessionAuth = sessionStorage.getItem(STORAGE_KEY_ADMIN_AUTH) === "true";
  const localAuth = localStorage.getItem(STORAGE_KEY_ADMIN_AUTH) === "true";
  return sessionAuth || localAuth;
}

function getAdminUsername() {
  return sessionStorage.getItem(STORAGE_KEY_ADMIN_USER) ||
         localStorage.getItem(STORAGE_KEY_ADMIN_USER) ||
         DEFAULT_ADMIN_USERNAME;
}

function updateAdminUserHeader() {
  const el = document.getElementById("admin-user-display");
  if (el) el.textContent = "👤 ผู้ดูแล: " + getAdminUsername();
  const secUser = document.getElementById("sec-input-username");
  if (secUser) secUser.value = getAdminUsername();
}

const adminLoginModal = document.getElementById("admin-login-modal");

function openAdminLoginModal() {
  if (!adminLoginModal) return;
  const userInp = document.getElementById("login-username");
  const passInp = document.getElementById("login-password");
  const errAlert = document.getElementById("login-error-alert");
  if (errAlert) errAlert.style.display = "none";
  if (passInp) passInp.value = "";
  if (userInp && !userInp.value) userInp.value = getAdminUsername();
  adminLoginModal.classList.add("open");
  setTimeout(() => {
    if (passInp) passInp.focus();
  }, 100);
}

function closeAdminLoginModal() {
  if (!adminLoginModal) return;
  adminLoginModal.classList.remove("open");
}

function togglePasswordVisibility() {
  const passInp = document.getElementById("login-password");
  const btn = document.getElementById("btn-toggle-pass");
  if (!passInp) return;
  if (passInp.type === "password") {
    passInp.type = "text";
    if (btn) btn.textContent = "🙈";
  } else {
    passInp.type = "password";
    if (btn) btn.textContent = "👁️";
  }
}

async function handleAdminLogin(e) {
  if (e && e.preventDefault) e.preventDefault();
  const userInp = document.getElementById("login-username");
  const passInp = document.getElementById("login-password");
  const rememberChk = document.getElementById("login-remember");
  const errAlert = document.getElementById("login-error-alert");
  const errText = document.getElementById("login-error-text");

  const inputUser = (userInp ? userInp.value : "").trim();
  const inputPass = passInp ? passInp.value : "";

  if (!inputUser || !inputPass) {
    if (errAlert) {
      errAlert.style.display = "flex";
      if (errText) errText.textContent = "กรุณาระบุชื่อผู้ใช้งานและรหัสผ่าน";
    }
    return;
  }

  const creds = getStoredAdminCreds();
  const inputHash = await sha256Hex(inputPass);

  const isUserValid = inputUser.toLowerCase() === creds.username.toLowerCase();
  const isPassValid = (inputHash === creds.passwordHash) ||
                      (creds.passwordHash === DEFAULT_PASSWORD_HASH && inputPass === "admin1234");

  if (isUserValid && isPassValid) {
    if (errAlert) errAlert.style.display = "none";
    sessionStorage.setItem(STORAGE_KEY_ADMIN_AUTH, "true");
    sessionStorage.setItem(STORAGE_KEY_ADMIN_USER, creds.username);
    if (rememberChk && rememberChk.checked) {
      localStorage.setItem(STORAGE_KEY_ADMIN_AUTH, "true");
      localStorage.setItem(STORAGE_KEY_ADMIN_USER, creds.username);
    } else {
      localStorage.removeItem(STORAGE_KEY_ADMIN_AUTH);
    }
    closeAdminLoginModal();
    openAdminModal();
  } else {
    if (errAlert) {
      errAlert.style.display = "flex";
      if (errText) errText.textContent = "ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง";
    }
    if (passInp) {
      passInp.select();
      passInp.focus();
    }
  }
}

function logoutAdmin() {
  sessionStorage.removeItem(STORAGE_KEY_ADMIN_AUTH);
  sessionStorage.removeItem(STORAGE_KEY_ADMIN_USER);
  localStorage.removeItem(STORAGE_KEY_ADMIN_AUTH);
  localStorage.removeItem(STORAGE_KEY_ADMIN_USER);
  closeAdminModal();
  alert("ออกจากระบบผู้ดูแลเรียบร้อยแล้ว");
}

async function saveNewAdminPassword() {
  const curPassInp = document.getElementById("sec-input-cur-pass");
  const newPassInp = document.getElementById("sec-input-new-pass");
  const confPassInp = document.getElementById("sec-input-confirm-pass");
  const alertBox = document.getElementById("sec-alert-msg");

  const curPass = curPassInp ? curPassInp.value : "";
  const newPass = newPassInp ? newPassInp.value : "";
  const confPass = confPassInp ? confPassInp.value : "";

  function showSecAlert(msg, isSuccess = false) {
    if (!alertBox) return;
    alertBox.style.display = "block";
    alertBox.style.background = isSuccess ? "#dcfce7" : "#fee2e2";
    alertBox.style.border = "1px solid " + (isSuccess ? "#86efac" : "#fca5a5");
    alertBox.style.color = isSuccess ? "#15803d" : "#b91c1c";
    alertBox.textContent = (isSuccess ? "✓ " : "⚠️ ") + msg;
  }

  if (!curPass) {
    showSecAlert("กรุณาระบุรหัสผ่านปัจจุบัน");
    if (curPassInp) curPassInp.focus();
    return;
  }
  if (!newPass || newPass.length < 4) {
    showSecAlert("รหัสผ่านใหม่ต้องมีความยาวอย่างน้อย 4 ตัวอักษร");
    if (newPassInp) newPassInp.focus();
    return;
  }
  if (newPass !== confPass) {
    showSecAlert("รหัสผ่านใหม่และยืนยันรหัสผ่านไม่ตรงกัน");
    if (confPassInp) confPassInp.focus();
    return;
  }

  const creds = getStoredAdminCreds();
  const curHash = await sha256Hex(curPass);
  const isCurValid = (curHash === creds.passwordHash) ||
                     (creds.passwordHash === DEFAULT_PASSWORD_HASH && curPass === "admin1234");

  if (!isCurValid) {
    showSecAlert("รหัสผ่านปัจจุบันไม่ถูกต้อง");
    if (curPassInp) { curPassInp.select(); curPassInp.focus(); }
    return;
  }

  const newHash = await sha256Hex(newPass);
  const updatedCreds = {
    username: creds.username,
    passwordHash: newHash,
    updatedAt: new Date().toLocaleString("th-TH")
  };

  try {
    localStorage.setItem(STORAGE_KEY_ADMIN_CREDS, JSON.stringify(updatedCreds));
    if (curPassInp) curPassInp.value = "";
    if (newPassInp) newPassInp.value = "";
    if (confPassInp) confPassInp.value = "";
    showSecAlert("เปลี่ยนรหัสผ่านผู้ดูแลระบบสำเร็จแล้ว!", true);
  } catch(e) {
    showSecAlert("เกิดข้อผิดพลาดในการบันทึก: " + e.message);
  }
}

function resetAdminPasswordDefault() {
  if (!confirm("คุณแน่ใจหรือไม่ว่าต้องการรีเซ็ตรหัสผ่านกลับเป็นค่าเริ่มต้น (admin1234)?")) {
    return;
  }
  try {
    localStorage.removeItem(STORAGE_KEY_ADMIN_CREDS);
    const alertBox = document.getElementById("sec-alert-msg");
    if (alertBox) {
      alertBox.style.display = "block";
      alertBox.style.background = "#dcfce7";
      alertBox.style.border = "1px solid #86efac";
      alertBox.style.color = "#15803d";
      alertBox.textContent = "✓ รีเซ็ตรหัสผ่านกลับเป็น admin1234 เรียบร้อยแล้ว";
    }
    const curPassInp = document.getElementById("sec-input-cur-pass");
    const newPassInp = document.getElementById("sec-input-new-pass");
    const confPassInp = document.getElementById("sec-input-confirm-pass");
    if (curPassInp) curPassInp.value = "";
    if (newPassInp) newPassInp.value = "";
    if (confPassInp) confPassInp.value = "";
  } catch(e) {
    alert("เกิดข้อผิดพลาด: " + e.message);
  }
}
"""

ADMIN_MODAL_FUNCS_OLD = """/* Modal Open & Close */
const adminModal = document.getElementById("admin-modal");

function openAdminModal() {
  if (!adminModal) return;
  adminModal.classList.add("open");
  switchAdminTab("custom-faqs");
  renderCustomFaqsList();
  renderQuestionLogsList();
  updateAdminBadgeCount();
}

function closeAdminModal() {
  if (!adminModal) return;
  adminModal.classList.remove("open");
}

function switchAdminTab(tabName) {
  document.querySelectorAll(".admin-tab-btn").forEach(b => b.classList.remove("active"));
  document.querySelectorAll(".admin-tab-content").forEach(c => c.classList.remove("active"));
  
  const targetBtn = document.getElementById(`atab-btn-${tabName === 'custom-faqs' ? 'faqs' : tabName === 'question-logs' ? 'logs' : 'sync'}`);
  const targetContent = document.getElementById(`admin-tab-${tabName}`);
  
  if (targetBtn) targetBtn.classList.add("active");
  if (targetContent) targetContent.classList.add("active");
  
  if (tabName === "custom-faqs") renderCustomFaqsList();
  if (tabName === "question-logs") renderQuestionLogsList();
}"""

ADMIN_MODAL_FUNCS_NEW = """/* Modal Open & Close */
const adminModal = document.getElementById("admin-modal");

function openAdminModal() {
  if (!isAdminLoggedIn()) {
    openAdminLoginModal();
    return;
  }
  if (!adminModal) return;
  updateAdminUserHeader();
  adminModal.classList.add("open");
  switchAdminTab("custom-faqs");
  renderCustomFaqsList();
  renderQuestionLogsList();
  updateAdminBadgeCount();
}

function closeAdminModal() {
  if (!adminModal) return;
  adminModal.classList.remove("open");
}

function switchAdminTab(tabName) {
  document.querySelectorAll(".admin-tab-btn").forEach(b => b.classList.remove("active"));
  document.querySelectorAll(".admin-tab-content").forEach(c => c.classList.remove("active"));
  
  let btnId = "atab-btn-faqs";
  if (tabName === "question-logs") btnId = "atab-btn-logs";
  else if (tabName === "backup-sync") btnId = "atab-btn-sync";
  else if (tabName === "security") btnId = "atab-btn-security";

  const targetBtn = document.getElementById(btnId);
  const targetContent = document.getElementById("admin-tab-" + tabName);
  
  if (targetBtn) targetBtn.classList.add("active");
  if (targetContent) targetContent.classList.add("active");
  
  if (tabName === "custom-faqs") renderCustomFaqsList();
  if (tabName === "question-logs") renderQuestionLogsList();
}"""


def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add CSS before </style>
    if "/* Admin Login Modal & Security Styles */" not in content:
        target = "</style>"
        pos = content.find(target)
        if pos == -1:
            raise ValueError(f"Could not find </style> in {filepath}")
        content = content[:pos] + CSS_TO_INSERT + "\n  " + content[pos:]
        print("  Added CSS.")
    else:
        print("  CSS already present.")

    # 2. Add Login Modal HTML before <!-- ADMIN CONTROL MODAL -->
    if "id=\"admin-login-modal\"" not in content:
        target = "<!-- ADMIN CONTROL MODAL -->"
        pos = content.find(target)
        if pos == -1:
            raise ValueError(f"Could not find {target} in {filepath}")
        content = content[:pos] + LOGIN_MODAL_HTML + "\n" + content[pos:]
        print("  Added Login Modal HTML.")
    else:
        print("  Login Modal HTML already present.")

    # 3. Update Admin Modal Header
    if ADMIN_HEADER_OLD in content:
        content = content.replace(ADMIN_HEADER_OLD, ADMIN_HEADER_NEW, 1)
        print("  Updated Admin Header.")
    elif "admin-user-pill" in content:
        print("  Admin Header already updated.")
    else:
        print("  Warning: ADMIN_HEADER_OLD not matched exactly.")

    # 4. Update Admin Tabs Bar
    if ADMIN_TABS_OLD in content:
        content = content.replace(ADMIN_TABS_OLD, ADMIN_TABS_NEW, 1)
        print("  Updated Admin Tabs Bar.")
    elif "atab-btn-security" in content:
        print("  Admin Tabs Bar already updated.")
    else:
        print("  Warning: ADMIN_TABS_OLD not matched exactly.")

    # 5. Add Tab 4 Content before closing </div></div></div> (end of admin modal)
    if "id=\"admin-tab-security\"" not in content:
        target = "        </div>\n      </div>\n    </div>\n  </div>\n</div>\n\n<script>"
        if target in content:
            replacement = "        </div>\n      </div>\n" + ADMIN_TAB4_HTML + "    </div>\n  </div>\n</div>\n\n<script>"
            content = content.replace(target, replacement, 1)
            print("  Added Tab 4 Content.")
        else:
            # try with \\r\\n
            target_crlf = target.replace("\n", "\r\n")
            if target_crlf in content:
                replacement_crlf = replacement.replace("\n", "\r\n")
                content = content.replace(target_crlf, replacement_crlf, 1)
                print("  Added Tab 4 Content (CRLF).")
            else:
                print("  Warning: Tab 4 insertion point not matched directly, searching alternative...")
                # Search for </div>\\s*</div>\\s*</div>\\s*<script>
                import re
                m = re.search(r'(\s*</div>\s*</div>\s*</div>\s*<script>)', content)
                if m:
                    content = content[:m.start()] + ADMIN_TAB4_HTML + "\n    </div>\n  </div>\n</div>\n\n<script>" + content[m.end():]
                    print("  Added Tab 4 Content via regex.")
                else:
                    raise ValueError("Could not find insertion point for Tab 4.")
    else:
        print("  Tab 4 HTML already present.")

    # 6. Add JS Authentication code before updateAdminBadgeCount()
    if "STORAGE_KEY_ADMIN_AUTH" not in content:
        target = "function updateAdminBadgeCount() {"
        pos = content.find(target)
        if pos == -1:
            raise ValueError(f"Could not find updateAdminBadgeCount in {filepath}")
        content = content[:pos] + ADMIN_JS_CODE + "\n" + content[pos:]
        print("  Added JS Authentication Code.")
    else:
        print("  JS Authentication Code already present.")

    # 7. Update openAdminModal & switchAdminTab
    if ADMIN_MODAL_FUNCS_OLD in content:
        content = content.replace(ADMIN_MODAL_FUNCS_OLD, ADMIN_MODAL_FUNCS_NEW, 1)
        print("  Updated openAdminModal & switchAdminTab.")
    elif "if (!isAdminLoggedIn())" in content:
        print("  openAdminModal already updated.")
    else:
        print("  Warning: ADMIN_MODAL_FUNCS_OLD not matched.")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Finished {filepath}.\n")


if __name__ == "__main__":
    process_file("mis-budget-chatbot-app.html")
    process_file("index.html")

    # Verify identical
    with open("mis-budget-chatbot-app.html", "rb") as f1, open("index.html", "rb") as f2:
        b1 = f1.read()
        b2 = f2.read()
        if b1 == b2:
            print("PERFECT: Both files are 100% identical!")
        else:
            print(f"MISMATCH: Lengths are {len(b1)} vs {len(b2)}")
