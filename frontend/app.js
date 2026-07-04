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
