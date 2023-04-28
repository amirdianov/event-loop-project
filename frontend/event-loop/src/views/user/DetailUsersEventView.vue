<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <EventInformationComponent v-if="!isLoading"/>
</template>

<script>
import {mapState} from "vuex";
import EventInformationComponent from "@/components/EventInformationComponent.vue";

export default {
    name: "DetailUsersEventView",
    components: {EventInformationComponent},

    computed: {
        ...mapState({
            error: state => state.login.error,
            isLoading: state => state.login.isLoading,
        }),
    },

}
</script>

<style scoped>

</style>