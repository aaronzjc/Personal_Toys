<template>
<app-header></app-header>
<!-- 这里是页面内容区 -->
<div class="content native-scroll">
  <div class="content-block">
      <div class="list-block">
          <ul>
              <!-- Text inputs -->
              <li>
                  <div class="item-content">
                      <div class="item-inner">
                          <div class="item-input">
                              <input type="text" name="username" placeholder="用户名" v-model="username">
                          </div>
                      </div>
                  </div>
              </li>
              <li class="align-top">
                  <div class="item-content">
                      <div class="item-inner">
                          <div class="item-input">
                              <input type="password" name="password" placeholder="密码" v-model="password">
                          </div>
                      </div>
                  </div>
              </li>
          </ul>
      </div>
  </div>
  <div class="content-block">
      <a v-on:click="login" class="button button-big button-fill">登录</a>
  </div>
</div>
</template>

<script>
import $ from 'zepto'
import appHeader from '../components/Header'
import Config from '../config'
import Cookies from 'cookies-js'

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  ready () {
    $.init()
  },
  methods: {
    login () {
      $.ajax({
        type: 'POST',
        url: Config.BASE_URL + Config.API.login,
        data: {name: this.username, password: this.password},
        dataType: 'json',
        success: data => {
          console.log(data)
          Cookies.set('token', data.token)
          this.$route.router.go({path: '/edit'})
        },
        error: (xhr, type) => {
          $.hidePreloader()
          $.toast('登录失败')
        }
      })
    }
  },
  components: {
    appHeader
  }
}
</script>
