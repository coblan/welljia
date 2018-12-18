require('./scss/left_menu.scss')

Vue.component('com-fullhome-left-menu',{
    props:['menuList','crtMenu'],
    data:function(){
        return {
            crt_action:this.crtMenu || this.menuList[0]
        }
    },
    template:`<div class="com-fullhome-left-menu">
    <div :class="['action',{'is_active':crt_action==action}]" v-for="action in menuList" @click="on_click(action)">
        <img v-if="crt_action==action" src="/static/images/big_btn.png" alt="">
        <span class="center-vh" style="z-index:200;white-space: nowrap;" v-text="action.label" ></span>

    </div>
    </div>`,
    methods:{
        on_click:function(action){
            this.crt_action = action
            this.$emit('action',action)
        }
    }

})