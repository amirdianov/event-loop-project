<template>
    <div>
        <div v-for="(event, index) in userEvents" :key="index" style="display: inline-block; padding: 10px">
            <div>
                <CardComponent :title="event.title" :description="event.description" :photo="event.photo"
                               @click="this.$router.push({name: 'my-event-page', params: {id: event.id}})">
                </CardComponent>
                <router-link :to="{name: 'my-event-page', params: {id: event.id}}"></router-link>

            </div>
        </div>
    </div>
</template>

<script>
import LayoutNav from "@/containers/LayoutNav.vue";
import {mapActions, mapState} from "vuex";
import CardComponent from "@/components/CardComponent.vue";

export default {
    name: "UsersEventsView",
    components: {CardComponent, LayoutNav},
    data() {
        return {
            items: 10
        }
    },
    computed: {
        ...mapState({
            isLoading: state => state.login.isLoading,
            userEvents: state => state.events.userEvents
        })
    },
    methods: {
        ...mapActions({loadEvents: "events/loadUsersEvents"})
    },
    created() {
        this.loadEvents()
    }
}
</script>

<style scoped>

</style>