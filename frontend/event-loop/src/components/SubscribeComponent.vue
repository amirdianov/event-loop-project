<template>
    <div v-if="!isLoading">
        <carry-out-outlined v-if="this.showConfirmIcon" style="font-size: 30px" @click="callShowConfirm"/>
        <check-outlined v-else style="font-size: 30px"/>
    </div>
</template>


<script>
import {createVNode, defineComponent} from 'vue';
import {CarryOutOutlined, CheckCircleOutlined, CheckOutlined} from "@ant-design/icons-vue";
import {Modal} from 'ant-design-vue';
import {subscribe, subscribers} from "../../services/api";
import {mapState} from "vuex";

export default defineComponent({
    name: "SubscribeComponent",
    components: {CarryOutOutlined, CheckOutlined},
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
            this.showConfirm(this.event_info)
        },
        async showConfirm(event) {
            try {
                await new Promise((resolve) => {
                    Modal.confirm({
                        title: 'Вы уверены, что хотите подписаться на мероприятие?',
                        icon: createVNode(CheckCircleOutlined, {style: 'color: green'}),
                        content: createVNode('div', {
                            style: 'color:red;',
                        }, 'Действие нельзя будет отменить по техническим причинам'),
                        okText: 'Подтвердить',
                        cancelText: 'Отменить',
                        autoFocusButton: null,
                        async onOk() {
                            await subscribe({'event': event});
                            resolve()
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
        //     TODO посмотреть Participant к данному методу,
        //      TODO если он есть в подписчиках, то this.showConfirmIcon = false
        //     TODO предаешь this.event_info.id и user.id  в isSubscribed() и смотришь после
        //     TODO какой ответ выдает API
    }
});
</script>

<style scoped>

</style>