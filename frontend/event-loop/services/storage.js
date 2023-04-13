export function storeTokens(ac_tok, ref_tok) {
    localStorage.setItem("access_token", ac_tok);
    localStorage.setItem("refresh_token", ref_tok);

}

export function getTokens() {
    return {
        "access_token": localStorage.getItem("access_token"),
        "refresh_token": localStorage.getItem("refresh_token")
    }
}

export function clearTokens() {
    localStorage.setItem("access_token", null);
    localStorage.setItem("refresh_token", null);
}