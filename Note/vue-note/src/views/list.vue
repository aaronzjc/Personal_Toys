<template>
<app-header>
  <a class="icon icon-search pull-right" v-link="{ name: 'search', exact: true}"></a>
  <h1 class="title">飘飘</h1>
</app-header>
<Tabs>
  <Tab name="undo" status="active">
    <Item type="undo"
      v-for="note in data.undo"
      :data="note"
      :index="$index">
    </Item>
  </Tab>
  <Tab name="done">
    <Item type="done"
      v-for="note in data.done"
      :data="note"
      :index="$index">
    </Item>
  </Tab>
  <Tab name="trash">
    <Item type="trash"
      v-for="note in data.trash"
      :data="note"
      :index="$index">
    </Item>
  </Tab>
</Tabs>
<Navbar></Navbar>
</template>

<script>
import appHeader from '../components/Header'
import Navbar from '../components/Navbar'
import Tabs from '../components/Tabs'
import Tab from '../components/Tab'
import Item from '../components/Item'
import $ from 'zepto'
import Config from '../config'
import Cookies from 'cookies-js'
import store from '../store/Store'

export default {
  created: function () {
    const cookie = Cookies.get('token')
    this.cookie = cookie
    if (cookie === undefined) {
      this.$route.router.go({path: '/login'})
    }
    var _self = this
    $.ajax({
      type: 'GET',
      url: Config.BASE_URL + Config.API.note + '?token=' + cookie,
      beforeSend: function (xhr) {
        xhr.withCredentials = true
      },
      success: function (data) {
        _self.data = data.data
      },
      error: function (xhr, type) {
        _self.$route.router.go({path: '/login'})
        console.log(xhr)
      }
    })
  },
  data: function () {
    return {
      cookie: '',
      data: {}
    }
  },
  events: {
    'deleteItem': function (msg) {
      var _self = this
      // 如果是待提醒，则移到回收站；回收站的，则彻底删除
      var note = this.data[msg.type][msg.index]
      $.get(Config.BASE_URL + Config.API.delete + '?token=' + this.cookie, {id: note.id}, function (data) {
        if (data.success) {
          $.toast('删除成功')
          if (msg.type !== 'trash') {
            note['type'] = 'trash'
            _self.data['trash'].push(note)
          }
          _self.data[msg.type].splice(msg.index, 1)
        } else {
          $.toast('删除失败')
        }
      })
    },
    'editItem': function (msg) {
      // 编辑项
      var note = this.data[msg.type][msg.index]
      store.note = note
      this.$router.go({name: 'editNote', params: {state: 1}})
    },
    'revertItem': function (msg) {
      var _self = this
      // 从回收站恢复到已提醒
      var note = this.data[msg.type][msg.index]
      $.get(Config.BASE_URL + Config.API.revert + '?token=' + this.cookie, {id: note.id}, function (data) {
        if (data.success) {
          $.toast('已恢复至已提醒')
          if (msg.type === 'trash') {
            note['type'] = 'done'
            _self.data['done'].push(note)
          }
          _self.data[msg.type].splice(msg.index, 1)
        } else {
          $.toast('恢复失败')
        }
      })
    }
  },
  computed: {},
  ready: function () {
  },
  attached: function () {},
  methods: {},
  components: {
    appHeader,
    Navbar,
    Tabs,
    Tab,
    Item
  }
}
</script>

<style lang="css">
</style>
