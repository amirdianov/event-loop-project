<template>
    <form @submit.prevent="connect">
        <input placeholder="ID события" v-model="eventId"/>
        <button>Подключиться</button>
    </form>
    <hr>
    <form @submit.prevent="sendMessage">
        <input placeholder="Сообщение" v-model="message"/>
        <button>Отправить</button>
    </form>

    <b>Сообщения</b>
    <pre>{{ messages }}</pre>
</template>

<script>

import {initNotifications} from "../../services/notifications";

export default {
    name: "NotificationView",
    data() {
        return {
            eventId: null,
            message: null,
            messages: ''
        };
    },
    methods: {
        connect() {
            this.send = initNotifications(this.eventId, (message) => {
                this.messages += message.message + "\n";
            })
        },
        sendMessage() {
            this.send({message: this.message});
            this.message = null;
        }
    }
}
</script>