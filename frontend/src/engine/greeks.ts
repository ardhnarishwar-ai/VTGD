export interface Greeks {

    delta: number;
    gamma: number;
    theta: number;
    vega: number;

}

export function normalizeGreek(
    value: number,
    min: number,
    max: number
): number {

    return Math.max(
        0,
        Math.min(
            1,
            (value - min) / (max - min)
        )
    );

}
