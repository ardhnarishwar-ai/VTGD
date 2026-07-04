import { VTGD } from "./constants";

export function normalize(

    value: number,
    min: number,
    max: number

): number {

    return Math.max(

        VTGD.MIN_WEIGHT,

        Math.min(

            VTGD.MAX_WEIGHT,

            (value - min) / (max - min)

        )

    );

}

export function clamp(

    value: number,
    min: number,
    max: number

): number {

    return Math.max(

        min,

        Math.min(max, value)

    );

}
