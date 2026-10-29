document.addEventListener("DOMContentLoaded",()=>{document.querySelectorAll(".share-buttons-container").forEach(p=>{const n=p,a=()=>{const e=n.dataset.url;return e&&e.startsWith("http")?e:`https://fsucieta.github.io${window.location.pathname}`},s=n.dataset.title||document.title,r=n.dataset.chapeau||"",l=r?r.length>120?r.slice(0,117)+"...":r:"";n.querySelector(".share-x-btn")?.addEventListener("click",e=>{e.preventDefault(),e.stopPropagation();const t=a(),o=`🔴 ENQUÊTE L'OCHJU : ${s}

${l}

👉 Preuves & Actes scellés :
${t}

#Corse #LOchju`;window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(o)}`,"_blank","noopener,noreferrer,width=600,height=440")}),n.querySelector(".share-wa-btn")?.addEventListener("click",e=>{e.preventDefault(),e.stopPropagation();const t=a(),o=`🔴 *Enquête L'OCHJU : ${s}*

${r?r+`

`:""}⚖️ *Dossier d'instruction et preuves scellées :*
👉 ${t}

_« Le Savoir partagé est notre contre-pouvoir. »_`;window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(o)}`,"_blank","noopener,noreferrer")}),n.querySelector(".share-tg-btn")?.addEventListener("click",e=>{e.preventDefault(),e.stopPropagation();const t=a(),o=`🔴 Enquête L'OCHJU : ${s}

${r?r+`

`:""}⚖️ Dossier d'instruction et preuves scellées :`;window.open(`https://t.me/share/url?url=${encodeURIComponent(t)}&text=${encodeURIComponent(o)}`,"_blank","noopener,noreferrer")}),n.querySelector(".share-fb-btn")?.addEventListener("click",e=>{e.preventDefault(),e.stopPropagation();const t=a();window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(t)}`,"_blank","noopener,noreferrer,width=600,height=400")}),n.querySelector(".share-native-btn")?.addEventListener("click",async e=>{e.preventDefault(),e.stopPropagation();const t=a();if(navigator.share)try{await navigator.share({title:`Enquête L'OCHJU : ${s}`,text:l||`Enquête L'OCHJU : ${s}`,url:t})}catch{}}),n.querySelector(".share-copy-btn")?.addEventListener("click",e=>{e.preventDefault(),e.stopPropagation();const t=a();navigator.clipboard.writeText(t).then(()=>{const o=n.querySelector(".share-copy-btn"),c=o?.querySelector(".copy-label"),i=o?.querySelector(".copy-icon");c&&i&&(c.innerText="Copié !",i.innerText="✅",setTimeout(()=>{c.innerText="Copier",i.innerText="🔗"},2500))})})})});
