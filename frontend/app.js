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
// Demo Live Data
// =========================

const demo = {

    nw: 0.37,

    pcr: 1.34,

    safety: 82,

    fvp: 24982

};

function updateDemo(){

    // Net Weight
    const nw = document.querySelector(".gravity-value strong");

    if(nw) nw.innerText = "+" + demo.nw.toFixed(2);

    // PCR
    const pcr = document.querySelector(".pcr-value strong");

    if(pcr) pcr.innerText = demo.pcr.toFixed(2);

    // FVP
    const fvp = document.querySelector(".fvp-price");

    if(fvp) fvp.innerText = "₹" + demo.fvp.toLocaleString();

}

updateDemo();
// =========================
// Net Weight Needle
// =========================

function updateNeedle(value){

    const needle = document.querySelector(".needle");

    if(!needle) return;

    // value range : -1.0 to +1.0

    const angle = value * 90;

    needle.style.transform =
        `rotate(${angle}deg)`;

}

// Demo
updateNeedle(demo.nw);
// ==========================
// VTGD Decision Engine
// ==========================

function updateDecision() {

    const action = document.querySelector(".decision-action");
    const confidence = document.querySelector(".decision-confidence");
    const reason = document.querySelector(".decision-reason");

    if (!action) return;

    if (demo.nw > 0 && demo.pcr >= 1.10) {

        action.className = "decision-action buy";
        action.innerHTML = "🟢 BUY CALL";

        confidence.innerHTML = "Confidence 91%";
        reason.innerHTML = "NW Positive • PCR Bullish • Vega Rising";

    }

    else if (demo.nw < 0 && demo.pcr <= 0.90) {

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

updateDecision();
