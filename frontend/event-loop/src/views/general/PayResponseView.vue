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
            return await getPayResponse(this.$route.query.payment_id)
        }
    },
    async created() {
        const payStatus = await this.getResponse()
        console.log(payStatus)
        const status = payStatus.status_pay
        console.log(status)
        if (status === 'ok') {
            subscribe({'event': self.event_info});
            this.text = 'Успешно!'
        } else {
            this.text = 'Ошибка транзакции'
        }
    },
}
</script>

<style scoped>

</style>