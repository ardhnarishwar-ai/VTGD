export interface Strike {

    strike: number;
    type: "CE" | "PE";

    nw: number;
    safety: number;
    pcr: number;
    fvp: number;

    score: number;

}

export function rankStrikes(

    strikes: Strike[]

): Strike[] {

    return strikes.sort(

        (a, b) => b.score - a.score

    );

}
