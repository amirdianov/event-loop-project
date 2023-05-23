import axios from "axios";
import {API_URL} from "../consts";
import store from "@/store";

export const instance = axios.create({
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