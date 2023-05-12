<template>
    <div v-if="!isLoading">
        <div v-for="(event, index) in this.allEvents" :key="index" style="display: inline-block; padding: 10px">
            <CardComponent :event_info="event" name="event-page" :slug="slug">
            </CardComponent>
        </div>
    </div>
</template>

<script>
import {mapActions, mapState} from "vuex";
import CardComponent from "@/containers/events/CardComponent.vue";

export default {
    name: "EventsView",
    components: {CardComponent},
    data() {
        return {
            items: 10,
            slug: null
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
        this.slug = this.$route.params.slug
        this.loadEvents(this.slug)
    },
    watch: {
        $route(to) {
            this.slug = this.$route.params.slug
            if (this.slug) {
                this.loadEvents(this.slug)
                console.log('Я тут')
            }
        }
    }
}
</script>

<style scoped>

</style>