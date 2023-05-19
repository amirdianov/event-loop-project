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
        console.log(store.state.login.tokens)
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
        let response
        console.log(data, Object.keys(data))
        if (!Object.keys(data).includes('password')) {
            response = await instance.patch(`/users/${store.state.login.user.id}/`, data)
        } else {
            response = await instance.post(`/users/${store.state.login.user.id}/set_password/`, data)
        }
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

export async function user_event(event_id) {
    // метод для получения информации о мероприятии пользователя, для редактирования информации о нем
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/my_events/${event_id}`)
    return response.data
}

export async function getEvent(event_id) {
    // метод для получения информации о мероприятии, включая всю информацию о рейтинге и об ораганизаторах
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/events/${event_id}/`)
    return response.data
}

export async function getEventComments(event_id) {
    // метод для получения информации о мероприятии, включая всю информацию о рейтинге и об ораганизаторах
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/event_comments`, {params: {event_id: event_id}})
    return response.data
}

export async function addEventComment(data) {
    // метод для получения информации о мероприятии, включая всю информацию о рейтинге и об ораганизаторах
    await check_token(store.state.login.tokens, instance)
    const response = await instance.post(`/event_comments/`, data)
    return response.data
}

export async function update_event(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.patch(`/my_events/${data.id}/`, data.data, {
        "content-type": `multipart/form-data; boundary=${data._boundary}`,
    },)
    return response.data
}

export async function getTags() {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/tags`)
    return response.data
}

export async function setRate(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.post(`/rate/`, data)
    return response.data
}

export async function getEventRate(event_id) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/rate`, {params: {event_id: event_id}})
    return response.data
}

export async function subscribe(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.post(`/subscribe/`, data)
    return response.data
}

export async function subscribers(event_id) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/subscribers/`, {params: {event_id: event_id}})
    return response.data
}

export async function getUsersSubscribedEvents() {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/user_subscriptions`)
    return response.data
}

export async function forgotPassword(email) {
    const response = await instance.post(`/forgot_password/`, email)
    return response.data
}

export async function resetPassword(data) {
    const response = await instance.post(`/reset_password/`, data)
    return response.data
}


export async function payEvent(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.post(`/pay_event/`, data)
    return response.data
}

export async function getPKForPay(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/get_pk/`, data)
    return response.data
}


export async function getPayResponse(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/pay_event_response/`, {params: {payment_id: data}})
    return response.data
}