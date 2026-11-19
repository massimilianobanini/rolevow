(() => {
  "use strict";
  const REPO="https://github.com/massimilianobanini/rolevow", CHATGPT="https://chatgpt.com/", START_PROMPT=REPO+"\n\nLet's begin.";
  const modal=document.getElementById("prompt-modal"), generatedPrompt=document.getElementById("generated-prompt"), copyStatus=document.getElementById("copy-status"), closeButton=document.getElementById("modal-close"), launchButton=document.getElementById("copy-and-open");
  if(!modal||!generatedPrompt||!copyStatus||!closeButton||!launchButton)return;
  let returnFocus=null, launchInProgress=false;
  function openPrompt(){returnFocus=document.activeElement;generatedPrompt.value=START_PROMPT;copyStatus.textContent="Press Copy and open ChatGPT. Then paste the copied message and send it in ChatGPT.";modal.hidden=false;document.body.style.overflow="hidden";closeButton.focus();}
  function closePrompt(){if(modal.hidden)return;modal.hidden=true;document.body.style.overflow="";if(returnFocus&&typeof returnFocus.focus==="function")returnFocus.focus();}
  async function copyPrompt(){const value=generatedPrompt.value;if(navigator.clipboard&&typeof navigator.clipboard.writeText==="function"){try{await navigator.clipboard.writeText(value);return true;}catch(_){}}
    generatedPrompt.focus();generatedPrompt.select();try{if(document.execCommand("copy"))return true;}catch(_){}return false;}
  document.querySelectorAll("[data-start-rolevow]").forEach(button=>button.addEventListener("click",openPrompt));
  closeButton.addEventListener("click",closePrompt);
  modal.addEventListener("click",event=>{if(event.target===modal)closePrompt();});
  document.addEventListener("keydown",event=>{if(modal.hidden)return;if(event.key==="Escape"){event.preventDefault();closePrompt();return;}if(event.key!=="Tab")return;const focusable=Array.from(modal.querySelectorAll("button, a[href], textarea")).filter(element=>!element.disabled&&element.getClientRects().length);if(!focusable.length)return;const first=focusable[0],last=focusable[focusable.length-1];if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}});
  launchButton.addEventListener("click",async()=>{if(launchInProgress)return;launchInProgress=true;launchButton.disabled=true;
    const copyAttempt=copyPrompt();let chatTab=null;try{chatTab=window.open("about:blank","_blank");if(chatTab)chatTab.opener=null;}catch(_){}
    try{const copied=await copyAttempt;if(!copied){if(chatTab&&!chatTab.closed)chatTab.close();copyStatus.textContent="Copying failed. No ChatGPT conversation was opened. Copy the selected message manually, or allow clipboard access and try again.";return;}
      if(!chatTab||chatTab.closed){copyStatus.textContent="Message copied, but the browser blocked the new tab. Allow pop-ups and retry, or open chatgpt.com manually. This page is still available.";return;}
      try{chatTab.location.replace(CHATGPT);copyStatus.textContent="Message copied. ChatGPT opened in a new tab: paste the message and press Send.";}catch(_){try{chatTab.close();}catch(_){}copyStatus.textContent="Message copied, but ChatGPT could not open. Open chatgpt.com manually and paste it.";}
    }finally{launchInProgress=false;launchButton.disabled=false;}
  });
})();
