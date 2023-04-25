<template>
    <div>
        <div v-for="(event, index) in allEvents" :key="index" style="display: inline-block; padding: 10px">
            <CardComponent :title="event.title" :description="event.description" :photo="event.photo"></CardComponent>
        </div>
    </div>
</template>

<script>
import LayoutNav from "@/containers/LayoutNav.vue";
import {mapActions, mapState} from "vuex";
import CardComponent from "@/components/CardComponent.vue";

export default {
    name: "EventsView",
    components: {CardComponent, LayoutNav},
    data() {
        return {
            items: 10
        }
    },
    computed: {
        ...mapState({
            isLoading: state => state.login.isLoading,
            allEvents: state => state.events.allEvents
        })
    },
    methods: {
        ...mapActions({loadEvents: "events/loadAllEvents"})
    },
    created() {
        this.loadEvents()
    }
}
</script>

<style scoped>

</style>