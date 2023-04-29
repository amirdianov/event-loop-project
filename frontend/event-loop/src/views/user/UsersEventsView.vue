<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <a-row type="flex" justify="end">
        <a-col>
            <a-button @click="this.$router.push({name: 'my-events-create'})">
                Добавить мероприятие
            </a-button>
        </a-col>
    </a-row>
    <a-row type="flex" justify="start" style="height: 100%">
        <a-col v-if="!isLoading">
                <div v-for="(event, index) in userEvents" :key="index" style="display: inline-block; padding: 10px">
                    <CardComponent :event_info="event" name="my-event-page"/>
                </div>
        </a-col>
    </a-row>
</template>

<script>
import {mapActions, mapState} from "vuex";
import CardComponent from "@/containers/CardComponent.vue";

export default {
    name: "UsersEventsView",
    components: {CardComponent},
    computed: {
        ...mapState({
            isLoading: state => state.login.isLoading,
            userEvents: state => state.events.userEvents,
            error: state => state.login.error
        })
    },
    methods: {
        ...mapActions({loadUsersEvents: "events/loadUsersEvents"})
    },
    created() {
        this.loadUsersEvents()
    }

}
</script>

<style scoped>

</style>