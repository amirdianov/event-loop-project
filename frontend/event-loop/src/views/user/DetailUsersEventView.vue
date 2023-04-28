<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <div v-if="!isLoading">
        <EventInformationComponent :event="this.event"/>
    </div>
</template>

<script>
import {mapMutations, mapState} from "vuex";
import EventInformationComponent from "@/components/EventInformationComponent.vue";
import {getUserEvent} from "../../../services/api";

export default {
    name: "DetailUsersEventView",
    components: {EventInformationComponent},
    data() {
        return {
            event: null,
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
        async loadUserEvent(event_id) {
            // this.setLoading(true)
            this.isLoading = true
            this.event = await getUserEvent(event_id);
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