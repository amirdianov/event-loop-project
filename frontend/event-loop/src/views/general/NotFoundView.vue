<template>
    <a-row type="flex" justify="center" align="middle" style="min-height: 550px">
        <a-col>
            <div>
                <img src="@/assets/images/404-error-with-people-holding-numbers-concept-illustration_114360-7913.png"
                        alt="Ошибка" width="750" height="500">
            </div>
        </a-col>
    </a-row>
</template>

<script>
import {LoadingOutlined} from "@ant-design/icons-vue";

export default {
    name: "NotFoundView",
    components: {LoadingOutlined}
}
</script>

<style scoped>

</style>