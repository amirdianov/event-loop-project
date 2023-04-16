<template>
    <a-form
            :model="formState"
            name="basic"
            :label-col="{ span: 5 }"
            :wrapper-col="{ span: 16 }"
            autocomplete="off"
            @finish="submit"
            @finishFailed="onFinishFailed"
    >
        <a-form-item
                label="Почта"
                name="username"
                :rules="[{ required: true, message: 'Please input your username!' }]"
        >
            <a-input v-model:value="formState.username"/>
        </a-form-item>

        <a-form-item
                label="Пароль"
                name="password"
                :rules="[{ required: true, message: 'Please input your password!' }]"
        >
            <a-input-password v-model:value="formState.password"/>
        </a-form-item>

        <a-form-item name="remember" :wrapper-col="{ offset: 5, span: 16 }">
            <a-checkbox v-model:checked="formState.remember">Remember me</a-checkbox>
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 5, span: 16 }">
            <a-button type="primary" html-type="submit" style="margin-right: 10px">Войти</a-button>
            <a-button type="primary" @click="$router.push('/registration')">Регистрация</a-button>

        </a-form-item>
    </a-form>
</template>
<script>
import {defineComponent, reactive} from 'vue';
import {mapActions, mapMutations, mapState} from "vuex";

export default defineComponent({
    name: "LoginComponent",
    setup() {
        const formState = reactive({
            username: '',
            password: '',
            remember: true,
        });
        const onFinish = values => {
            console.log('Success:', values);
        };
        const onFinishFailed = errorInfo => {
            console.log('Failed:', errorInfo);
        };
        return {
            formState,
            onFinish,
            onFinishFailed,
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