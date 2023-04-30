<template>
    <a-space direction="vertical" :size="12">
        <a-date-picker v-model:value="val"
                       show-time placeholder="Select Time" @change="changeTime" @ok="onOk"/>
    </a-space>
</template>
<script>
import {defineComponent} from 'vue';

export default defineComponent({
    data(){
        return{
            val: this.value
        }
    },
    props: {
        modelValue: String,
        value: {}
    },
    emits: ["update:modelValue"],
    methods: {
        changeTime(value, dateString) {
            console.log(value)
            console.log(dateString)
            this.$emit("update:modelValue", dateString);
        },
        onOk(value) {
            console.log('onOk: ', value);
        },
    }
})
</script>