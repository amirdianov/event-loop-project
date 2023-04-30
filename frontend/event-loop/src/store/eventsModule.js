import store from "@/store/index";
import {all_events, create_event, update_event, user_event, user_events} from "../../services/api";

export const eventsModule = {
    state: () => ({
        allEvents: null,
        userEvents: null,
        userEvent: null,
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
        async getUserEvent({commit}, id) {
            try {
                const events = await user_event(id)
                commit("setUserEvent", events)
            } catch (e) {
                commit("setError", 'Ошибка')
            }
        },
        async createUsersEvent({commit}, data) {
            try {
                await create_event(data)
            } catch (e) {
                commit("setError", 'Ошибка')
            }
        },
        async updateUsersEvent({commit}, data) {
            try {
                await update_event(data)
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
        },
        setUserEvent(state, event) {
            state.userEvent = event
        }
    },
    namespaced: true
}