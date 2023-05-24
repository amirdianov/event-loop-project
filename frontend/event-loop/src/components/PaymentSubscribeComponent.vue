<template>
    <div v-if="!isLoading">
        <slot :showConfirmIcon="showConfirmIcon" :callShowConfirm="callShowConfirm"></slot>
    </div>
    <div v-if="isLoading">
        <LoadingOutlined></LoadingOutlined>
    </div>
</template>

<script>
import {createVNode, defineComponent} from 'vue';
import {
    CarryOutOutlined,
    CheckCircleOutlined,
    CheckOutlined,
    LoadingOutlined,
    PayCircleOutlined
} from "@ant-design/icons-vue";
import {Modal} from 'ant-design-vue';
import {getPKForPay, payEvent, subscribers} from "../../services/api/subscribtion";
import {mapState} from "vuex";
import {loadStripe} from "@stripe/stripe-js";

export default defineComponent({
    name: "PaymentSubscribeComponent",
    components: {LoadingOutlined, CarryOutOutlined, CheckOutlined, PayCircleOutlined},
    data() {
        return {
            showConfirmIcon: true,
            isLoading: false,
        }
    },
    props: {
        event_info: {}
    },
    computed: {
        ...mapState({
            user: state => state.login.user
        }),
    },
    methods: {
        callShowConfirm() {
            this.showConfirm()
        },
        async showConfirm() {
            try {
                const self = this; // Сохранение контекста `this`
                await new Promise((resolve) => {
                    Modal.confirm({
                        title: 'Вы уверены, что хотите подписаться на мероприятие?',
                        icon: createVNode(CheckCircleOutlined, {style: 'color: green'}),
                        content: createVNode('div', {
                            style: 'color:red;',
                        }, 'Действие нельзя отменить - платная услуга'),
                        okText: 'Подтвердить',
                        cancelText: 'Отменить',
                        autoFocusButton: null,
                        async onOk() {
                            try {
                                await self.handleCheckout();
                                resolve()
                            } catch (e) {
                                console.log(e)
                            }

                        },
                        onCancel() {
                            console.log('Cancel');
                        },
                        closable: true
                    });
                })
                this.showConfirmIcon = false
            } catch (error) {
                console.error(error);

            }
        },
        async handleCheckout() {
            try {
                const response_PKToken = await getPKForPay();
                const stripePromise = loadStripe(response_PKToken.pk_token);
                const response = await payEvent({'event': this.event_info, 'user': this.user});
                console.log(response)
                const sessionId = response.sessionId;

                if (sessionId) {
                    const stripe = await stripePromise;
                    const {error} = await stripe.redirectToCheckout({
                        sessionId: sessionId,
                    });

                    if (error) {
                        console.error(error);
                    }

                } else {
                    console.error('sessionId is undefined');
                }
            } catch (error) {
                console.error(error);
            }
        },
        async loadSubscribers() {
            this.isLoading = true
            const all_subscribers = await subscribers(this.event_info.id)
            this.isLoading = false
            return all_subscribers
        }

    },
    async created() {
        const all_subscribers = await this.loadSubscribers()
        all_subscribers.forEach((element) => {
            console.log('Я тут')
            if (element.user === this.user.id) {
                this.showConfirmIcon = false
            }
        })
    }
});
</script>

<style scoped>

</style>