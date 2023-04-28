import store from "@/store/index";
import {all_events, create_event, user_events} from "../../services/api";

export const eventsModule = {
    state: () => ({
        allEvents: null,
        userEvents: null
    }),
    actions: {
        async loadAllEvents({commit}, data) {
            store.state.login.isLoading = true
            try {
                console.log(data)
                const events = await all_events(data)
                commit("setAllEvents", events)
            } catch (e) {
                store.state.login.isLoading = false
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
                store.state.login.isLoading = false

                commit("setError", 'Ошибка')
            }
            store.state.login.isLoading = false

        },
        async createUsersEvent({commit}, data) {
            try {
                await create_event(data)
            } catch (e) {
                commit("setError", 'Ошибка')
            }
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