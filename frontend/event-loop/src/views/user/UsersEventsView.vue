<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <a-row type="flex" justify="start" style="height: 100%">
        <a-col v-if="!isLoading">
                <div v-for="(event, index) in userEvents" :key="index" style="display: inline-block; padding: 10px">
                    <div class="cards">
                        <CardComponent :event="event" name="my-event-page"/>
                    </div>
                </div>
        </a-col>
    </a-row>
</template>

<script>
import {mapState} from "vuex";
import CardComponent from "@/components/CardComponent.vue";
import LoginComponent from "@/components/LoginComponent.vue";

export default {
    name: "UsersEventsView",
    components: {LoginComponent, CardComponent},
    computed: {
        ...mapState({
            isLoading: state => state.login.isLoading,
            userEvents: state => state.events.userEvents,
            error: state => state.login.error
        })
    },

}
</script>

<style scoped>

</style>