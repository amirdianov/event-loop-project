<template>
    <a-row type="flex" justify="center" align="middle" style="min-height: 550px">
        <a-col :span="10">
            <a-form
                    :label-col="{ span: 6 }"
                    :wrapper-col="{ span: 15 }"
                    ref="formRef"
                    name="custom-validation"
                    :model="formState"
                    :rules="rules"
                    @finish="submit"
            >
                <a-form-item has-feedback label="Пароль" name="pass">
                    <a-input v-model:value="formState.pass" type="password" autocomplete="off">
                        <template #prefix>
                            <LockOutlined class="site-form-item-icon"/>
                        </template>
                    </a-input>
                </a-form-item>
                <a-form-item has-feedback label="Повторный пароль" name="checkPass">
                    <a-input v-model:value="formState.checkPass" type="password" autocomplete="off">
                        <template #prefix>
                            <LockOutlined class="site-form-item-icon"/>
                        </template>
                    </a-input>
                </a-form-item>
                <a-form-item :wrapper-col="{ offset: 6, span: 15 }">
                    <a-button type="primary" html-type="submit" style="width: 100%">Изменить пароль</a-button>
                </a-form-item>
            </a-form>
        </a-col>
    </a-row>
</template>


<script>
import {defineComponent, reactive, ref} from 'vue';
import {mapState} from "vuex";
import {LockOutlined, MailOutlined} from "@ant-design/icons-vue";

export default defineComponent({
    name: "ResetPasswordView",
    components: {LockOutlined, MailOutlined},
    setup() {
        const formRef = ref();
        const formState = reactive({
            pass: '',
            checkPass: '',
            age: undefined,
        });
        let validatePass = async (_rule, value) => {
            if (value === '') {
                return Promise.reject('Введите пароль');
            } else if (value.length < 5) {
                return Promise.reject('Пароль должен быть содержать не менее 5 символов');
            } else {
                if (formState.checkPass !== '') {
                    formRef.value.validateFields('checkPass');
                }
                return Promise.resolve();
            }
        };
        let validatePass2 = async (_rule, value) => {
            if (value === '') {
                return Promise.reject('Повторите пароль');
            } else if (value.length < 5) {
                return Promise.reject('Пароль должен быть содержать не менее 5 символов');
            } else if (value !== formState.pass) {
                return Promise.reject("Пароли не совпадают");
            } else {
                return Promise.resolve();
            }
        };
        const rules = {
            pass: [{
                required: true,
                min: 10,
                validator: validatePass,
                trigger: 'change',
            }],
            checkPass: [{
                required: true,
                min: 10,
                validator: validatePass2,
                trigger: 'change',
            }],
        };
        return {
            formState,
            formRef,
            rules,
        };
    },
    computed: {
        ...mapState({
            error: state => state.login.error
        })
    },
    methods: {
        submit(data) {
            console.log(data)
        }
    }

})
</script>

<style scoped>

</style>