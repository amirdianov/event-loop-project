import axios from "axios";
import {API_URL} from "./consts";
import store from "@/store";
import {check_token} from "./token_verify";


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

export async function registration(data) {
    const response = await instance.post('/users/registration/', data)
    return response.data
}

export async function profile() {
    try {
        await check_token(store.state.login.tokens, instance)
        const response = await instance.get('/users/profile/')
        return response.data
    } catch (e) {
        throw new Error(e)
    }
}

export async function change_profile_information(data) {
    try {
        await check_token(store.state.login.tokens, instance)
        const response = await instance.patch(`/users/${store.state.login.user.id}/`, data)
        return response.data
    } catch (e) {
        throw new Error(e)
    }
}

export async function all_events(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get('/events/')
    return response.data
}