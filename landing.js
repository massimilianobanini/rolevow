(() => {
  "use strict";
  const field = document.getElementById("starter-text");
  const button = document.getElementById("copy-starter");
  const status = document.getElementById("release-status");
  if (!field || !button || !status) return;
  button.addEventListener("click", async () => {
    try {
      if (!navigator.clipboard || typeof navigator.clipboard.writeText !== "function") throw new Error("No clipboard");
      await navigator.clipboard.writeText(field.value);
      status.textContent = "Copied. Open a new ChatGPT conversation, paste the message and send it.";
    } catch (_) {
      field.focus(); field.select();
      status.textContent = "Copy the selected text manually, then paste it into a new ChatGPT conversation.";
    }
  });
})();
