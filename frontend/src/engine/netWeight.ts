export interface NetWeightResult {

    value: number;
    status: string;

}

export function calculateNetWeight(

    pcr: number,
    delta: number,
    gamma: number,
    theta: number,
    vega: number

): NetWeightResult {

    const value =

        (pcr * 0.30) +
        (delta * 0.25) +
        (gamma * 0.20) +
        (vega * 0.15) -
        (theta * 0.10);

    let status = "Neutral";

    if (value > 0.60)
        status = "Buyer Dominant";

    else if (value < 0.40)
        status = "Seller Dominant";

    return {

        value,
        status

    };

}
