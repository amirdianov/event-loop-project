<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <EventInformationComponent v-if="!isLoading" :event="this.event_info"/>
</template>

<script>

import EventInformationComponent from "@/containers/EventInformationComponent.vue";
import {mapMutations, mapState} from "vuex";
import {getEvent} from "../../../services/api";

export default {
    name: "DetailEventsView",
    components: {EventInformationComponent},
    data() {
        return {
            event_info: '',
            isLoading: true
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
        }
    },
    created() {
        this.loadEvent(this.$route.params.id)
    }
}
</script>

<style scoped>

</style>