<template>
    <MessageComponent v-if="this.error" typeMessage="error" messageText="Ошибка" :messageDescription="this.error"/>
    <a-row type="flex" justify="center" align="middle" style="min-height: 550px">
        <a-col :span="10">
            <a-form v-if="!sendMail"
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

                <a-form-item :wrapper-col="{ offset: 5, span: 16 }">
                    <a-button type="primary" html-type="submit" style="margin-right: 10px; width: 100%">Сбросить
                        пароль
                    </a-button>
                    <router-link to="/login">Вход</router-link>
                </a-form-item>
            </a-form>
            <div v-else style="display: flex; justify-content: center; border: 1px #002a29 solid; border-radius: 10px">
                Письмо отправлено на вашу почту!
            </div>
        </a-col>
    </a-row>
</template>

<script>
import {LockOutlined, MailOutlined} from "@ant-design/icons-vue";
import {defineComponent, reactive} from "vue";
import {mapState} from "vuex";
import {forgotPassword} from "../../../services/api/user";
import store from "@/store";
import MessageComponent from "@/components/MessageComponent.vue";

export default defineComponent({
    name: "ForgotPasswordView",
    components: {MessageComponent, LockOutlined, MailOutlined},
    data() {
        return {
            sendMail: false,
        }
    },
    setup() {
        const formState = reactive({
            email: '',
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
        async submit(data) {
            try {
                await forgotPassword(data)
                this.sendMail = true
                setTimeout(() => {
                    this.$router.push({name: 'login'})
                }, 3000)
            } catch (e) {
                store.state.login.error = e.message
                setTimeout(() => {
                    store.state.login.error = false
                }, 3000)
            }
        }

    }
});
</script>

<style scoped>

</style>