import {auth, profile} from "../../services/api";
import store from "@/store/index";
import {clearTokens, getTokens, storageTokens} from "../../services/storage";

export const loginModule =
    {
        state: () => ({
            user: null,
            tokens: getTokens(),
            isLoading: null,
            error: null
        }),
        actions: {
            async loginUser({commit}, data) {
                try {
                    const resp_tokens = await auth(data.username, data.password)
                    storageTokens(resp_tokens.access, resp_tokens.refresh);
                    commit("setTokens", resp_tokens)
                    await store.dispatch('login/loadUser')
                } catch (e) {
                    commit("setError", e)
                }
            },
            async loadUser({state, commit}) {
                try {
                    const user = await profile()
                    commit("setUser", user)
                } catch (e) {
                    console.log(e);
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
            },
            setError(state, error) {
                state.error = error
            }
        },
        namespaced: true
    }