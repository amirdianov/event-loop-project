<template>
  <div class="page-loader">
    <LoadingOutlined :style="{fontSize: '50px', color: '#4d2a16'}"/>
  </div>
</template>

<script>
import {LoadingOutlined} from "@ant-design/icons-vue";

export default {
    components: {LoadingOutlined},
    name: "PageLoaderComponent"
}
</script>

<style scoped>
.page-loader {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #c7cedf;
    z-index: 999;
}
</style>