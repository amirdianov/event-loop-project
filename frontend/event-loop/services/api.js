import axios from "axios";
import {API_URL} from "./consts";
import {getTokens} from "./storage";
import store from "@/store";


const instance = axios.create({
    baseURL: API_URL,
});

// instance.interceptors.request.use(function (config) {
//     if (getUser) {
//         config.headers['Authorization'] = `Bearer ${getTokens().access_token}`;
//     }
//     return config;
// }, function (error) {
//     return Promise.reject(error);
// });

export async function auth(email, password) {
    const response = await instance.post('/auth/', {email, password})
    return response.data;
}


export async function profile() {
    const instance_new = axios.create({
        baseURL: API_URL,
        headers: {'Authorization': `Bearer ${getTokens().access_token}`} // Заголовок запроса
    });
    const response = await instance_new.get('/profile/')
    return response.data;
}

