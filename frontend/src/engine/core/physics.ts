/**
 * Market Gravity OS
 * Physics Layer
 *
 * Brownian Motion
 * ↓
 * Heat Equation
 * ↓
 * Diffusion
 * ↓
 * Market Gravity
 */

export const PHYSICS = {

    BROWNIAN: "Brownian Motion",

    HEAT: "Heat Equation",

    DIFFUSION: "Diffusion",

    GRAVITY: "Market Gravity",

    EQUILIBRIUM: "Fair Balance"

};

export function equilibrium(

    buyers: number,
    sellers: number

): number {

    return buyers - sellers;

}
