<template>
    <h1>{{ event.title }}</h1>
</template>

<script>
import {mapState} from "vuex";

export default {
    name: "EventInformationComponent",
    computed: {
        ...mapState({
            error: state => state.login.error,
            isSuccess: state => state.profile.isSuccess,
            isLoading: state => state.login.isLoading,
            userEvents: state => state.events.userEvents,
            user: state => state.login.user
        }),
    },
    props: {
        event: {}
    }

}
</script>

<style scoped>

</style>