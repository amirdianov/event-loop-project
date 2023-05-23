<template>
    <MessageComponent v-if="this.isSuccess" typeMessage="success" messageText="Данные сохранены"/>
    <MessageComponent v-if="this.error" typeMessage="error" messageText="Ошибка" :messageDescription="this.error"/>
    <a-row type="flex" justify="center" style="margin-bottom: 5px">
        <a-col>
            <a-button @click="this.$router.push({name: 'my-events-create'})" type="primary">
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
import CardComponent from "@/containers/events/CardComponent.vue";
import MessageComponent from "@/components/MessageComponent.vue";

export default {
    name: "UsersEventsView",
    components: {MessageComponent, CardComponent},
    computed: {
        ...mapState({
            isLoading: state => state.login.isLoading,
            userEvents: state => state.events.userEvents,
            error: state => state.login.error,
            isSuccess: state => state.login.isSuccess,
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