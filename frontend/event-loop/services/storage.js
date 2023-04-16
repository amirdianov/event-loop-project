export function storageTokens(ac_tok, ref_tok) {
    localStorage.setItem("access", ac_tok);
    localStorage.setItem("refresh", ref_tok);

}

export function storageAccessToken(ac_tok) {
    localStorage.setItem("access", ac_tok);
}

export function getTokens() {
    return {
        "access": localStorage.getItem("access"),
        "refresh": localStorage.getItem("refresh")
    }
}

export function clearTokens() {
    localStorage.setItem("access", null);
    localStorage.setItem("refresh", null);
}