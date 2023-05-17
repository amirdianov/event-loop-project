<template>
    <h1>{{ this.text }}</h1>
</template>

<script>
import {getPayResponse, subscribe} from "../../../services/api";

export default {
    name: "PayResponseView",
    data() {
        return {
            text: ''
        }
    },
    methods: {
        async getResponse() {
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
            } catch (error) {
                console.error(error);
            }
        }
    },
    mounted() {
        this.getResponse();
    }
}
</script>

<style scoped>

</style>