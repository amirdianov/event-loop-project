<template>
    <LayoutNav v-if="!isLoading">
        <div>
            <div v-for="(item, index) in items" :key="index" style="display: inline-block; padding: 10px">
                <CardComponent></CardComponent>
            </div>
        </div>
    </LayoutNav>
</template>

<script>
import LayoutNav from "@/containers/LayoutNav.vue";
import {mapState} from "vuex";
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
            isLoading: state => state.login.isLoading
        })
    },
}
</script>

<style scoped>

</style>