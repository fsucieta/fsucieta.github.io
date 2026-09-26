document.addEventListener("DOMContentLoaded",()=>{document.querySelectorAll(".share-buttons-container").forEach(s=>{const t=s,c=()=>{const e=t.dataset.url;return e&&e.startsWith("http")?e:e?`${window.location.origin}/${e.replace(/^\.\//,"").replace(/^\//,"")}`:window.location.href},l=t.dataset.title||document.title,r=t.dataset.chapeau||"";t.querySelector(".share-x-btn")?.addEventListener("click",e=>{e.preventDefault(),e.stopPropagation();const n=c(),o=`🔴 Enquête L'OCHJU : ${l}

${r?r.slice(0,140)+"...":""}

À lire ici :`;window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(o)}&url=${encodeURIComponent(n)}`,"_blank","noopener,noreferrer,width=600,height=400")}),t.querySelector(".share-wa-btn")?.addEventListener("click",e=>{e.preventDefault(),e.stopPropagation();const n=c(),o=`🔴 *Enquête L'OCHJU : ${l}*

${r?r+`

`:""}👉 ${n}`;window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(o)}`,"_blank","noopener,noreferrer")}),t.querySelector(".share-copy-btn")?.addEventListener("click",e=>{e.preventDefault(),e.stopPropagation();const n=c();navigator.clipboard.writeText(n).then(()=>{const o=t.querySelector(".share-copy-btn"),i=o?.querySelector(".copy-label"),a=o?.querySelector(".copy-icon");i&&a&&(i.innerText="Copié !",a.innerText="✅",setTimeout(()=>{i.innerText="Copier",a.innerText="🔗"},2500))})})})});
