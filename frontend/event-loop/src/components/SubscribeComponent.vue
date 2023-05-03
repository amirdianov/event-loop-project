<template>
    <carry-out-outlined v-if="this.confirm" style="font-size: 30px" @click="showConfirm"/>
</template>


<script>
import {createVNode, defineComponent} from 'vue';
import {CarryOutOutlined, CheckCircleOutlined} from "@ant-design/icons-vue";
import {Modal} from 'ant-design-vue';

export default defineComponent({
    name: "SubscribeComponent",
    components: {CarryOutOutlined},
    data() {
        return {
            confirm: true
        }
    },
    methods: {
        answerFromModal() {
        }
    },
    setup() {
        const showConfirm = () => {
            Modal.confirm({
                title: 'Вы уверены, что хотите подписаться на мероприятие?',
                icon: createVNode(CheckCircleOutlined, {style: 'color: green'}),
                content: createVNode('div', {
                    style: 'color:red;',
                }, 'Действие нельзя будет отменить по техническим причинам'),
                okText: 'Подтвердить',
                cancelText: 'Отменить',
                autoFocusButton: null,
                onOk() {
                    console.log('OK');
                },
                onCancel() {
                    console.log('Cancel');
                },
                closable: true
            });
        };
        return {
            showConfirm,
        }
    },
});
</script>

<style scoped>

</style>