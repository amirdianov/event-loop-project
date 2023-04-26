<template>
    <EventInformationComponent v-if="!isLoading">
    </EventInformationComponent>
</template>

<script>
import {mapState} from "vuex";
import EventInformationComponent from "@/components/EventInformationComponent.vue";

export default {
    name: "ProfileView",
    components: {EventInformationComponent},
    data() {
        return {
            event: null
        }
    },
    computed: {
        ...mapState({
            error: state => state.login.error,
            isSuccess: state => state.profile.isSuccess,
            isLoading: state => state.login.isLoading,
            userEvents: state => state.events.userEvents,
            user: state => state.login.user
        }),
    },

}
</script>

<style scoped>

</style>