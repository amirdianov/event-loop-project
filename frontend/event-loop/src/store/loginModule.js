import axios from "axios";
import {API_URL} from "../../services/consts";

const instance = axios.create({
    baseURL: API_URL,
});
export const loginModule =
    {
        state: () => ({
            user: null,
            tokens: {
                refresh_token: null,
                access_token: null,
            },
        }),
        actions: {
            async loginUser({state, commit}, data) {
                let email = data.username;
                let password = data.password;
                console.log(email, password)
                const resp = await instance.post('/auth/', {email, password})
                console.log(resp.data.refresh)
                console.log(resp.data.access)

            }
        },
        getters: {
            getRefreshToken(state) {
                return state.tokens.refresh_token
            },
            getAccessToken(state) {
                return state.tokens.access_token
            },
            getUser(state) {
                return state.user
            },
            isAuth(state) {
                return state.user != null
            }
        },
        mutations: {
            setUser(state, user) {
                state.user = user
            },
            setAccessToken(state, new_access_toke) {
                state.tokens.access_token = new_access_toke
            }
        },
        namespaced: true
    }