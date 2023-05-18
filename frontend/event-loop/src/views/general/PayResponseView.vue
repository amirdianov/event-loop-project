<template>
    <a-row type="flex" justify="center" align="middle" style="min-height: 550px">
        <a-col>
            <LoadingOutlined v-if="isLoading" :style="{fontSize: '50px', color: '#4d2a16'}"/>
            <div v-if="!isLoading">
                <img v-if="text === 'Успешно!'" src="@/assets/images/top-up-credit-concept-illustration_114360-7244.png"
                     alt="Успешный платеж" width="500" height="500">
                <img v-else src="@/assets/images/business-people-saying-no-concept-illustration_114360-14201.png"
                     alt="Неуспешный платеж" width="500" height="500">
            </div>
        </a-col>
    </a-row>
</template>

<script>
import {getPayResponse, subscribe} from "../../../services/api";
import {LoadingOutlined} from "@ant-design/icons-vue";
import LoginComponent from "@/containers/user/LoginComponent.vue";

export default {
    name: "PayResponseView",
    components: {LoginComponent, LoadingOutlined},
    data() {
        return {
            text: '',
            isLoading: false
        }
    },
    methods: {
        async getResponse() {
            this.isLoading = true
            try {
                const payInfo = await getPayResponse(this.$route.query.payment_id);
                console.log(payInfo);
                const status = payInfo.status_pay;
                if (status === 'ok') {
                    await subscribe({event: payInfo.event});
                    this.text = 'Успешно!';
                } else {
                    this.text = 'Ошибка транзакции';
                }
                this.isLoading = false
            } catch (error) {
                this.isLoading = false
                console.error(error);
            }
        }
    },
    mounted() {
        this.getResponse();
        setTimeout(() => {
            // Выполнить перенаправление на главную страницу
            this.$router.push({name: 'calendar'});
        }, 5000); // 5000 миллисекунд = 5 секунд
    }
}
</script>

<style scoped>

</style>