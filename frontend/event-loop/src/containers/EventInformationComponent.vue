<template>
    <h1>{{ event.title }}</h1>
    <div><img :src="event.photo" alt="Фотография" width="400" height="400"></div>
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
        const organizators = []
        this.event.organizer.forEach((element) => {
            if (element.user === this.user.id) {
                organizators.push(element.user)
            }
        })
        if (!organizators.includes(this.user.id)) {
            this.event.rating_event.forEach((element) => {
                if (element.user === this.user.id) {
                    this.showRating = false
                }
            })
        } else {
            this.showRating = false
        }

    },
    props: {
        event: {}
    }

}
</script>

<style scoped>

</style>