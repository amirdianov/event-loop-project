<template>
    <a-form ref="form"
            :model="formState"
            v-bind="layout"
            name="nest-messages"
            :validate-messages="validateMessages"
            @finish="submit"
            :wrapper-col="{span: 20}"
            :label-col="{span: 4}"
            :rules="rules"
    >
        <a-form-item :name="['event', 'title']" label="Заголовок" :rules="[{ required: true}]">
            <a-input v-model:value="formState.event.title"/>
        </a-form-item>
        <a-form-item :name="['event', 'category']" label="Категория" :rules="[{ required: true}]">
            <a-select
                    ref="select"
                    v-model:value="formState.event.category"
                    :options="options1"
            ></a-select>
        </a-form-item>
        <a-form-item :name="['event', 'description']" label="Описание" :rules="[{ required: true}]">
            <a-textarea v-model:value="formState.event.description"/>
        </a-form-item>
        <a-form-item :name="['event', 'tags']" label="Теги">
            <div>
                <tags-component @update:model-value="formState.event.tags = $event"
                                v-model:value="formState.event.tags"></tags-component>
            </div>
        </a-form-item>
        <a-form-item :name="['event', 'price']" label="Цена">
            <a-input-number v-model:value="formState.event.price" style="width: 100%"></a-input-number>
        </a-form-item>
        <a-form-item :name="['event', 'url']" label="Ссылка">
            <a-input v-model:value="formState.event.url" style="width: 100%"></a-input>
        </a-form-item>
        <a-form-item :name="['event', 'start_time']" label="Начало мероприятия"
        >
            <time-component @update:model-value="formState.event.start_time = $event"
            ></time-component>
        </a-form-item>
        <a-form-item :name="['event', 'finish_time']" label="Конец мероприятия">
            <time-component @update:model-value="formState.event.finish_time = $event"></time-component>
        </a-form-item>
        <!--        TODO antdv upload file-->
        <a-form-item :name="['event', 'photo']" label="Фото" style="margin-bottom: 20px">
            <input type="file" ref="file" @change="handleFileChange">
        </a-form-item>
        <a-form-item :wrapper-col="{ ...layout.wrapperCol, offset: 4}" style="margin-bottom: 0">
            <a-button type="primary" html-type="submit">Подтвердить</a-button>
        </a-form-item>
    </a-form>
</template>
<script>
import {defineComponent, reactive, ref} from 'vue';
import TimeComponent from "@/components/TimeComponent.vue";
import {mapActions} from "vuex";
import TagsComponent from "@/components/TagsComponent.vue";
import store from "@/store";

export default defineComponent({
    name: 'CreateEditEventInformationComponent',
    components: {TagsComponent, TimeComponent},
    setup() {
        const file = ref(null)
        const layout = {
            labelCol: {
                span: 8,
            },
            wrapperCol: {
                span: 16,
            },
        };
        const validateMessages = {
            required: 'Поле должно быть заполнено!',
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
            event: store.state.events.userEvent ? store.state.events.userEvent : {
                title: '',
                description: undefined,
                start_time: '',
                finish_time: '',
                photo: '',
                category: '',
                tags: undefined,
                price: null,
                url: null,
            },
        });
        let validateStart = async (_rule, value) => {
            if (value === '') {
                return Promise.reject('Поле должно быть заполнено!');
            } else if (value >= formState.event.finish_time && formState.event.finish_time !== '') {
                return Promise.reject('Введите предыдущую дату');
            } else {
                return Promise.resolve();
            }
        };
        let validateFinish = async (_rule, value) => {
            if (value === '') {
                return Promise.reject('Поле должно быть заполнено!');
            } else if (value <= formState.event.start_time) {
                return Promise.reject('Введите последующую дату');
            } else {
                return Promise.resolve();
            }
        };
        // let validatePhoto = async (_rule, value) => {
        //     console.log(file.value.files[0])
        //     if (file.value.files[0] !== undefined) {
        //         formState.event.photo = file.value.files[0];
        //         rules.event.photo = [{required: false, trigger: 'change', validator: validatePhoto}];
        //         return Promise.resolve()
        //     } else {
        //         formState.event.photo = '';
        //         rules.event.photo = [{required: true, trigger: 'change', validator: validatePhoto}];
        //         return Promise.reject('Поле должно быть заполнено!');
        //     }
        // }

        const rules = {
            event: {
                start_time: [
                    {
                        required: true,
                        validator: validateStart,
                        trigger: 'change',
                    },
                ],
                finish_time: [
                    {
                        required: true,
                        validator: validateFinish,
                        trigger: 'change',
                    },
                ],
                photo: [
                    {
                        required: true,
                        // validator: validatePhoto,
                        trigger: 'change',
                    }
                ]
            },
        };
        return {
            formState,
            layout,
            validateMessages,
            options1,
            rules,
            file,
            // validatePhoto
        };
    },
    methods: {
        ...mapActions({
            createUsersEvent: 'events/createUsersEvent',
            updateUserEvent: 'events/updateUsersEvent'
        }),
        handleFileChange() {
            console.log('change')
            if (this.$refs.file.files.length > 0) {
                console.log('второй')
                this.formState.event.photo = this.$refs.file.files[0];
                this.rules.event.photo = [];
            } else {
                console.log('третий')
                this.formState.event.photo = '';
                this.rules.event.photo = [{required: false, trigger: 'change', validator: this.validatePhoto}];

            }
        },
        async submit(data) {
            const formData = new FormData();
            let keys = Object.keys(data['event'])
            keys.forEach((key) => {
                console.log(key, data['event'][key])
                if (key === 'tags') {
                    if (data['event'][key] !== undefined) {
                        const ans = JSON.parse(JSON.stringify(data['event'][key]))
                        console.log(ans)
                        for (let i in ans) {
                            formData.append('tags', ans[i])
                        }
                    }
                } else if (key === 'photo') {
                    {
                        if (this.$refs.file.files[0]) {
                            formData.append('photo', this.$refs.file.files[0]);
                        }
                    }
                } else {
                    if (key !== null) {
                        formData.append(key, data['event'][key])
                        console.log(formData.get(key))
                    }
                }
            })
            if (this.$refs.file.files[0]) {
                formData.append('photo', this.$refs.file.files[0]);
            }
            try {
                if (this.$route.params.id) {
                    try {
                        await this.updateUserEvent({data: formData, id: this.$route.params.id})
                    } catch (e) {
                        console.log(e)
                    }
                } else {
                    try {
                        await this.createUsersEvent(formData)
                    } catch (e) {
                        console.log(e)
                    }
                }
                this.$router.push({name: 'my-events'})

            } catch (e) {
                console.log(e)
            }
        },
    },
    watch: {
        $route() {
            if (!this.$route.params.id) {
                store.state.events.userEvent = null
            }
        },

    },
})
;
</script>