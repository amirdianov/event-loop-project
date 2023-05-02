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
            <a-rate v-if="name==='event-page' && !isLoading" :value="this.rate" disabled allow-half/>
            <carry-out-outlined v-if="name==='event-page'" style="font-size: 25px"/>
        </template>
        <a-card-meta :title=event_info.title
                     :description="event_info.price ? `Платный доступ` : `Посещение свободное`"
                     @click="this.$router.push({name: name, params: {id: event_info.id, slug: slug}})">
            <template #avatar>
                <!--            TODO avatar-->
                <!--                <a-avatar src={{store.state.login.user.photo}}></a-avatar>-->
            </template>
        </a-card-meta>
        <div style="display: inline-block; margin-top:10px;">
            <a-tag v-for="(tag, index) in event_info.tags" :key="index">
                {{ tag }}
            </a-tag>
        </div>
    </a-card>
</template>
<script>
import {CarryOutOutlined, EditOutlined} from '@ant-design/icons-vue';
import {defineComponent} from 'vue';
import {getEventRate} from "../../services/api";

export default defineComponent({
    name: "CardComponent",
    data() {
        return {
            isLoading: false,
            rate: 0
        }
    },
    components: {
        EditOutlined, CarryOutOutlined
    },
    props: {
        event_info: {},
        name: {},
        slug: {},
    },
    methods: {
        async getRate() {
            this.isLoading = true
            const obj = await getEventRate(this.event_info.id)
            console.log(obj)
            this.rate = obj['rate']
            this.isLoading = false
        }
    },
    created() {
        this.getRate()
    }
});

</script>

<style scoped>

</style>