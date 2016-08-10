<template>
<!-- 工具栏 -->
<nav class="bar bar-tab">
    <a class="tab-item active" v-link="{ path: '/edit', activeClass: 'active'}">
        <span class="icon icon-edit"></span>
        <span class="tab-label">添加</span>
    </a>
    <a class="tab-item" v-link="{ path: '/list', activeClass: 'active'}">
        <span class="icon icon-clock"></span>
        <span class="tab-label">管理</span>
    </a>
    <a class="tab-item">
        <span class="icon icon-settings"></span>
        <span class="tab-label">待开发</span>
    </a>
</nav>
</template>

<script>
export default {
  data: function () {
    return {
    }
  }
}
</script>

<style lang="css">
</style>
