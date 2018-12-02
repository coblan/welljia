require('./scss/left_menu.scss')

Vue.component('com-fullhome-left-menu',{
    props:['menuList'],
    template:`<div class="com-fullhome-left-menu">
    <div class="action" v-for="menu in menuList" @click="$emit('action',menu)">
        <span v-text="menu.label" ></span>
    </div>
    </div>`
})