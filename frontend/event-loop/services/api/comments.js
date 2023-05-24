import {check_token} from "../token_verify";
import store from "@/store";
import {instance} from "./instance";

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
