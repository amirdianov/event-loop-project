import {check_token} from "../token_verify";
import store from "@/store";
import {instance} from "./instance";

export async function subscribe(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.post(`/subscribe/`, data)
    return response.data
}

export async function unsubscribe(data) {
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