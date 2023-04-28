<template>
    <a-card hoverable style="width: 285px">
        <template #cover>
            <img
                    alt="example"
                    :src=event.photo
                    @click="this.$router.push({name: name, params: {id: event.id, slug: slug}})"/>
        </template>
        <template #actions>
            <edit-outlined v-if="name==='my-event-page'" key="edit" style="font-size: 20px"
                           @click="this.$router.push({name: 'my-event-page-edit', params: {id: event.id, slug: slug}})">
            </edit-outlined>
            <!--            TODO rate-->
            <a-rate v-if="name==='event-page'" :value="2" disabled/>
            <carry-out-outlined v-if="name==='event-page'" style="font-size: 25px"/>
        </template>
        <a-card-meta :title=event.title
                     :description="event.price ? `Цена доступа: ` + event.price + ` р` : `Посещение свободное`"
                     @click="this.$router.push({name: name, params: {id: event.id, slug: slug}})">
            <template #avatar>
                <!--            TODO avatar-->
                <!--                <a-avatar src={{store.state.login.user.photo}}></a-avatar>-->
            </template>
        </a-card-meta>
    </a-card>
</template>
<script>
import {CarryOutOutlined, EditOutlined} from '@ant-design/icons-vue';
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
        EditOutlined, CarryOutOutlined
    },
    props: {
        event: {},
        name: {},
        slug: {},
    }
});

</script>

<style scoped>

</style>