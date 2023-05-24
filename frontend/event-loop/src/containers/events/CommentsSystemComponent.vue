<template>
    <a-row type="flex" justify="space-around">
        <a-col style="width: 100%; margin:  30px 20px 0 50px">
            <h1><strong>Комментарии</strong></h1>
            <div class="comments-list">
                <a-list
                        v-if="comments"
                        :data-source="comments"
                        item-layout="horizontal"
                >
                    <template #renderItem="{ item }">
                        <a-list-item style="margin-left: 15px">
                            <a-comment
                                    :author="item.user_name"
                                    :content="item.text"
                                    :datetime="item.created_at"
                            />
                        </a-list-item>
                    </template>
                </a-list>
            </div>
            <a-comment>
                <template #content>
                    <a-form-item>
                        <a-textarea v-model:value="this.value" :rows="4"/>
                    </a-form-item>
                    <a-form-item>
                        <a-button html-type="submit" :loading="this.submitting" type="primary" @click="sendMessage">
                            Комментировать
                        </a-button>
                    </a-form-item>
                </template>
            </a-comment>
        </a-col>
    </a-row>
</template>
<script>
import {defineComponent} from 'vue';
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';
import {initNotifications} from "../../../services/notifications";
import store from "@/store";
import {addEventComment} from "../../../services/api/comments";

dayjs.extend(relativeTime);
export default defineComponent({
    data() {
        return {
            comments: this.event_comments,
            submitting: false,
            value: '',
        }
    },
    props: {
        event_comments: {}
    },
    created() {
        this.send = initNotifications(this.$route.params.id, (message) => {
            this.comments = [message, ...this.comments];
        })
    },
    methods: {
        sendMessage() {
            console.log('Я тут')
            let comment = {
                user_name: store.state.login.user.name,
                text: this.value,
                created_at: dayjs().fromNow()
            }
            this.send(comment);
            this.addComment(comment)
            this.value = null;

        },
        async addComment(comment) {
            comment['user'] = store.state.login.user.id
            comment['event'] = this.$route.params.id
            this.submitting = true
            await addEventComment(comment)
            this.submitting = false
        }
    }
})
</script>
<style>
.ant-comment-avatar {
    margin-right: 0;
}

.comments-list {
    min-height: 200px;
    max-height: 200px;
    overflow: auto;
    border: 1px solid #a9a8a8;
    border-radius: 5px;
    margin-top: 12px
}
</style>