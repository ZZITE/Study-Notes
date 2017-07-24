webpackJsonp([0],[
/* 0 */,
/* 1 */,
/* 2 */,
/* 3 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_vue_router__ = __webpack_require__(18);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__components_hellow__ = __webpack_require__(13);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__components_hellow___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2__components_hellow__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__components_login__ = __webpack_require__(14);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__components_login___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3__components_login__);




__WEBPACK_IMPORTED_MODULE_0_vue__["a" /* default */].use(__WEBPACK_IMPORTED_MODULE_1_vue_router__["a" /* default */]);

/* harmony default export */ __webpack_exports__["a"] = (new __WEBPACK_IMPORTED_MODULE_1_vue_router__["a" /* default */]({
  routes: [{
    path: '/',
    name: 'login',
    component: __WEBPACK_IMPORTED_MODULE_3__components_login___default.a
  }, {
    path: '/hellow',
    name: 'hellow',
    component: __WEBPACK_IMPORTED_MODULE_2__components_hellow___default.a
  }]
}));

/***/ }),
/* 4 */
/***/ (function(module, exports, __webpack_require__) {


/* styles */
__webpack_require__(10)

var Component = __webpack_require__(1)(
  /* script */
  __webpack_require__(6),
  /* template */
  __webpack_require__(15),
  /* scopeId */
  null,
  /* cssModules */
  null
)

module.exports = Component.exports


/***/ }),
/* 5 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_vuex__ = __webpack_require__(2);



__WEBPACK_IMPORTED_MODULE_0_vue__["a" /* default */].use(__WEBPACK_IMPORTED_MODULE_1_vuex__["a" /* default */])

const store = new __WEBPACK_IMPORTED_MODULE_1_vuex__["a" /* default */].Store({
  // 定义状态
  state: {
   name: ''
    },
  mutations: {
    hellowName(state,change) {
      state.name = change
    }
  }
})

/* harmony default export */ __webpack_exports__["a"] = (store);

/***/ }),
/* 6 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });


/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'app'
});

/***/ }),
/* 7 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });


/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'hellow',
  data: function data() {
    return {};
  },

  computed: {
    name: function name() {
      return this.$store.state.name;
    }
  }
});

/***/ }),
/* 8 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });


/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'login',
  data: function data() {
    return {
      login: '登录',
      name: ''
    };
  },

  methods: {
    addName: function addName() {
      if (this.name === '') {
        alert('请输入账户密码');
        return;
      }
      this.$store.commit('hellowName', this.name);
      this.$router.push({ path: '/hellow' });
    }
  }
});

/***/ }),
/* 9 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__App__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__App___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1__App__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__router__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_vuex__ = __webpack_require__(2);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__vuex_store__ = __webpack_require__(5);







__WEBPACK_IMPORTED_MODULE_0_vue__["a" /* default */].config.productionTip = false;

new __WEBPACK_IMPORTED_MODULE_0_vue__["a" /* default */]({
  el: '#app',
  router: __WEBPACK_IMPORTED_MODULE_2__router__["a" /* default */],
  store: __WEBPACK_IMPORTED_MODULE_4__vuex_store__["a" /* default */],
  template: '<App/>',
  components: { App: __WEBPACK_IMPORTED_MODULE_1__App___default.a }
});

/***/ }),
/* 10 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 11 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 12 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 13 */
/***/ (function(module, exports, __webpack_require__) {


/* styles */
__webpack_require__(11)

var Component = __webpack_require__(1)(
  /* script */
  __webpack_require__(7),
  /* template */
  __webpack_require__(16),
  /* scopeId */
  "data-v-639e85d6",
  /* cssModules */
  null
)

module.exports = Component.exports


/***/ }),
/* 14 */
/***/ (function(module, exports, __webpack_require__) {


/* styles */
__webpack_require__(12)

var Component = __webpack_require__(1)(
  /* script */
  __webpack_require__(8),
  /* template */
  __webpack_require__(17),
  /* scopeId */
  "data-v-717e7f69",
  /* cssModules */
  null
)

module.exports = Component.exports


/***/ }),
/* 15 */
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    attrs: {
      "id": "app"
    }
  }, [_c('router-view')], 1)
},staticRenderFns: []}

/***/ }),
/* 16 */
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    staticClass: "hellow"
  }, [_c('h2', [_vm._v("\n   你好，" + _vm._s(_vm.name) + "\n ")])])
},staticRenderFns: []}

/***/ }),
/* 17 */
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    staticClass: "wrap"
  }, [_c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.name),
      expression: "name"
    }],
    attrs: {
      "type": "text",
      "placeholder": "账户名"
    },
    domProps: {
      "value": (_vm.name)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.name = $event.target.value
      }
    }
  }), _vm._v(" "), _c('br'), _vm._v(" "), _c('input', {
    attrs: {
      "type": "password",
      "placeholder": "密码"
    }
  }), _vm._v(" "), _c('br'), _vm._v(" "), _c('button', {
    on: {
      "click": function($event) {
        _vm.addName()
      }
    }
  }, [_vm._v(_vm._s(_vm.login))])])
},staticRenderFns: []}

/***/ })
],[9]);
//# sourceMappingURL=app.3ad8aabe565373e2000e.js.map