<template>
    <a-form
            :model="formState"
            v-bind="layout"
            name="nest-messages"
            :validate-messages="validateMessages"
            @finish="sub"
    >
        <a-form-item :name="['event', 'title']" label="Title" :rules="[{ required: true }]">
            <a-input v-model:value="formState.event.title"/>
        </a-form-item>
        <a-form-item :name="['event', 'description']" label="Description" :rules="[{ required: true }]">
            <a-input v-model:value="formState.event.description"/>
        </a-form-item>
        <a-form-item :name="['event', 'start_time']" label="Start Time">
            <time-component @update:model-value="formState.event.start_time = $event"></time-component>
        </a-form-item>
        <a-form-item :name="['event', 'finish_time']" label="Finish Time">
            <time-component @update:model-value="formState.event.finish_time = $event"></time-component>
        </a-form-item>
        <a-form-item :name="['event', 'category']" label="Category">
            <a-textarea v-model:value="formState.event.category"/>
        </a-form-item>
<!--        TODO antdv upload file-->
        <a-form-item :name="['event', 'photo']" label="Photo">
<!--                        <upload-component v-model:value="formState.event.photo"></upload-component>-->
            <input type="file" ref="file">

        </a-form-item>
        <a-form-item :wrapper-col="{ ...layout.wrapperCol, offset: 8 }">
            <a-button type="primary" html-type="submit">Submit</a-button>
        </a-form-item>
    </a-form>
</template>
<script>
import {defineComponent, reactive} from 'vue';
import UploadComponent from "@/components/UploadComponent.vue";
import TimeComponent from "@/components/TimeComponent.vue";
import {mapActions} from "vuex";

export default defineComponent({
    components: {TimeComponent, UploadComponent},
    data() {
        return{
            val: ''
        }
    },
    setup() {
        const layout = {
            labelCol: {
                span: 8,
            },
            wrapperCol: {
                span: 16,
            },
        };
        const validateMessages = {
            required: '${label} is required!',
            types: {
                email: '${label} is not a valid email!',
                number: '${label} is not a valid number!',
            },
            number: {
                range: '${label} must be between ${min} and ${max}',
            },
        };
        const formState = reactive({
            event: {
                title: '',
                description: undefined,
                start_time: '',
                finish_time: '',
                category: '',
                photo: ''
            },
        });
        const onFinish = values => {
            console.log(values)
        };
        return {
            formState,
            onFinish,
            layout,
            validateMessages,
        };
    },
    methods: {
        ...mapActions({createUsersEvent: 'events/createUsersEvent'}),
        async sub(data) {
            const formData = new FormData();
            let keys = Object.keys(data['event'])
            keys.forEach((key) => {
                console.log(key, data['event'][key])
                formData.append(key, data['event'][key])
                console.log(formData.get(key))
            })
            formData.append('photo', this.$refs.file.files[0]);
            try {
                await this.createUsersEvent(formData)
            } catch (e) {
                console.log(e)
            }
        }

    },
});
</script>