import {change_profile_information} from "../../services/api";
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
            } catch (e) {
                store.state.login.isLoading = true
                commit("setError", 'К сожалению, данные изменить не удалось')
            }
            store.state.login.isLoading = false
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