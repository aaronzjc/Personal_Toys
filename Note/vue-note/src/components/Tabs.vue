<template>
<!-- 这里是页面内容区 -->
<div class="content native-scroll">
    <div class="buttons-tab">
        <a href="#undo" class="tab-link button active">待提醒</a>
        <a href="#done" class="tab-link button">已提醒</a>
        <a href="#trash" class="tab-link button">回收站</a>
    </div>
    <div class="tabs">
      <slot></slot>
    </div>
</div>
</template>

<script>
export default {
  data: function () {
    return {

    }
  },
  computed: {},
  ready: function () {},
  attached: function () {},
  methods: {},
  components: {}
}
</script>

<style lang="css">
</style>
