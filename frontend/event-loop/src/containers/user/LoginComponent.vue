<template>
    <a-form
            :model="formState"
            name="basic"
            :label-col="{ span: 5 }"
            :wrapper-col="{ span: 16 }"
            :validate-messages="validateMessages"
            autocomplete="off"
            @finish="submit"
            @finishFailed="onFinishFailed"
    >
        <a-form-item
                label="Почта"
                name="email"
                :rules="[{ required: true, type: 'email'}]"
        >
            <a-input v-model:value="formState.email">
                <template #prefix>
                    <MailOutlined class="site-form-item-icon"/>
                </template>
            </a-input>
        </a-form-item>

        <a-form-item
                label="Пароль"
                name="password"
                :rules="[{ required: true}]"
        >
            <a-input-password v-model:value="formState.password">
                <template #prefix>
                    <LockOutlined class="site-form-item-icon"/>
                </template>
            </a-input-password>
        </a-form-item>

        <a-form-item name="remember" :wrapper-col="{ offset: 5, span: 16 }">
            <a-checkbox v-model:checked="formState.remember">Remember me</a-checkbox>
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 5, span: 16 }">
            <a-button type="primary" html-type="submit" style="margin-right: 10px; width: 100%">Войти</a-button>
            <router-link to="/registration">Регистрация</router-link>
        </a-form-item>
    </a-form>
</template>
<script>
import {defineComponent, reactive} from 'vue';
import {mapActions, mapMutations, mapState} from "vuex";
import {LockOutlined, MailOutlined} from "@ant-design/icons-vue";

export default defineComponent({
    name: "LoginComponent",
    components: {LockOutlined, MailOutlined},
    setup() {
        const formState = reactive({
            email: '',
            password: '',
            remember: true,
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
    methods: {
        ...mapMutations({
            setUser: 'login/setUser'
        }),
        ...mapActions({loginUser: 'login/loginUser',}),
        async submit(data) {
            console.log(data)
            try {
                await this.loginUser(data)
                this.$router.push({name: 'profile'})
            } catch (e) {
                console.log(e)
            }
        }

    },
});
</script>