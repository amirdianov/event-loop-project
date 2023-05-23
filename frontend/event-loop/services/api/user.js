import store from "@/store";
import {check_token} from "../token_verify";
import {instance} from "./instance"

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


export async function forgotPassword(email) {
    const response = await instance.post(`/forgot_password/`, email)
    return response.data
}

export async function resetPassword(data) {
    const response = await instance.post(`/reset_password/`, data)
    return response.data
}