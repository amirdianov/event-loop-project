import {auth, profile, registration} from "../../services/api";
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
                commit("setLoading", true)
                commit("setError", null)
                try {
                    const resp_tokens = await auth(data.email, data.password)
                    storageTokens(resp_tokens.access, resp_tokens.refresh);
                    commit("setTokens", resp_tokens)
                    await store.dispatch('login/loadUser')
                } catch (e) {
                    commit("setLoading", false)
                    if (e.response.status === 401) {
                        commit("setError", "Проверьте корректность введенных данных")
                    }
                    if (e.response.status === 500) {
                        commit("setError", "Что-то пошло не так")
                    }
                    throw new Error(e)
                }
                commit("setLoading", false)
            },
            async registrationUser({commit}, data) {
                commit("setLoading", true)
                try {
                    const resp_tokens = await registration(data)
                    storageTokens(resp_tokens.access, resp_tokens.refresh);
                    commit("setTokens", resp_tokens)
                    await store.dispatch('login/loadUser')
                    commit("setError", null)
                } catch (e) {
                    commit("setLoading", false)
                    if (e.response.status === 400) {
                        commit("setError", "Проверьте правильность введенных данных")
                    }
                    if (e.response.status === 500) {
                        commit("setError", "Что-то пошло не так")
                    }
                    throw new Error(e)
                }
                commit("setLoading", false)
            },
            async loadUser({state, commit}) {
                commit("setLoading", true)
                try {
                    const user = await profile()
                    commit("setUser", user)
                } catch (e) {
                    console.log(e);
                }
                if (!state.user) {
                    await store.dispatch('login/logout')
                }
                commit("setLoading", false)
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
                setTimeout(() => state.error = null, 3000);
            },
            setLoading(state, loading) {
                state.isLoading = loading
            }
        },
        namespaced: true
    }