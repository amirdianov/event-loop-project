import axios from "axios";
import {API_URL} from "./consts";
import store from "@/store";
import {getTokens, storageAccessToken} from "./storage";


const instance = axios.create({
    baseURL: API_URL,
});

instance.interceptors.request.use(function (config) {
    if (store.state.login.tokens) {
        config.headers['Authorization'] = `Bearer ${store.state.login.tokens.access}`;
    }
    return config;
}, function (error) {
    return Promise.reject(error);
});

export async function auth(email, password) {
    const response = await instance.post('/token/', {email, password})
    return response.data;
}


export async function profile() {
    try {
        const response_verify = await access_token_verify(getTokens().access)
        const response = await instance.get('/profile/')
        return response.data
    } catch (e) {
        try {
            const response_access_token_new = await access_token_refresh(getTokens().refresh)
            storageAccessToken(response_access_token_new.data.access)
            store.state.login.tokens.access = response_access_token_new.data.access
            const response = await instance.get('/profile/')
            return response.data
        } catch (e) {
            throw new Error(e)
        }
    }
}

export async function access_token_verify(token) {
    return await instance.post('/token/verify/', {"token": token});

}

export async function access_token_refresh(refresh_token) {
    return await instance.post('/token/refresh/', {"refresh": refresh_token});
}