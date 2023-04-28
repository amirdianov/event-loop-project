<template>
    <h1>{{this.event}}</h1>
<!--    <div v-for="(event, index) in userEvents" :key="index">-->
<!--        <div v-if="event.id==this.$route.params.id" class="event">-->
<!--            {{ event.title }}-->
<!--        </div>-->
<!--    </div>-->
</template>

<script>
import {mapState} from "vuex";
import {getUserEvent} from "../../services/api";

export default {
    name: "EventInformationComponent",
    data(){
        return{
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
    methods: {
        async loadUserEvent(event_id) {
            this.isLoading = true;
            this.event = await getUserEvent(event_id);
            this.isLoading = false;
        }
    },
    created() {
        this.loadUserEvent(this.$route.params.id)
        // this.userEvents.forEach((event) => {
        //     if (event.id == this.$route.params.id) {
        //         this.event = event
        //     }
        // })
        // if (this.event == null) {
        //     store.state.login.error = 'Ошибка'
        //     this.$router.push({name: 'my-events'})
        // }
    }
}
</script>

<style scoped>

</style>