<template>
    <a-form
            :model="formState"
            v-bind="layout"
            name="nest-messages"
            :validate-messages="validateMessages"
            @finish="submit"
            :wrapper-col="{span: 21}"
            :label-col="{span: 3}"
    >
        <a-form-item :name="['event', 'title']" label="Title">
            <a-input v-model:value="formState.event.title"/>
        </a-form-item>
        <a-form-item :name="['event', 'category']" label="Category">
            <a-select
                    ref="select"
                    v-model:value="formState.event.category"
                    :options="options1"
            ></a-select>
        </a-form-item>
        <a-form-item :name="['event', 'description']" label="Description">
            <a-textarea v-model:value="formState.event.description"/>
        </a-form-item>
        <a-form-item :name="['event', 'tags']" label="Tags">
            <div>
                <tags-component @update:model-value="formState.event.tags = $event"></tags-component>
            </div>
        </a-form-item>
        <a-form-item :name="['event', 'start_time']" label="Start Time">
            <time-component @update:model-value="formState.event.start_time = $event"></time-component>
        </a-form-item>
        <a-form-item :name="['event', 'finish_time']" label="Finish Time">
            <time-component @update:model-value="formState.event.finish_time = $event"></time-component>
        </a-form-item>
        <!--        TODO antdv upload file-->
        <a-form-item :name="['event', 'photo']" label="Photo">
            <!--                        <upload-component v-model:value="formState.event.photo"></upload-component>-->
            <input type="file" ref="file">
        </a-form-item>
        <a-form-item :wrapper-col="{ ...layout.wrapperCol, offset: 3}">
            <a-button type="primary" html-type="submit">Submit</a-button>
        </a-form-item>
    </a-form>
</template>
<script>
import {defineComponent, reactive, ref} from 'vue';
import UploadComponent from "@/components/UploadComponent.vue";
import TimeComponent from "@/components/TimeComponent.vue";
import {mapActions} from "vuex";
import TagsComponent from "@/components/TagsComponent.vue";

export default defineComponent({
    name: 'CreateEditEventInformationComponent',
    components: {TagsComponent, TimeComponent, UploadComponent},
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
        const options1 = ref([{
            value: 'lesson',
            label: 'Урок',
        }, {
            value: 'webinar',
            label: 'Вебинар',
        }, {
            value: 'masterclass',
            label: 'Мастер-класс',
        }, {
            value: 'entertainments',
            label: 'Развлечения',
        }]);
        const formState = reactive({
            event: {
                title: '',
                description: undefined,
                start_time: '',
                finish_time: '',
                photo: '',
                category: '',
                tags: '',
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
            options1
        };
    },
    methods: {
        ...mapActions({createUsersEvent: 'events/createUsersEvent'}),
        async submit(data) {
            const formData = new FormData();
            let keys = Object.keys(data['event'])
            keys.forEach((key) => {
                console.log(key, data['event'][key], 'DDDDDD')
                if (key === 'tags') {
                    const ans = JSON.parse(JSON.stringify(data['event'][key]))
                    console.log(ans)
                    for (let i in ans) {
                        formData.append('tags', ans[i])
                    }
                } else {
                    formData.append(key, data['event'][key])
                    console.log(formData.get(key))
                }
            })
            formData.append('photo', this.$refs.file.files[0]);
            try {
                await this.createUsersEvent(formData)
                this.$router.push({name: 'my-events'})

            } catch (e) {
                console.log(e)
            }
        },
    }
});
</script>