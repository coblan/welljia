require('./scss/footer.scss')

Vue.component('com-fullhome-footer',{
    data:function(){
        return {
            footer_imgs:[
                '/static/images/foot_1.png',
                '/static/images/foot_2.png',
                '/static/images/foot_3.png',
                '/static/images/foot_4.png',
            ]
        }
    },
    template:`<div class="com-fullhome-footer">
        <img v-for="item in footer_imgs" :src="item" alt="">
    </div>`
})