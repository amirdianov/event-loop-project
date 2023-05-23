import {check_token} from "../token_verify";
import store from "@/store";
import {instance} from "./instance";

export async function all_events(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get('/events', {params: {slug: data}})
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

export async function update_event(data) {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.patch(`/my_events/${data.id}/`, data.data, {
        "content-type": `multipart/form-data; boundary=${data._boundary}`,
    },)
    return response.data
}

export async function user_events() {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get('/my_events/')
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