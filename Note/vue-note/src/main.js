import Vue from 'vue'
import VueRouter from 'vue-router'
import RouterConfig from './router'
import App from './App'

Vue.use(VueRouter)

var router = new VueRouter({
  hashbang: true,
  history: false,
  saveScrollPosition: true,
  transitionOnLoad: true
})

RouterConfig(router)

router.start(App, '#app')
