<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <EventInformationComponent v-if="!isLoading" :event="this.event_info"/>
    <CommentsSystemComponent v-if="!isLoadingEventComments" :event_comments="this.event_comments"/>
</template>

<script>

import EventInformationComponent from "@/containers/events/EventInformationComponent.vue";
import {mapMutations, mapState} from "vuex";
import {getEvent, getEventComments} from "../../../services/api";
import CommentsSystemComponent from "@/containers/events/CommentsSystemComponent.vue";

export default {
    name: "DetailEventsView",
    components: {CommentsSystemComponent, EventInformationComponent},
    data() {
        return {
            event_info: '',
            event_comments: [],
            isLoading: true,
            isLoadingEventComments: true,
        }
    },
    computed: {
        ...mapState({
            error: state => state.login.error,
            // isLoading: state => state.login.isLoading,
        }),
    },
    methods: {
        ...mapMutations({
            setLoading: 'login/setLoading'
        }),
        // TODO почему не работает с глобальным loading
        async loadEvent(event_id) {
            this.isLoading = true
            this.event_info = await getEvent(event_id);
            this.isLoading = false
        },
        async loadEventComments(event_id) {
            this.isLoadingEventComments = true
            this.event_comments = await getEventComments(event_id)
            this.isLoadingEventComments = false
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