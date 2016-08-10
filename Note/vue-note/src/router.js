export default function (router) {
  router.map({
    '*': {
      name: 'main',
      component: function (resolve) {
        require(['./views/login'], resolve)
      }
    },
    '/login': {
      name: 'login',
      component: function (resolve) {
        require(['./views/login'], resolve)
      }
    },
    '/edit': {
      name: 'edit',
      canReuse: false,
      component: function (resolve) {
        require(['./views/edit'], resolve)
      }
    },
    '/edit/:state': {
      name: 'editNote',
      canReuse: false,
      component: function (resolve) {
        require(['./views/edit'], resolve)
      }
    },
    '/list': {
      name: 'list',
      component: function (resolve) {
        require(['./views/list'], resolve)
      }
    },
    '/search': {
      name: 'search',
      component: function (resolve) {
        require(['./views/search'], resolve)
      }
    },
    '/hello': {
      name: 'hello',
      component: function (resolve) {
        require(['./components/Hello'], resolve)
      }
    }
  })
}
