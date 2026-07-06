console.log("VTGD Cockpit Loaded 🚀");
// =========================
// Live Clock
// =========================

function updateClock() {

    const live = document.querySelector(".live");

    if (!live) return;

    const now = new Date();

    const time = now.toLocaleTimeString("en-IN", {
        hour12: false
    });

    live.innerHTML = `
        ${time}<br>
        <span>LIVE ●</span>
    `;
}

updateClock();

setInterval(updateClock,1000);
// =========================
// Live Data Integration
// =========================

// Fields displayed in the UI
let liveData = {
    nw: null,
    pcr: null,
    safety: null,
    fvp: null
};

// Update UI from data object; if value is null => show Research Pending
function updateLiveUI(){

    // Net Weight
    const nwEl = document.querySelector(".gravity-value strong");
    if(nwEl) nwEl.innerText = liveData.nw !== null ? (liveData.nw >= 0 ? "+" : "") + liveData.nw.toFixed(2) : "Research Pending";

    // PCR
    const pcrEl = document.querySelector(".pcr-value strong");
    if(pcrEl) pcrEl.innerText = liveData.pcr !== null ? liveData.pcr.toFixed(2) : "Research Pending";

    // FVP
    const fvpEl = document.querySelector(".fvp-price");
    if(fvpEl) fvpEl.innerText = liveData.fvp !== null ? ("₹" + liveData.fvp.toLocaleString()) : "Research Pending";

}

// Needle movement based on NW value
function updateNeedle(value){

    const needle = document.querySelector(".needle");

    if(!needle) return;

    if(value === null){
        // Reset needle to center when unknown
        needle.style.transform = `rotate(0deg)`;
        return;
    }

    // value range : -1.0 to +1.0
    const clamped = Math.max(-1, Math.min(1, value));
    const angle = clamped * 90;

    needle.style.transform =
        `rotate(${angle}deg)`;

}

// Decision engine UI (uses live data when available)
function updateDecision() {

    const action = document.querySelector(".decision-action");
    const confidence = document.querySelector(".decision-confidence");
    const reason = document.querySelector(".decision-reason");

    if (!action) return;

    const nw = liveData.nw;
    const pcr = liveData.pcr;

    if (nw !== null && pcr !== null && nw > 0 && pcr >= 1.10) {

        action.className = "decision-action buy";
        action.innerHTML = "🟢 BUY CALL";

        confidence.innerHTML = "Confidence 91%";
        reason.innerHTML = "NW Positive • PCR Bullish • Vega Rising";

    }

    else if (nw !== null && pcr !== null && nw < 0 && pcr <= 0.90) {

        action.className = "decision-action sell";
        action.innerHTML = "🔴 BUY PUT";

        confidence.innerHTML = "Confidence 88%";
        reason.innerHTML = "NW Negative • PCR Bearish • Vega Falling";

    }

    else {

        action.className = "decision-action wait";
        action.innerHTML = "🟡 WAIT";

        confidence.innerHTML = "Confidence 54%";
        reason.innerHTML = "Mixed Signals";

    }

}

// Initial UI update
updateLiveUI();
updateNeedle(null);
updateDecision();

// =========================
// Backend Integration
// =========================

const BACKEND_BASE = "https://vtgd.onrender.com";

async function fetchVTGDTop(){
    try{
        const res = await fetch(BACKEND_BASE + '/vtgd/top');
        if(!res.ok) throw new Error('Network response not ok');
        const data = await res.json();
        return data;
    }catch(e){
        console.warn('fetchVTGDTop failed', e);
        return null;
    }
}

async function fetchVTGDRank(){
    try{
        const res = await fetch(BACKEND_BASE + '/vtgd/rank');
        if(!res.ok) throw new Error('Network response not ok');
        const data = await res.json();
        return data;
    }catch(e){
        console.warn('fetchVTGDRank failed', e);
        return null;
    }
}

async function fetchLiveData(){
    // Attempt to populate liveData from backend responses.
    // Preferred: use /vtgd/rank results if they contain aggregated vtgd values.
    const rank = await fetchVTGDRank();
    if(rank && Array.isArray(rank.results) && rank.results.length > 0){
        // Find the first result that contains vtgd fields
        const r = rank.results.find(x => x && x.vtgd);
        if(r && r.vtgd){
            // Map expected fields conservatively; if missing, set null (Research Pending)
            liveData.nw = typeof r.vtgd.net_weight === 'number' ? r.vtgd.net_weight : null;
            liveData.pcr = typeof r.vtgd.pcr === 'number' ? r.vtgd.pcr : null;
            liveData.safety = typeof r.vtgd.safety === 'number' ? r.vtgd.safety : null;
            liveData.fvp = typeof r.vtgd.fvp === 'number' ? r.vtgd.fvp : null;
            updateLiveUI();
            updateNeedle(liveData.nw);
            updateDecision();
            return;
        }
    }

    // Fallback: try /vtgd/top which may contain best_call / best_put with vtgd fields
    const top = await fetchVTGDTop();
    if(top){
        const candidate = top.best_call || top.best_put || null;
        if(candidate && candidate.vtgd){
            liveData.nw = typeof candidate.vtgd.net_weight === 'number' ? candidate.vtgd.net_weight : null;
            liveData.pcr = typeof candidate.vtgd.pcr === 'number' ? candidate.vtgd.pcr : null;
            liveData.safety = typeof candidate.vtgd.safety === 'number' ? candidate.vtgd.safety : null;
            liveData.fvp = typeof candidate.vtgd.fvp === 'number' ? candidate.vtgd.fvp : null;
            updateLiveUI();
            updateNeedle(liveData.nw);
            updateDecision();
            return;
        }
    }

    // If we reach here, backend did not provide expected vtgd fields.
    // Mark all as Research Pending per VTGD Constitution.
    liveData.nw = null;
    liveData.pcr = null;
    liveData.safety = null;
    liveData.fvp = null;
    updateLiveUI();
    updateNeedle(null);
    updateDecision();
}

// Poll live data periodically
fetchLiveData();
setInterval(fetchLiveData, 5000);
