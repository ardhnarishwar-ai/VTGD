import { calculateNetWeight } from "./netWeight";
import { calculateDiffusion } from "./diffusion";
import { calculatePrediction } from "./prediction";

export interface VTGDResult {

    netWeight: number;
    diffusion: number;

    mode: string;
    confidence: number;

}

export function runVTGD(

    pcr: number,
    delta: number,
    gamma: number,
    theta: number,
    vega: number

): VTGDResult {

    const nw = calculateNetWeight(
        pcr,
        delta,
        gamma,
        theta,
        vega
    );

    const diffusion =
        calculateDiffusion(
            nw.value,
            vega
        );

    const prediction =
        calculatePrediction(
            nw.value,
            diffusion.value
        );

    return {

        netWeight: nw.value,

        diffusion: diffusion.value,

        mode: prediction.mode,

        confidence: prediction.confidence

    };

}
