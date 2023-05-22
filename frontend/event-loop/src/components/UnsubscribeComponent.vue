<template>
    <slot :unsubscribe="unsubscribeEvent"></slot>
</template>

<script>
import {unsubscribe} from "../../services/api";

export default {
    name: "UnsubscribeComponent",
    methods: {
        async unsubscribeEvent() {
            await unsubscribe({event: this.event, unsubscribe: true})
        }
    },
    props: {
        event: {},
    }
}
</script>

<style scoped>

</style>