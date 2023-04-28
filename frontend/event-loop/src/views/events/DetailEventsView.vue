<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <EventInformationComponent v-if="!isLoading" :event="this.event_info"/>
</template>

<script>

import EventInformationComponent from "@/components/EventInformationComponent.vue";
import {mapMutations, mapState} from "vuex";
import {getEvent} from "../../../services/api";

export default {
    name: "DetailEventsView",
    components: {EventInformationComponent},
    data(){
        return{
            isLoading: true
        }
    },
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
            // this.setLoading(true)
            this.isLoading = true
            this.event_info = await getEvent(event_id);
            this.isLoading = false
            // this.setLoading(false)
        }
    },
    created() {
        this.loadUserEvent(this.$route.params.id)
    }
}
</script>

<style scoped>

</style>