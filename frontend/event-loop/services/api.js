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
    const response = await instance.get('/events', {params: {slug: data}})
    return response.data
}

export async function user_events() {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get('/my_events/')
    return response.data
}

export async function create_event(data) {
    for (const value of data.values()) {
        console.log(value);
    }
    await check_token(store.state.login.tokens, instance)

    const response = await instance.post('/my_events/', data, {
        "content-type": `multipart/form-data; boundary=${data._boundary}`,
    },)
    return response.data
}

export async function getUserEvent(event_id) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/my_events/${event_id}`)
    return response.data
}

export async function getEvent(event_id) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/events/${event_id}`)
    return response.data
}
