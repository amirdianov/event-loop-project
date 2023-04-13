import {auth, profile} from "../../services/api";
import store from "@/store/index";
import {clearTokens, getTokens, storeTokens} from "../../services/storage";

export const loginModule =
    {
        state: () => ({
            user: null,
            tokens: getTokens(),
        }),
        actions: {
            async loginUser({commit}, data) {
                const resp_tokens = await auth(data.username, data.password)
                storeTokens(resp_tokens.access, resp_tokens.refresh);
                commit("setTokens", getTokens())
                await store.dispatch('login/loadUser')
            },
            async loadUser({state, commit}) {
                try {
                    const user = await profile(state.tokens.access_token)
                    commit("setUser", user)
                } catch (e) {
                    console.error(e);
                }
                if (!state.user) {
                    await store.dispatch('login/logout')
                }
            },
            logout({commit}) {
                commit("setUser", null);
                commit("setTokens", null)
                clearTokens();
            }
        },
        getters: {
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
            setTokens(state, values) {
                state.tokens = values
            }
        },
        namespaced: true
    }