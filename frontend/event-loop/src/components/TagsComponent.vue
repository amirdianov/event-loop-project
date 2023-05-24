<template>
    <div>
        <a-select v-if="!isLoading"
                  v-model:value="val"
                  mode="tags"
                  style="width: 100%"
                  placeholder="Tags Mode"
                  :options="options"
                  @change="handleChange"
        ></a-select>
    </div>

</template>
<script>
import {defineComponent} from 'vue';
import {getTags} from "../../services/api/tag";

export default defineComponent({
    data() {
        return {
            isLoading: false,
            val: this.value
        }
    },
    props: {
        modelValue: Array,
        value: Array,
    },
    emits: ["update:modelValue"],

    methods: {
        handleChange(value) {
            this.$emit("update:modelValue", value);
        },
        async load() {
            this.isLoading = true;
            this.result = await getTags();
            this.isLoading = false;
        }
    },
    created() {
        this.load();
    },
    computed: {
        options() {
            return [
                ...this.result.map(x => ({value: x.title, label: x.title}))
            ]
        }
    }
});
</script>