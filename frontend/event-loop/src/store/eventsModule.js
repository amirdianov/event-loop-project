import store from "@/store/index";
import {all_events as loadAllEvents} from "../../services/api";

export const eventsModule = {
    state: () => ({
        allEvents: null
    }),
    actions: {
        async loadEvents({commit}) {
            store.state.login.isLoading = true
            try {
                const events = await loadAllEvents()
                commit("setEvents", events)
            } catch (e) {
                store.state.login.isLoading = true
                commit("setError", 'К сожалению, данные изменить не удалось')
            }
            store.state.login.isLoading = false
        }
    },
    mutations: {
        setError(state, error) {
            store.state.login.error = error
            setTimeout(() => store.state.login.error = null, 3000);
        },
        setEvents(state, events) {
            state.allEvents = events
        }
    },
    namespaced: true
}