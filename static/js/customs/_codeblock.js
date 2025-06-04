document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".copy-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const code = btn.closest(".group").querySelector("code").innerText;
      const originalText = btn.dataset.originalText || "Copy";
      const copiedText = btn.dataset.copiedText || "✓ Copied";

      navigator.clipboard.writeText(code).then(() => {
        btn.innerText = copiedText;
        setTimeout(() => {
          btn.innerText = originalText;
        }, 1500);
      });
    });
  });
});
