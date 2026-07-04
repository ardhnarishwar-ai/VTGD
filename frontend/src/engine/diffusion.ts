export interface DiffusionResult {

    value: number;
    state: string;

}

export function calculateDiffusion(

    netWeight: number,
    vega: number

): DiffusionResult {

    const value =

        (netWeight * 0.70) +
        (vega * 0.30);

    let state = "Balanced";

    if (value > 0.65)
        state = "Expansion";

    else if (value < 0.35)
        state = "Compression";

    return {

        value,
        state

    };

}
