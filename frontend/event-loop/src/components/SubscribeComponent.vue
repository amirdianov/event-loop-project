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
import {CarryOutOutlined, CheckCircleOutlined, CheckOutlined, LoadingOutlined} from "@ant-design/icons-vue";
import {Modal} from 'ant-design-vue';
import {subscribe, subscribers} from "../../services/api";
import {mapState} from "vuex";

export default defineComponent({
    name: "SubscribeComponent",
    components: {LoadingOutlined, CarryOutOutlined, CheckOutlined},
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
                        // content: createVNode('div', {
                        //     style: 'color:red;',
                        // }, 'Действие нельзя будет отменить по техническим причинам'),
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
            console.log(this.event_info.id)
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