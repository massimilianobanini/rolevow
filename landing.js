/* Adapted from the Divertoscopio landing launch contract (same author).
   The pre-release source permits technical playtests only.
   No unsupported ChatGPT query parameter, telemetry or third-party services. */
(() => {
  "use strict";
  const repo = "https://github.com/massimilianobanini/rolevow";
  const prompt = repo + "\n\nLet's begin.";
  const root = document.body;
  const field = document.getElementById("starter-text");
  const button = document.getElementById("copy-starter");
  const status = document.getElementById("release-status");
  if (!root || !field || !button || !status) return;
  field.value = prompt;
  const released = ["pre-release", "released"].includes(root.getAttribute("data-release-status"));
  button.disabled = !released;
  if (!released) {
    status.textContent = "Disabled: the repository is not available for technical testing.";
    return;
  }
  status.textContent = "Copy the message, open a new conversation at chatgpt.com, paste it and send. Repository-loading behavior is not guaranteed. The monetary guarantee is not active.";
  button.addEventListener("click", async () => {
    let copied = false;
    if (navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
      try { await navigator.clipboard.writeText(prompt); copied = true; } catch (_) { /* Manual copy fallback below */ }
    }
    if (copied) {
      status.textContent = "Copied. Now open https://chatgpt.com/ in a new tab, paste the message into a new conversation and send it.";
    } else {
      field.focus(); field.select();
      status.textContent = "Automatic clipboard access is unavailable. Select and copy the highlighted text manually, then paste it into a new ChatGPT conversation.";
    }
  });
})();
