<template>
    <a-card hoverable style="width: 285px">
        <template #cover>
            <img
                    alt="example"
                    :src=event.photo
                    @click="this.$router.push({name: 'my-event-page', params: {id: event.id}})"/>
        </template>
        <template #actions>
            <edit-outlined key="edit" @click="this.$router.push({name: 'my-event-page-edit', params: {id: event.id}})">
            </edit-outlined>
        </template>
        <a-card-meta :title=event.title :description="event.price ? event.price + ` р` : `Посещение свободное`"
                     @click="this.$router.push({name: 'my-event-page', params: {id: event.id}})">
            <template #avatar>
                <!--                <a-avatar src={{store.state.login.user.photo}}></a-avatar>-->
            </template>
        </a-card-meta>
    </a-card>
</template>
<script>
import {EditOutlined, EllipsisOutlined, SettingOutlined} from '@ant-design/icons-vue';
import {defineComponent} from 'vue';
import store from "../store";

export default defineComponent({
    name: "CardComponent",
    computed: {
        store() {
            return store
        }
    },

    components: {
        SettingOutlined,
        EditOutlined,
        EllipsisOutlined,
    },
    props: {
        event: {},
    }
});

</script>

<style scoped>

</style>