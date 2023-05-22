<template>
    <slot :unsubscribe="unsubscribeEvent"></slot>
</template>

<script>
import {unsubscribe} from "../../services/api";
import {Modal} from "ant-design-vue";
import {createVNode} from "vue";
import {CheckCircleOutlined} from "@ant-design/icons-vue";

export default {
    name: "UnsubscribeComponent",
    data() {
        return {
            eventsInfoNew: []
        }
    },
    methods: {
        // async unsubscribeEvent() {
        //     await unsubscribe({event: this.event, unsubscribe: true})
        //     console.log(this.eventsInfo)
        //     this.eventsInfo.forEach((object) => {
        //         if (object.event.id !== this.event.id) {
        //             this.eventsInfoNew.push(object)
        //         }
        //     })
        //     this.$emit('update:eventsInfo', this.eventsInfoNew)
        // },
        async unsubscribeEvent() {
            try {
                const self = this
                await new Promise((resolve) => {
                    Modal.confirm({
                        title: 'Вы уверены, что хотите отписаться от мероприятия?',
                        icon: createVNode(CheckCircleOutlined, {style: 'color: green'}),
                        content: createVNode('div', {
                            style: 'color:red;',
                        }, 'Действие нельзя отменить'),
                        okText: 'Подтвердить',
                        cancelText: 'Отменить',
                        autoFocusButton: null,
                        async onOk() {
                            try {
                                await unsubscribe({event: self.event, unsubscribe: true})
                                self.eventsInfo.forEach((object) => {
                                    if (object.event.id !== self.event.id) {
                                        self.eventsInfoNew.push(object)
                                    }
                                })
                                self.$emit('update:eventsInfo', self.eventsInfoNew)
                                resolve()
                            } catch (e) {
                                console.log(e)
                            }

                        },
                        onCancel() {
                            console.log('Cancel');
                        },
                        closable: true
                    });
                })
            } catch (error) {
                console.error(error);

            }
        },
    },
    props: {
        event: {},
        eventsInfo: {}
    },
    emits: ['update:eventsInfo'],
    created() {
        console.log(this.event, this.eventsInfo)
    }
}
</script>

<style scoped>

</style>