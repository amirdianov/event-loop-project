<template>
    <div v-if="!isLoading">
        <div v-for="(event, index) in this.allEvents" :key="index" style="display: inline-block; padding: 10px">
            <div>
                <CardComponent :event="event" name="event-page" :slug="slug">
                </CardComponent>
            </div>
        </div>
    </div>
</template>

<script>
import {mapActions, mapState} from "vuex";
import CardComponent from "@/components/CardComponent.vue";

export default {
    name: "EventsView",
    components: {CardComponent},
    data() {
        return {
            items: 10,
            slug: this.$route.params.slug
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
        this.loadEvents(this.$route.params.slug)
    },
    watch: {
        $route(to) {
            console.log(this.$route.params.slug)
            this.loadEvents(this.$route.params.slug)
            // const params = {...to.query, "page": this.parameters.page};
            // this.loadEvents(`?${qs.stringify(params, {indices: false})}`);
        }
    }
}
</script>

<style scoped>

</style>