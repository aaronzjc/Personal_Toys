<template>
<app-header>
  <a class="button button-link button-nav pull-left back" v-link="{ name: 'list', replace: true}">
    <span class="icon icon-left"></span>
    返回
  </a>
  <h1 class="title">搜索</h1>
</app-header>
<div class="content native-scroll" id="">
<div class="content-padded">

<div class="searchbar row">
<div class="search-input col-80">
  <label class="icon icon-search" for="search"></label>
  <input type="search" id="search" v-model="keyword" placeholder="输入关键字...">
</div>
<a class="button button-fill button-primary col-20" id="searchbtn" @click="search">搜索</a>
</div>

</div>
<div class="content-scroll" id="search-result">
<div class="list-block media-list todo-items">
    <ul>
      <Item type="undo"
        v-for="note in data.undo"
        :data="note"
        :index="$index">
      </Item>
      <Item type="done"
        v-for="note in data.done"
        :data="note"
        :index="$index">
      </Item>
      <Item type="trash"
        v-for="note in data.trash"
        :data="note"
        :index="$index">
      </Item>
    </ul>
</div>
</div>
</div>
</template>

<script>
import appHeader from '../components/Header'
import Item from '../components/Item'
import Config from '../config'
import Cookies from 'cookies-js'
import $ from 'zepto'

export default {
  created: function () {
    const cookie = Cookies.get('token')
    this.cookie = cookie
    if (cookie === undefined) {
      this.$route.router.go({path: '/login'})
    }
  },
  data: function () {
    return {
      cookie: '',
      keyword: '',
      data: {}
    }
  },
  route: {
    data: function (transition) {}
  },
  computed: {},
  ready: function () {},
  attached: function () {},
  methods: {
    search: function () {
      var _self = this
      var keyword = this.keyword
      $.post(Config.BASE_URL + Config.API.search + '?token=' + this.cookie, {keyword: keyword}, function (data) {
        if (data.success) {
          _self.data = data.data
        } else {
          $.toast('系统错误')
        }
      }, 'json')
    }
  },
  components: {
    appHeader,
    Item
  }
}
</script>

<style lang="css">
</style>
