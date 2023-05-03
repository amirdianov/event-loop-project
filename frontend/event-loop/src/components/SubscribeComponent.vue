<template>
    <carry-out-outlined v-if="this.showConfirmIcon" style="font-size: 30px" @click="callShowConfirm"/>
    <check-outlined v-else style="font-size: 30px"/>
</template>


<script>
import {createVNode, defineComponent} from 'vue';
import {CarryOutOutlined, CheckCircleOutlined, CheckOutlined} from "@ant-design/icons-vue";
import {Modal} from 'ant-design-vue';
import {subscribe} from "../../services/api";

export default defineComponent({
    name: "SubscribeComponent",
    components: {CarryOutOutlined, CheckOutlined},
    data() {
        return {
            showConfirmIcon: true,
        }
    },
    props: {
        event_info: {}
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
        }

    },
    created() {
        //     TODO посмотреть Participant к данному методу,
        //      TODO если он есть в подписчиках, то this.showConfirmIcon = false
    }
});
</script>

<style scoped>

</style>