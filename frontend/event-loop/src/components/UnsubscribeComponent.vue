<template>
    <slot :unsubscribe="unsubscribeEvent"></slot>
</template>

<script>
import {unsubscribe} from "../../services/api";

export default {
    name: "UnsubscribeComponent",
    data() {
        return {
            eventsInfoNew: []
        }
    },
    methods: {
        async unsubscribeEvent() {
            await unsubscribe({event: this.event, unsubscribe: true})
            console.log(this.eventsInfo)
            this.eventsInfo.forEach((object) => {
                if (object.event.id !== this.event.id) {
                    this.eventsInfoNew.push(object)
                }
            })
            this.$emit('update:eventsInfo', this.eventsInfoNew) // раньше было `this.$emit('input', title)`
        }
    },
    props: {
        event: {},
        eventsInfo: {}
    },
    emits: ['update:eventsInfo'],
    created() {
        console.log(this.event, this.eventsInfo)
    }
}
</script>

<style scoped>

</style>