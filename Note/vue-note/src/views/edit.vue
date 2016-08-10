<template>
<app-header></app-header>
<!-- 这里是页面内容区 -->
<div class="content native-scroll">
    <div class="content-block">
        <img src="../assets/avatar.png" id="avatar" alt="">
    </div>
    <div class="content-block">
        <div class="list-block">
            <ul>
                <!-- Text inputs -->
                <li>
                    <div class="item-content">
                        <div class="item-inner">
                            <input type="hidden" id="note-id" name="noteid" v-model="note.id" />
                            <div class="item-title label">时间日期</div>
                            <div class="item-input">
                                <input type="text" placeholder="" v-model="note.datetime"  name="datetime" id="time-picker" readonly="">
                            </div>
                        </div>
                    </div>
                </li>
                <li class="align-top">
                    <div class="item-content">
                        <div class="item-inner">
                            <div class="item-title label">提醒内容</div>
                            <div class="item-input">
                                <textarea name="content" v-model="note.content">{{ note.content }}</textarea>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
    <div class="content-block">
        <a @click="saveNote" class="button button-big button-fill purple">保存提醒</a>
    </div>
</div>
<Navbar></Navbar>
</template>

<script>
import appHeader from '../components/Header'
import Navbar from '../components/Navbar'
import $ from 'zepto'
import store from '../store/Store'
import Config from '../config'
import Cookies from 'cookies-js'

export default {
  created: function () {
    const cookie = Cookies.get('token')
    if (cookie === undefined) {
      this.$route.router.go({name: 'login'})
    }
  },
  data: function () {
    return {
      note: {
        id: 0,
        content: '',
        datetime: ''
      }
    }
  },
  route: {
    data: function (transition) {
      // console.log(transition.to.params)
      if (transition.to.params.state) {
        let note = store.note
        this.note = {
          id: note.id,
          content: note.content,
          datetime: note.reminder
        }
      } else {
        this.note = {
          id: 0,
          content: '',
          datetime: ''
        }
        store.note = this.note
      }
    }
  },
  ready: function () {
    let date = this.initDate(store.note.reminder)
    $('#time-picker').datetimePicker({
      value: [ date.year, date.month, date.date, date.hours, date.minutes ]
    })
  },
  methods: {
    saveNote: function () {
      var _self = this
      if (this.note.content === '') {
        $.toast('提醒内容不能为空')
        return false
      }
      let cookie = Cookies.get('token')
      $.post(Config.BASE_URL + Config.API.note + '?token=' + cookie, this.note, function (data) {
        if (data.success) {
          $.toast('保存成功')
          _self.note = {
            id: 0,
            content: '',
            datetime: ''
          }
        } else {
          $.toast('保存失败')
        }
      })
    },
    initDate: function (d = undefined) {
      let date = ''
      if (d !== undefined) {
        date = new Date(d)
      } else {
        date = new Date()
      }
      let currentDate = {}
      currentDate.year = date.getFullYear()
      currentDate.month = date.getMonth() + 1
      if (currentDate.month < 10) {
        currentDate.month = '0' + currentDate.month
      }
      if (date.getDate() < 10) {
        currentDate.date = '0' + date.getDate()
      } else {
        currentDate.date = date.getDate()
      }
      currentDate.hours = date.getHours()
      currentDate.minutes = date.getMinutes() + 1
      if (currentDate.minutes < 10) {
        currentDate.minutes = '0' + currentDate.minutes
      }
      this.note.datetime = `${currentDate.year}-${currentDate.month}-${currentDate.date} ${currentDate.hours}:${currentDate.minutes}:00`
      return currentDate
    }
  },
  components: {
    appHeader,
    Navbar
  }
}
</script>

<style lang="css">
#avatar {
  width:4rem;
  height: 4rem;
  display: block;
  margin:0px auto;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2rem;
}
</style>
