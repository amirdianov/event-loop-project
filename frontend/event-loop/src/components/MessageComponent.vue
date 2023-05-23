<template></template>
<script>
import {notification} from 'ant-design-vue';
import {defineComponent} from 'vue';

export default defineComponent({

    name: "MessageComponent",
    props: {
        typeMessage: {},
        messageText: {},
        messageDescription: {}
    },
    setup() {
        function openNotificationWithIcon(type, msg, desc) {
            notification[type]({
                message: msg,
                description: desc,
                placement: 'bottomRight',
                style: type=== 'error' ? 'background-color: #f7d5df' : 'background-color: #d5f7d9'
            });
        }

        return {
            openNotificationWithIcon,
        };
    },
    created() {
        this.openNotificationWithIcon(this.typeMessage, this.messageText, this.messageDescription)
    }
});
</script>
<style scoped>

</style>