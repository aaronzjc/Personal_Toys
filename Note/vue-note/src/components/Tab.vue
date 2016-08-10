<template>
  <div :id="name" :class="className">
      <div class="content-scroll">
          <div class="list-block media-list">
              <ul><slot></slot></ul>
          </div>
      </div>
  </div>
</template>

<script>
import Item from '../components/Item'

export default {
  props: ['name', 'status'],
  data: function () {
    return {
      className: {
        tab: true,
        active: this.status
      }
    }
  },
  computed: {},
  ready: function () {},
  attached: function () {},
  methods: {},
  components: {
    Item
  }
}
</script>

<style lang="css">
</style>
