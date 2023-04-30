<template>
    <a-form v-if="changePassword"
            :model="formState"
            name="basic"
            :label-col="{ span: 5 }"
            :wrapper-col="{ span: 16 }"
            :validate-messages="validateMessages"
            autocomplete="off"
            @finish="changeInformation"
            @finishFailed="onFinishFailed"
    >
        <a-form-item
                label="Имя"
                name="name"
                :rules="[{ required: true}]"
        >
            <a-input v-model:value="formState.name">
                <template #prefix>
                    <UserOutlined class="site-form-item-icon"/>
                </template>
            </a-input>
        </a-form-item>
        <a-form-item
                label="Фамилия"
                name="surname"
                :rules="[{ required: true}]"
        >
            <a-input v-model:value="formState.surname">
                <template #prefix>
                    <TeamOutlined class="site-form-item-icon"/>
                </template>
            </a-input>
        </a-form-item>
        <a-form-item
                label="Почта"
                name="email"
                :rules="[{ required: true, type: 'email'}]"
        >
            <a-input v-model:value="formState.email">
                <template #prefix>
                    <MailOutlined class="site-form-item-icon"></MailOutlined>
                </template>
            </a-input>
        </a-form-item>
        <a-form-item :wrapper-col="{ offset: 5, span: 16 }">
            <a-button type="primary" html-type="submit" style="margin-right: 10px; width: 100%">Подвердить изменения
            </a-button>
            <p style="color: #1d39c4" @click="changePassword = !changePassword">Изменить пароль?</p>
        </a-form-item>
    </a-form>
    <a-form v-else
            :model="formState"
            name="basic"
            :label-col="{ span: 5 }"
            :wrapper-col="{ span: 16 }"
            :validate-messages="validateMessages"
            autocomplete="off"
            @finish="submit"
            @finishFailed="onFinishFailed">
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
        <a-form-item :wrapper-col="{ offset: 5, span: 16 }">
            <a-button type="primary" html-type="submit" style="margin-right: 10px; width: 100%">Подвердить изменения
            </a-button>
            <p style="color: #1d39c4" @click="changePassword = !changePassword">Изменить личные данные?</p>
        </a-form-item>
    </a-form>


</template>
<script>
import {defineComponent, reactive} from 'vue';
import {mapActions, mapState} from "vuex";
import {LockOutlined, MailOutlined, TeamOutlined, UserOutlined} from "@ant-design/icons-vue";
import store from "@/store";

export default defineComponent({
    name: "ProfileInformationComponent",
    components: {UserOutlined, LockOutlined, MailOutlined, TeamOutlined},
    setup() {
        const formState = reactive({
            name: store.state.login.user.name,
            surname: store.state.login.user.surname,
            email: store.state.login.user.email,
            password: '',
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
    data() {
        return {
            changePassword: true,
        }
    },
    computed: {
        ...mapState({
            user: state => state.login.user
        })
    },
    methods: {
        ...mapActions({changeUserInformation: 'profile/changeUserInformation', logout: 'login/logout'}),
        async changeInformation(data) {
            try {
                await this.changeUserInformation(data)
                this.$router.push({name: 'profile'})
            } catch (e) {
                console.log(e)
            }
        },
        logout_click() {
            this.logout()
            this.$router.push({name: "home"});
        }
    }
});
</script>
