<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <EventInformationComponent v-if="!isLoading" :event="this.event"/>
</template>

<script>

import EventInformationComponent from "@/components/EventInformationComponent.vue";
import {mapMutations, mapState} from "vuex";
import {getEvent} from "../../../services/api";

export default {
    name: "DetailEventsView",
    components: {EventInformationComponent},

    computed: {
        ...mapState({
            error: state => state.login.error,
            isLoading: state => state.login.isLoading,
        }),
    },
    methods: {
        ...mapMutations({
            setLoading: 'login/setLoading'
        }),
        async loadUserEvent(event_id) {
            this.setLoading(true)
            this.event = await getEvent(event_id);
            this.setLoading(false)
        }
    },
    created() {
        this.loadUserEvent(this.$route.params.id)
    }
}
</script>

<style scoped>

</style>