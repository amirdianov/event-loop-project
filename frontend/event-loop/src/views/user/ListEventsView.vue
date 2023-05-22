<template>
    <a-list v-if="!store.state.isLoading" item-layout="vertical" size="large" :pagination="pagination"
            :data-source="eventsInformation">
        <template #footer>
        </template>
        <template #renderItem="{ item }">
            <a-list-item key="item.title">
                <template #actions>
          <span v-for="{ type, text } in item.actions" :key="type">
            <component :is="type" style="margin-right: 8px"/>
            {{ text }}
          </span>
                    <UnsubscribeComponent :event="item.event" v-model:eventsInfo="eventsInformation">
                        <template v-slot:default="slotProps" >
                            <a-button v-if="!item.event.price" @click=slotProps.unsubscribe type="dashed"
                                      style="border-color: red; color: red" >
                                Отписаться от
                                мероприятия
                            </a-button>
                            <a-button v-if="item.event.price" disabled type="dashed"
                                      style="border-color: red; color: red">
                                Отписаться от
                                мероприятия
                            </a-button>
                        </template>

                    </UnsubscribeComponent>
                </template>
                <template #extra>
                    <img
                            width="200"
                            height="200"
                            alt="logo"
                            :src=item.photo
                    />
                </template>
                <a-list-item-meta :description="item.description">
                    <template #title>
                        <RouterLink
                                :to="{name: 'event-page', params: { slug: item.event.category, id: item.event.id }}">
                            {{ item.title }}
                        </RouterLink>
                    </template>
                </a-list-item-meta>
                {{ item.content }}
            </a-list-item>
        </template>
    </a-list>
</template>
<script>
import {LikeOutlined, MessageOutlined, StarOutlined} from '@ant-design/icons-vue';
import {defineComponent, onMounted, ref} from 'vue';
import {getEventComments, getEventRate, getUsersSubscribedEvents} from "../../../services/api";
import store from "@/store";
import UnsubscribeComponent from "@/components/UnsubscribeComponent.vue";

export default defineComponent({
    computed: {
        store() {
            return store
        }
    },
    components: {
        UnsubscribeComponent,
        StarOutlined,
        LikeOutlined,
        MessageOutlined,
    },

    setup() {
        const responseData = ref([]);
        const eventsInformation = ref([]);
        const isLoading = ref(true);
        const commentsCount = ref()
        const rateCount = ref()
        store.state.login.isLoading = true
        onMounted(async () => {
            try {
                responseData.value = await getUsersSubscribedEvents();
                for (const element of responseData.value) {
                    commentsCount.value = await getEventComments(element.event.id)
                    rateCount.value = await getEventRate(element.event.id)
                    const actions = [{
                        type: 'StarOutlined',
                        text: rateCount.value.count,
                    }, {
                        type: 'MessageOutlined',
                        text: commentsCount.value.length,
                    }];
                    console.log(element.event.price)
                    eventsInformation.value.push({
                        actions: actions,
                        event: element.event,
                        eventId: element.event.id,
                        title: element.event.title,
                        photo: element.event.photo,
                        description: element.event.price ? "Платный доступ" : "Посещение свободное",
                        content: element.event.description.length > 500 ? element.event.description.slice(0, 500) + ' ...' : element.event.description,
                    });
                }
                isLoading.value = false

                store.state.login.isLoading = false
            } catch (e) {
                console.log(e);
                isLoading.value = false

                store.state.login.isLoading = false

            }
        });
        const pagination = {
            onChange: page => {
                console.log(page);
            },
            pageSize: 4,
        };
        return {
            eventsInformation,
            pagination,
            isLoading,
        };
    },
});
</script>