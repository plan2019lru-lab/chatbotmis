# -*- coding: utf-8 -*-
"""
Helper to update backdrop click and escape handlers in both files.
"""

def update_events(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_snippet = """imgModal.onclick = (e) => {
  if(e.target === imgModal) closeImageModal();
};

// Escape Key Hierarchy: Close modal first, or drawer if modal not open
document.addEventListener("keydown", (e) => {
  if(e.key === "Escape"){
    if(adminModal && adminModal.classList.contains("open")){
      closeAdminModal();
    } else if(imgModal.classList.contains("open")){
      closeImageModal();
    } else if(previewDrawer.classList.contains("open")){
      closePagePreview();
    }
  }
});"""

    new_snippet = """imgModal.onclick = (e) => {
  if(e.target === imgModal) closeImageModal();
};
if(adminModal){
  adminModal.onclick = (e) => {
    if(e.target === adminModal) closeAdminModal();
  };
}
if(adminLoginModal){
  adminLoginModal.onclick = (e) => {
    if(e.target === adminLoginModal) closeAdminLoginModal();
  };
}

// Escape Key Hierarchy: Close modal first, or drawer if modal not open
document.addEventListener("keydown", (e) => {
  if(e.key === "Escape"){
    if(adminLoginModal && adminLoginModal.classList.contains("open")){
      closeAdminLoginModal();
    } else if(adminModal && adminModal.classList.contains("open")){
      closeAdminModal();
    } else if(imgModal.classList.contains("open")){
      closeImageModal();
    } else if(previewDrawer.classList.contains("open")){
      closePagePreview();
    }
  }
});"""

    if old_snippet in content:
        content = content.replace(old_snippet, new_snippet, 1)
        print(f"Updated event handlers in {filepath}")
    elif "adminLoginModal.onclick" in content:
        print(f"Event handlers already updated in {filepath}")
    else:
        # Check CRLF
        old_crlf = old_snippet.replace('\n', '\r\n')
        new_crlf = new_snippet.replace('\n', '\r\n')
        if old_crlf in content:
            content = content.replace(old_crlf, new_crlf, 1)
            print(f"Updated event handlers (CRLF) in {filepath}")
        else:
            print(f"Snippet not found in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_events('mis-budget-chatbot-app.html')
    update_events('index.html')

    with open('mis-budget-chatbot-app.html', 'rb') as f1, open('index.html', 'rb') as f2:
        assert f1.read() == f2.read(), "Files must be identical!"
    print("Files remain 100% identical.")
