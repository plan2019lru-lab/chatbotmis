import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('mis-budget-chatbot-app.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update CSS: add .btn-admin-action.admin-hidden
old_css = """.btn-admin-action {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    color: var(--navy) !important;
    font-weight: 500 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    transition: all .15s ease !important;
  }
  .btn-admin-action:hover {
    background: #f1f5f9 !important;
    border-color: #94a3b8 !important;
    transform: translateY(-1px);
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  }"""

new_css = """.btn-admin-action {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    color: var(--navy) !important;
    font-weight: 500 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    transition: all .15s ease !important;
  }
  .btn-admin-action:hover {
    background: #f1f5f9 !important;
    border-color: #94a3b8 !important;
    transform: translateY(-1px);
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  }
  .btn-admin-action.admin-hidden {
    display: none !important;
  }"""

assert old_css in text, "Could not find old_css"
text = text.replace(old_css, new_css, 1)

# 2. Update HTML: add admin-hidden class to #btn-admin-panel
old_btn = '<button class="btn-action btn-admin-action" id="btn-admin-panel" onclick="openAdminModal()" title="แผงจัดการข้อมูลสำหรับผู้ดูแลระบบ">'
new_btn = '<button class="btn-action btn-admin-action admin-hidden" id="btn-admin-panel" onclick="openAdminModal()" title="แผงจัดการข้อมูลสำหรับผู้ดูแลระบบ">'
assert old_btn in text, "Could not find old_btn"
text = text.replace(old_btn, new_btn, 1)

# 3. Add Brand title attribute
old_brand = '<div id="brand">'
new_brand = '<div id="brand" title="ระบบผู้ช่วยคำของบประมาณ LRU">'
if old_brand in text:
    text = text.replace(old_brand, new_brand, 1)

# 4. Replace sha256Hex and remove comment for admin1234
old_hash_def = 'const DEFAULT_PASSWORD_HASH = "ac9689e2272427085e35b9d3e3e8bed88cb3434828b43b86fc0596cad4c6e270"; // SHA-256 for "admin1234"'
new_hash_def = 'const DEFAULT_PASSWORD_HASH = "ac9689e2272427085e35b9d3e3e8bed88cb3434828b43b86fc0596cad4c6e270";'
assert old_hash_def in text, "Could not find old_hash_def"
text = text.replace(old_hash_def, new_hash_def, 1)

old_sha256 = """async function sha256Hex(text) {
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
}"""

new_sha256 = """function pureSha256(ascii) {
  function rightRotate(value, amount) {
    return (value >>> amount) | (value << (32 - amount));
  }
  var mathPow = Math.pow;
  var maxWord = mathPow(2, 32);
  var lengthProperty = 'length';
  var i, j;
  var result = '';
  var words = [];
  var asciiBitLength = ascii[lengthProperty] * 8;
  var hash = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
  ];
  var k = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
  ];
  var composite = '';
  for (var n = 0; n < ascii[lengthProperty]; n++) {
    var charCode = ascii.charCodeAt(n);
    if (charCode < 128) {
      composite += String.fromCharCode(charCode);
    } else if (charCode < 2048) {
      composite += String.fromCharCode((charCode >> 6) | 192);
      composite += String.fromCharCode((charCode & 63) | 128);
    } else {
      composite += String.fromCharCode((charCode >> 12) | 224);
      composite += String.fromCharCode(((charCode >> 6) & 63) | 128);
      composite += String.fromCharCode((charCode & 63) | 128);
    }
  }
  ascii = composite;
  asciiBitLength = ascii[lengthProperty] * 8;
  ascii += '\\x80';
  while (ascii[lengthProperty] % 64 - 56) ascii += '\\x00';
  for (i = 0; i < ascii[lengthProperty]; i++) {
    j = ascii.charCodeAt(i);
    words[i >> 2] |= j << ((3 - i) % 4) * 8;
  }
  words[words[lengthProperty]] = ((asciiBitLength / maxWord) | 0);
  words[words[lengthProperty]] = (asciiBitLength);
  for (j = 0; j < words[lengthProperty];) {
    var w = words.slice(j, j += 16);
    var oldHash = hash;
    hash = hash.slice(0, 8);
    for (i = 0; i < 64; i++) {
      var i2 = i + j;
      var w15 = w[i - 15], w2 = w[i - 2];
      var a = hash[0], e = hash[4];
      var temp1 = hash[7]
        + (rightRotate(e, 6) ^ rightRotate(e, 11) ^ rightRotate(e, 25))
        + ((e & hash[5]) ^ ((~e) & hash[6]))
        + k[i]
        + (w[i] = (i < 16) ? w[i] : (
            w[i - 16]
            + (rightRotate(w15, 7) ^ rightRotate(w15, 18) ^ (w15 >>> 3))
            + w[i - 7]
            + (rightRotate(w2, 17) ^ rightRotate(w2, 19) ^ (w2 >>> 10))
          ) | 0
        );
      var temp2 = (rightRotate(a, 2) ^ rightRotate(a, 13) ^ rightRotate(a, 22))
        + ((a & hash[1]) ^ (a & hash[2]) ^ (hash[1] & hash[2]));
      hash = [(temp1 + temp2) | 0].concat(hash);
      hash[4] = (hash[4] + temp1) | 0;
    }
    for (i = 0; i < 8; i++) {
      hash[i] = (hash[i] + oldHash[i]) | 0;
    }
  }
  for (i = 0; i < 8; i++) {
    for (i2 = 3; i2 >= 0; i2--) {
      var b = (hash[i] >> (i2 * 8)) & 255;
      result += ((b < 16) ? '0' : '') + b.toString(16);
    }
  }
  return result;
}

async function sha256Hex(text) {
  try {
    if (window.crypto && window.crypto.subtle) {
      const msgUint8 = new TextEncoder().encode(text);
      const hashBuffer = await crypto.subtle.digest("SHA-256", msgUint8);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      return hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
    }
  } catch(e) {
    console.warn("Subtle crypto error, using pureSha256 fallback:", e);
  }
  return pureSha256(text);
}"""

assert old_sha256 in text, "Could not find old_sha256"
text = text.replace(old_sha256, new_sha256, 1)

# 5. Remove admin1234 from handleAdminLogin
old_login_check = """  const isUserValid = inputUser.toLowerCase() === creds.username.toLowerCase();
  const isPassValid = (inputHash === creds.passwordHash) ||
                      (creds.passwordHash === DEFAULT_PASSWORD_HASH && inputPass === "admin1234");"""

new_login_check = """  const isUserValid = inputUser.toLowerCase() === creds.username.toLowerCase();
  const isPassValid = (inputHash === creds.passwordHash);"""

assert old_login_check in text, "Could not find old_login_check"
text = text.replace(old_login_check, new_login_check, 1)

# Also ensure checkAdminVisibility is called in handleAdminLogin
old_login_success = """    if (rememberChk && rememberChk.checked) {
      localStorage.setItem(STORAGE_KEY_ADMIN_AUTH, "true");
      localStorage.setItem(STORAGE_KEY_ADMIN_USER, creds.username);
    } else {
      localStorage.removeItem(STORAGE_KEY_ADMIN_AUTH);
    }
    closeAdminLoginModal();
    openAdminModal();"""

new_login_success = """    if (rememberChk && rememberChk.checked) {
      localStorage.setItem(STORAGE_KEY_ADMIN_AUTH, "true");
      localStorage.setItem(STORAGE_KEY_ADMIN_USER, creds.username);
    } else {
      localStorage.removeItem(STORAGE_KEY_ADMIN_AUTH);
    }
    checkAdminVisibility();
    closeAdminLoginModal();
    openAdminModal();"""

assert old_login_success in text, "Could not find old_login_success"
text = text.replace(old_login_success, new_login_success, 1)

# 6. Remove admin1234 from saveNewAdminPassword
old_save_check = """  const isCurValid = (curHash === creds.passwordHash) ||
                     (creds.passwordHash === DEFAULT_PASSWORD_HASH && curPass === "admin1234");"""

new_save_check = """  const isCurValid = (curHash === creds.passwordHash);"""

assert old_save_check in text, "Could not find old_save_check"
text = text.replace(old_save_check, new_save_check, 1)

# 7. Add checkAdminVisibility to logoutAdmin
old_logout = """function logoutAdmin() {
  sessionStorage.removeItem(STORAGE_KEY_ADMIN_AUTH);
  sessionStorage.removeItem(STORAGE_KEY_ADMIN_USER);
  localStorage.removeItem(STORAGE_KEY_ADMIN_AUTH);
  localStorage.removeItem(STORAGE_KEY_ADMIN_USER);
  closeAdminModal();
  alert("ออกจากระบบผู้ดูแลเรียบร้อยแล้ว");
}"""

new_logout = """function logoutAdmin() {
  sessionStorage.removeItem(STORAGE_KEY_ADMIN_AUTH);
  sessionStorage.removeItem(STORAGE_KEY_ADMIN_USER);
  localStorage.removeItem(STORAGE_KEY_ADMIN_AUTH);
  localStorage.removeItem(STORAGE_KEY_ADMIN_USER);
  closeAdminModal();
  checkAdminVisibility();
  alert("ออกจากระบบผู้ดูแลเรียบร้อยแล้ว");
}"""

assert old_logout in text, "Could not find old_logout"
text = text.replace(old_logout, new_logout, 1)

# 8. Add checkAdminVisibility, Hotkey, and Logo Easter Egg
old_modal_close = """function closeAdminModal() {
  if (!adminModal) return;
  adminModal.classList.remove("open");
}"""

new_modal_close = """function closeAdminModal() {
  if (!adminModal) return;
  adminModal.classList.remove("open");
}

function checkAdminVisibility() {
  const adminBtn = document.getElementById("btn-admin-panel");
  if (!adminBtn) return;
  const urlParams = new URLSearchParams(window.location.search);
  const hasAdminQuery = urlParams.has("admin") || window.location.hash === "#admin";
  
  if (isAdminLoggedIn() || hasAdminQuery) {
    adminBtn.classList.remove("admin-hidden");
  } else {
    adminBtn.classList.add("admin-hidden");
  }
}

// Secret Hotkey: Ctrl+Shift+A or Cmd+Shift+A to trigger Admin
document.addEventListener("keydown", (e) => {
  if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === "A" || e.key === "a")) {
    e.preventDefault();
    const adminBtn = document.getElementById("btn-admin-panel");
    if (adminBtn) adminBtn.classList.remove("admin-hidden");
    if (isAdminLoggedIn()) {
      openAdminModal();
    } else {
      openAdminLoginModal();
    }
  }
});

// Logo Easter Egg: Click Brand logo 5 times within 3 seconds
let brandClickCount = 0;
let brandClickTimer = null;
const brandEl = document.getElementById("brand");
if (brandEl) {
  brandEl.style.cursor = "pointer";
  brandEl.addEventListener("click", () => {
    brandClickCount++;
    clearTimeout(brandClickTimer);
    if (brandClickCount >= 5) {
      brandClickCount = 0;
      const adminBtn = document.getElementById("btn-admin-panel");
      if (adminBtn) adminBtn.classList.remove("admin-hidden");
      if (isAdminLoggedIn()) {
        openAdminModal();
      } else {
        openAdminLoginModal();
      }
    } else {
      brandClickTimer = setTimeout(() => { brandClickCount = 0; }, 3000);
    }
  });
}"""

assert old_modal_close in text, "Could not find old_modal_close"
text = text.replace(old_modal_close, new_modal_close, 1)

# 9. In initialization, call checkAdminVisibility()
old_init = """renderTopics();
renderQuickRow();
greet();
updateAdminBadgeCount();"""

new_init = """renderTopics();
renderQuickRow();
greet();
updateAdminBadgeCount();
checkAdminVisibility();"""

assert old_init in text, "Could not find old_init"
text = text.replace(old_init, new_init, 1)

# Write back to mis-budget-chatbot-app.html and index.html
with open('mis-budget-chatbot-app.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated mis-budget-chatbot-app.html and index.html successfully!')
