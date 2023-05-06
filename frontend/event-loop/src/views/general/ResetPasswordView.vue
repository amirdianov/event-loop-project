<template>
    <a-row type="flex" justify="center" align="middle" style="min-height: 550px">
        <a-col :span="10">
            <a-form
                    :model="formState"
                    name="basic"
                    :label-col="{ span: 6 }"
                    :wrapper-col="{ span: 15 }"
                    :validate-messages="validateMessages"
                    autocomplete="off"
                    @finish="submit"
                    @finishFailed="onFinishFailed"
            >
                <a-form-item
                        label="Пароль"
                        name="password"
                        :rules="[{ required: true, type: 'password'}]"
                >
                    <a-input-password v-model:value="formState.password">
                        <template #prefix>
                            <LockOutlined class="site-form-item-icon"/>
                        </template>
                    </a-input-password>
                </a-form-item>

                <a-form-item
                        label="Повторный пароль"
                        name="password_confirm"
                        :rules="[{ required: true}]"
                >
                    <a-input-password v-model:value="formState.password_confirm">
                        <template #prefix>
                            <LockOutlined class="site-form-item-icon"/>
                        </template>
                    </a-input-password>
                </a-form-item>
                <a-form-item :wrapper-col="{ offset: 6, span: 15 }">
                    <a-button type="primary" html-type="submit" style="width: 100%">Изменить пароль</a-button>
                </a-form-item>
            </a-form>
        </a-col>
    </a-row>
</template>


<script>
import {defineComponent, reactive} from 'vue';
import {mapState} from "vuex";
import {LockOutlined, MailOutlined} from "@ant-design/icons-vue";

export default defineComponent({
    name: "ResetPasswordView",
    components: {LockOutlined, MailOutlined},
    setup() {
        const formState = reactive({
            password: '',
            password_confirm: '',
        });
        const onFinish = values => {
            console.log('Success:', values);
        };
        const onFinishFailed = errorInfo => {
            console.log('Failed:', errorInfo);
        };
        const validateMessages = {
            required: 'Поле должно быть заполнено!',
            types: {
                email: '${label} неверно введена!',
            },
        };
        return {
            formState,
            onFinish,
            onFinishFailed,
            validateMessages
        };
    },
    computed: {
        ...mapState({
            error: state => state.login.error
        })
    },

})
</script>

<style scoped>

</style>