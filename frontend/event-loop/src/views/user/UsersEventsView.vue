<template>
    <div v-if="!isLoading">
        <div v-for="(event, index) in userEvents" :key="index" style="display: inline-block; padding: 10px">
            <div>
                <CardComponent :event="event">
                </CardComponent>
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