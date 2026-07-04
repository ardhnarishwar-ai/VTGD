export interface PredictionResult {

    mode: string;
    confidence: number;

}

export function calculatePrediction(

    netWeight: number,
    diffusion: number

): PredictionResult {

    let mode = "WAIT";
    let confidence = 50;

    if (netWeight > 0.60 && diffusion > 0.60) {

        mode = "BUY CALL";
        confidence = 92;

    }

    else if (netWeight < 0.40 && diffusion < 0.40) {

        mode = "BUY PUT";
        confidence = 92;

    }

    else {

        mode = "ZERO → HERO";
        confidence = 75;

    }

    return {

        mode,
        confidence

    };

}
