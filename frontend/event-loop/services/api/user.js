import store from "@/store";
import {check_token} from "../token_verify";
import {instance} from "./instance"
import axios from "axios";

export async function auth(email, password) {
    try {
        const response = await instance.post('/token/', {email, password})
        return response.data;
    } catch (e) {
        if (e.response.status === 401) {
            throw new Error("Ошибка при вводе данных")
        } else if (e.response.status === 500) {
            throw new Error("Ошибка сервера")
        } else {
            throw new Error("Произошла ошибка")
        }
    }

}

export async function registration(data) {
    try {
        const response = await instance.post('/users/registration/', data)
        return response.data
    } catch (e) {
        if (e.response.status === 400) {
            throw new Error("Ошибка при вводе данных")
        } else if (e.response.status === 500) {
            throw new Error("Ошибка сервера")
        } else {
            throw new Error("Произошла ошибка")
        }
    }
}

export async function profile() {
    try {
        await check_token(store.state.login.tokens, instance)
        const response = await instance.get('/users/profile/')
        return response.data
    } catch (e) {
        if (e.response.status === 400) {
            throw new Error("Ошибка при вводе данных")
        } else if (e.response.status === 500) {
            throw new Error("Ошибка сервера")
        } else {
            throw new Error("Произошла ошибка")
        }
    }
}

export async function change_profile_information(data) {
    try {
        await check_token(store.state.login.tokens, instance)
        let response
        if (!Object.keys(data).includes('password')) {
            response = await instance.patch(`/users/${store.state.login.user.id}/`, data)
        } else {
            response = await instance.post(`/users/${store.state.login.user.id}/set_password/`, data)
        }
        return response.data
    } catch (e) {
        if (e.response.status === 400) {
            throw new Error("Ошибка при вводе данных")
        } else if (e.response.status === 500) {
            throw new Error("Ошибка сервера")
        } else {
            throw new Error("Произошла ошибка")
        }
    }
}


export async function forgotPassword(email) {
    const response = await instance.post(`/forgot_password/`, email)
    return response.data
}

export async function resetPassword(data) {
    const response = await instance.post(`/reset_password/`, data)
    return response.data
}

export async function yandexToken(data) {
    console.log('я тут')
    const response = await axios.post(`http://127.0.0.1:8000/api/yandex_token/`, data)
    return response.data
}