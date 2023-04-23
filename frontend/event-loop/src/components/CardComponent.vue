<template>
    <a-card hoverable style="width: 285px">
        <template #cover>
            <img
                    alt="example"
                    :src=photo
            />
        </template>
        <template #actions>
            <setting-outlined key="setting"/>
            <edit-outlined key="edit"/>
            <ellipsis-outlined key="ellipsis"/>
        </template>
        <a-card-meta :title=title :description=description>
            <template #avatar>
                <a-avatar src="https://joeschmoe.io/api/v1/random"/>
            </template>
        </a-card-meta>
    </a-card>
</template>
<script>
import {EditOutlined, EllipsisOutlined, SettingOutlined} from '@ant-design/icons-vue';
import {defineComponent} from 'vue';

export default defineComponent({
    name: "CardComponent",

    components: {
        SettingOutlined,
        EditOutlined,
        EllipsisOutlined,
    },
    props: {
        title: {},
        description: {},
        photo: {},
    }
});

</script>

<style scoped>

</style>