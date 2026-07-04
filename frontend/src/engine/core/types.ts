export interface Greeks {

    delta: number;
    gamma: number;
    theta: number;
    vega: number;

}

export interface NetWeight {

    value: number;
    status: string;

}

export interface Diffusion {

    value: number;
    state: string;

}

export interface Prediction {

    mode: string;
    confidence: number;

}

export interface Strike {

    strike: number;
    type: "CE" | "PE";

    score: number;
    safety: number;

}

export interface OptionData {

    pcr: number;

    greeks: Greeks;

}
