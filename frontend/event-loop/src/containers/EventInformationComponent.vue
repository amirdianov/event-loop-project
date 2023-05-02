<template>
    <h1>{{ event.title }}</h1>
    <div v-if="showRating">
        <a-rate v-model:value="value"/>
    </div>
</template>

<script>
import {mapState} from "vuex";

export default {
    name: "EventInformationComponent",
    data() {
        return {
            showRating: true,
            value: 0,
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
    created() {
        this.event.rating_event.forEach((element) => {
            if (element.user_id === this.user.id) {
                this.showRating = false
            }
        })
    },
    props: {
        event: {}
    }

}
</script>

<style scoped>

</style>