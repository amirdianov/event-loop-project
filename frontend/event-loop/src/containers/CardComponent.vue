<template>
    <a-card hoverable style="width: 285px">
        <template #cover>
            <img
                    alt="example"
                    :src=event_info.photo
                    @click="this.$router.push({name: name, params: {id: this.event_info.id, slug: this.slug}})"
                    width="300" height="300"
            />
        </template>
        <template #actions>
            <edit-outlined v-if="name==='my-event-page'" key="edit" style="font-size: 20px"
                           @click="this.$router.push({name: 'my-event-page-edit', params: {id: event_info.id, slug: slug}})">
            </edit-outlined>
            <!--            TODO rate-->
            <a-rate v-if="name==='event-page'" :value="2" disabled/>
            <carry-out-outlined v-if="name==='event-page'" style="font-size: 25px"/>
        </template>
        <a-card-meta :title=event_info.title
                     :description="event_info.price ? `Цена доступа: ` + event_info.price + ` р` : `Посещение свободное`"
                     @click="this.$router.push({name: name, params: {id: event_info.id, slug: slug}})">
            <template #avatar>
                <!--            TODO avatar-->
                <!--                <a-avatar src={{store.state.login.user.photo}}></a-avatar>-->
            </template>
        </a-card-meta>
<!--        TODO tags-->
        <div style="display: inline-block; margin-top:10px;">
            <a-tag>Tag 1</a-tag>
            <a-tag>Tag 1</a-tag>

        </div>

    </a-card>
</template>
<script>
import {CarryOutOutlined, EditOutlined} from '@ant-design/icons-vue';
import {defineComponent} from 'vue';

export default defineComponent({
    name: "CardComponent",

    components: {
        EditOutlined, CarryOutOutlined
    },
    props: {
        event_info: {},
        name: {},
        slug: {},
    }
});

</script>

<style scoped>

</style>