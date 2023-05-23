import {change_profile_information} from "../../services/api/user";
import store from "@/store/index";

export const profileModule = {
    state: () => ({
        isSuccess: false
    }),
    actions: {
        async changeUserInformation({commit}, data) {
            store.state.login.isLoading = true
            try {
                store.state.login.user = await change_profile_information(data)
                commit("setSuccess", true)
                store.state.login.isLoading = false
            } catch (e) {
                store.state.login.isLoading = true
                commit("setError", e.message)
                store.state.login.isLoading = false
                throw new Error(e)
            }
        }
    },
    mutations: {
        setSuccess(state, success) {
            state.isSuccess = success
            setTimeout(() => state.isSuccess = false, 3000);
        },
        setError(state, error) {
            store.state.login.error = error
            setTimeout(() => store.state.login.error = null, 3000);

        }
    },
    namespaced: true

}