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
            <!--            TODO выполнить подписку-->
            <edit-outlined v-if="name==='my-event-page'" key="edit" style="font-size: 30px"
                           @click="this.$router.push({name: 'my-event-page-edit', params: {id: event_info.id, slug: slug}})">
            </edit-outlined>
            <a-rate v-if="name==='event-page' && !isLoading" :value="this.rate" disabled allow-half/>
            <div v-else>
                <LoadingOutlined></LoadingOutlined>
            </div>
            <carry-out-outlined
                    v-if="name==='event-page' && !event_info.price && !this.organizators.includes(this.user.id)"
                    style="font-size: 30px"/>
            <pay-circle-outlined
                    v-if="name==='event-page' && event_info.price && !this.organizators.includes(this.user.id)"
                    style="font-size: 30px"/>
        </template>
        <a-card-meta :title=event_info.title
                     :description="event_info.price ? `Платный доступ` : `Посещение свободное`"
                     @click="this.$router.push({name: name, params: {id: event_info.id, slug: slug}})">
        </a-card-meta>
        <div v-if="!isLoading" style="display: inline-block; margin-top:10px; ">
            <a-tag v-for="(tag, index) in event_info.tags" :key="index">
                {{ tag }}
            </a-tag>
        </div>
    </a-card>
</template>
<script>
import {CarryOutOutlined, EditOutlined, LoadingOutlined, PayCircleOutlined} from '@ant-design/icons-vue';
import {defineComponent} from 'vue';
import {getEventRate} from "../../services/api";
import {mapState} from "vuex";

export default defineComponent({
    name: "CardComponent",
    data() {
        return {
            isLoading: false,
            rate: 0,
            organizators: []
        }
    },
    components: {
        EditOutlined, CarryOutOutlined, PayCircleOutlined, LoadingOutlined
    },
    props: {
        event_info: {},
        name: {},
        slug: {},
    },
    computed: {
        ...mapState({
            user: state => state.login.user,
        }),
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
        this.event_info.organizer.forEach((element) => {
            this.organizators.push(element.user)
        })
        if (this.name === 'event-page') {
            this.getRate()
        }
    }
});

</script>

<style scoped>

</style>