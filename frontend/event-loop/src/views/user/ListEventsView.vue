<template>
    <a-list item-layout="vertical" size="large" :pagination="pagination" :data-source="eventsInformation">
        <template #footer>
        </template>
        <template #renderItem="{ item }">
            <a-list-item key="item.title">
                <template #actions>
          <span v-for="{ type, text } in actions" :key="type">
            <component :is="type" style="margin-right: 8px"/>
            {{ text }}
          </span>
                </template>
                <template #extra>
                    <img
                            width="272"
                            alt="logo"
                            :src=item.photo
                    />
                </template>
                <a-list-item-meta :description="item.description">
                    <template #title>
                        <a :href="item.href">{{ item.title }}</a>
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
import {getUsersSubscribedEvents} from "../../../services/api";

export default defineComponent({
    components: {
        StarOutlined,
        LikeOutlined,
        MessageOutlined,
    },
    setup() {
        const responseData = ref([]);
        const eventsInformation = ref([]);
        const isLoading = ref(true);
        onMounted(async () => {
            try {
                responseData.value = await getUsersSubscribedEvents();
                responseData.value.forEach((element) => {
                    console.log(element)
                    eventsInformation.value.push({
                        // href: this.$router.push({
                        //     name: 'my-event-page-edit',
                        //     params: {id: element.id, slug: element.category}
                        // }),
                        title: element.event.title,
                        photo: element.event.photo,
                        description: 'Ant Design, a design language for background applications, is refined by Ant UED Team.',
                        content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
                    });
                    console.log(element.photo)
                })
                isLoading.value = false
            } catch (e) {
                console.log(e);
                isLoading.value = false
            }
        });
        const pagination = {
            onChange: page => {
                console.log(page);
            },
            pageSize: 4,
        };
        const actions = [{
            type: 'StarOutlined',
            text: '156',
        }, {
            type: 'LikeOutlined',
            text: '156',
        }, {
            type: 'MessageOutlined',
            text: '2',
        }];
        return {
            eventsInformation,
            pagination,
            actions,
        };
    },
});
</script>