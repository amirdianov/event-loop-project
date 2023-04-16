import store from "@/store";
import {storageAccessToken} from "./storage";

export async function check_token(tokens, instance) {
    try {
        const response_verify_access = await access_token_verify(tokens.access, instance)
        const response_verify_refresh = await access_token_verify(tokens.refresh, instance)
        return response_verify_access.data
    } catch (e) {
        try {
            const response_access_token_new = await access_token_refresh(tokens.refresh, instance)
            storageAccessToken(response_access_token_new.data.access)
            store.state.login.tokens.access = response_access_token_new.data.access
            return response_access_token_new.data
        } catch (e) {
            throw new Error(e)
        }
    }
}


export async function access_token_verify(token, instance) {
    return await instance.post('/token/verify/', {"token": token});

}

export async function access_token_refresh(refresh_token, instance) {
    return await instance.post('/token/refresh/', {"refresh": refresh_token});
}