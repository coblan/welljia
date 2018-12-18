require('./scss/footer.scss')

//Vue.component('com-fullhome-footer',{
//    data:function(){
//        return {
//            footer_imgs:[
//                '/static/images/foot_1.png',
//                '/static/images/foot_2.png',
//                '/static/images/foot_3.png',
//                '/static/images/foot_4.png',
//            ]
//        }
//    },
//    template:`<div class="com-fullhome-footer">
//        <img v-for="item in footer_imgs" :src="item" alt="">
//    </div>`
//})
require('./scss/footer.scss')

Vue.component('com-fullhome-footer',{
    data:function(){
        return {
        }
    },
    template:`<div class="com-fullhome-footer">
         <div style="text-align: center" >
            <span style="color: #494e5b">
                <span>四川威尔佳科技有限责任公司</span>
                <span class="divider"></span>
                <span>蜀ICP备160XXXX号</span>
            </span>
                 <br>

                <a style="color: #0093f1">@2014-2018 Jongde Software LLC All rights reserved.</a>
         </div>
    </div>`
})