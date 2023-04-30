<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <div v-if="!isLoading">
        <EventInformationComponent :event="store.state.events.userEvent"/>
    </div>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";
import EventInformationComponent from "@/components/EventInformationComponent.vue";
import store from "@/store";

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
        store() {
            return store
        },
        ...mapState({
            error: state => state.login.error,
        }),
    },

    methods: {
        ...mapActions({'getUserEvent': 'events/getUserEvent'}),
        async loadUserEvent(event_id) {
            this.isLoading = true
            this.event = await this.getUserEvent(event_id);
            console.log(this.event)
            this.isLoading = false
        }
    },
    created() {
        this.loadUserEvent(this.$route.params.id)
    }
}
</script>

<style scoped>

</style>