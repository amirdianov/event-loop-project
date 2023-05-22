<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <EventInformationComponent v-if="!this.isLoadingNow" :event="this.event_info"/>
    <CommentsSystemComponent v-if="!this.isLoadingNow" :event_comments="this.event_comments"/>
</template>

<script>

import EventInformationComponent from "@/containers/events/EventInformationComponent.vue";
import {mapState} from "vuex";
import {getEvent, getEventComments} from "../../../services/api";
import CommentsSystemComponent from "@/containers/events/CommentsSystemComponent.vue";
import store from "@/store";

export default {
    name: "DetailEventsView",
    components: {CommentsSystemComponent, EventInformationComponent},
    data() {
        return {
            event_info: '',
            event_comments: [],
            isLoadingNow: true,
        }
    },
    computed: {
        ...mapState({
            error: state => state.login.error,
        }),
    },
    methods: {
        // TODO почему не работает с глобальным loading
        async loadEvent(event_id) {
            store.state.login.isLoading = true
            console.log(this.isLoading, store.state.login.isLoading)
            this.event_info = await getEvent(event_id);
            console.log(this.event_info)
            // store.state.login.isLoading = false
        },
        async loadEventComments(event_id) {
            // store.state.login.isLoading = true
            this.event_comments = await getEventComments(event_id)
            store.state.login.isLoading = false
            this.isLoadingNow = false
        }
    },
    created() {
        const event_id = this.$route.params.id;
        this.loadEvent(event_id)
        this.loadEventComments(event_id)
    }
}
</script>

<style scoped>

</style>