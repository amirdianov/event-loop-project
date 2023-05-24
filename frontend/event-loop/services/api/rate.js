import {check_token} from "../token_verify";
import store from "@/store";
import {instance} from "./instance";

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
