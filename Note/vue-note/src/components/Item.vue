<template>
<li v-on:click="operation(index, type)">
    <label class='label-checkbox item-content'>
        <div class='item-media'><i class='icon icon-star'></i></div>
        <div class='item-inner'>
            <div class='item-title-row'>
                <div class='item-title'>{{ data.reminder }}</div>
            </div>
            <div class='item-text'>{{ data.content }}</div>
        </div>
    </label>
</li>
</template>

<script>
import $ from 'zepto'

export default {
  props: ['data', 'type', 'index'],
  data: function () {
    return {
      btnGroup: {
        'edit': {
          text: '编辑'
        },
        'delete': {
          text: '删除',
          color: 'danger'
        },
        'revert': {
          text: '恢复'
        },
        'cancel': {
          text: '取消'
        }
      },
      active: {
        index: 0,
        type: ''
      }
    }
  },
  created: function () {
    this.btnGroup['edit'].onClick = this.edit
    this.btnGroup['delete'].onClick = this.delete
    this.btnGroup['revert'].onClick = this.revert
  },
  computed: {},
  ready: function () {},
  attached: function () {},
  methods: {
    delete: function () {
      this.$dispatch('deleteItem', this.active)
    },
    edit: function () {
      this.$dispatch('editItem', this.active)
    },
    revert: function () {
      this.$dispatch('revertItem', this.active)
    },
    operation: function (index, type) {
      if (this.$route.name !== 'list') {
        return false
      }
      this.active = {
        index: index,
        type: type
      }
      let btnGroup = []
      if (type === 'undo') {
        btnGroup = [[this.btnGroup['edit'], this.btnGroup['delete']], [this.btnGroup['cancel']]]
      } else if (type === 'done') {
        btnGroup = [[this.btnGroup['delete']], [this.btnGroup['cancel']]]
      } else if (type === 'trash') {
        btnGroup = [[this.btnGroup['revert'], this.btnGroup['delete']], [this.btnGroup['cancel']]]
      }
      $.actions(btnGroup)
    }
  },
  components: {}
}
</script>

<style lang="css">
</style>
