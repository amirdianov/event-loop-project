import store from "@/store/index";
import {all_events, user_events} from "../../services/api";

export const eventsModule = {
    state: () => ({
        allEvents: null,
        userEvents: null
    }),
    actions: {
        async loadAllEvents({commit}) {
            store.state.login.isLoading = true
            try {
                const events = await all_events()
                commit("setAllEvents", events)
            } catch (e) {
                store.state.login.isLoading = true
                commit("setError", 'Ошибка')
            }
            store.state.login.isLoading = false
        },
        async loadUsersEvents({commit}) {
            store.state.login.isLoading = true
            try {
                const events = await user_events()
                commit("setUserEvents", events)
            } catch (e) {
                store.state.login.isLoading = true
                commit("setError", 'Ошибка')
            }
            store.state.login.isLoading = false
        }
    },
    mutations: {
        setError(state, error) {
            store.state.login.error = error
            setTimeout(() => store.state.login.error = null, 3000);
        },
        setAllEvents(state, events) {
            state.allEvents = events
        },
        setUserEvents(state, events) {
            state.userEvents = events
        }
    },
    namespaced: true
}