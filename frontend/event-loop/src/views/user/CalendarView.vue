<template>
    <a-calendar v-if="!isLoading" v-model:value="value">
        <template #dateCellRender="{ current }">
            <ul class="events">
                <li v-for="item in getListData(current)" :key="item.content">
                    <a-badge :status="item.type" :text="item.content"/>
                </li>
            </ul>
        </template>
        <template #monthCellRender="{ current }">
            <div v-if="getMonthData(current)" class="notes-month" style="font-size: 15px">
                <section>{{ getMonthData(current) }}</section>
                <span>Количество мероприятий</span>
            </div>
        </template>
    </a-calendar>
</template>
<script>
import {defineComponent, onMounted, ref} from 'vue';
import {getUsersSubscribedEvents} from "../../../services/api/subscribtion";

export default defineComponent({
    setup() {
        const value = ref();
        const eventsInformation = ref([]);
        const isLoading = ref(true);

        onMounted(async () => {
            try {
                eventsInformation.value = await getUsersSubscribedEvents();
                console.log(eventsInformation.value)
                isLoading.value = false
            } catch (e) {
                console.log(e);
                isLoading.value = false
            }
        });
        const getListData = value => {
            let listData = [];
            const date = value.format("YYYY-MM-DD");
            eventsInformation.value.forEach((variable) => {
                if (variable.event.start_time === date) {
                    listData.push({type: 'success', content: `${variable.event.title}`})
                }
                if (variable.event.finish_time === date) {
                    listData.push({type: 'error', content: `${variable.event.title}`})
                }
            })
            return listData || [];
        };
        const getMonthData = value => {
            const month = value.month();
            return '';
        };
        return {
            value,
            getListData,
            getMonthData,
            isLoading,
            eventsInformation
        };
    },
});
</script>
<style scoped>
.events {
    list-style: none;
    margin: 0;
    padding: 0;
}

.events .ant-badge-status {
    overflow: hidden;
    white-space: nowrap;
    width: 100%;
    text-overflow: ellipsis;
    font-size: 12px;
}

.notes-month {
    text-align: center;
    font-size: 28px;
}

.notes-month section {
    font-size: 28px;
}
</style>
