require('./scss/builder_floor.scss')

Vue.component('com-builder-floor',{
    props:['building'],
    template:`<div class="com-builder-floor clickable flex-v">
          <div class="big-title"><h5 v-text="building.label"></h5></div>
          <div class="floors flex-grow">
            <div v-for="floor in building.floors" :class="['floor flex',floor.status]" @click="show_img(floor)">
                <!--<slot :floor="floor"></slot>-->
                <div style="color: #a3a3a3;padding-left: 8px"> <i class="fa fa-home"></i></div>
                <span class="flex-grow" v-text="floor.label"></span>
                <!--<span style="display: inline-block;margin-left: 1em;">-->
                    <!--<button @click="show_2d(floor.img_2d)">2D</button>-->
                    <!--<button @click="show_3d(floor.img_3d)">3D</button>-->
                <!--</span>-->

            </div>
          </div>
    </div>`,
    methods:{
        show_img:function(floor){
            var ctx={
                floor:floor
            }
            pop_layer(ctx,'com-pop-huxing',function(){},{
                title:false,
                area: ['90%', '90%'],
                shade: 0.8,
                skin: 'img-shower',
                shadeClose: true,
            })
        },
    }
})


Vue.component('com-pop-huxing',{
    props:['ctx'],
    data:function(){
        return {
            crt_view:'2d',
            read_3d:''
        }
    },
    computed:{
        wraped_3d:function(){
            return '/3d_wrap?d3_url='+encodeURIComponent(this.ctx.floor.img_3d)
        }
    },
    methods:{
        start_read:function(){
            this.read_3d= this.wraped_3d
        }
    },
    template:`<div class="com-pop-huxing"  style="position: absolute;top:0;left: 0;bottom: 0;right: 0;">
             <img v-show="crt_view=='2d'" class="center-vh" :src="ctx.floor.img_2d" style="max-width: 95%;max-height:95%" alt="">
             <iframe allowvr="yes" scrolling="no" v-show="crt_view=='3d'" :src="wraped_3d" frameborder="0" width="100%" height="100%"></iframe>
             <!--<iframe  allowvr="yes" scrolling="no" v-if="crt_view=='3d'" :src="read_3d" frameborder="0" width="100%" height="100%"></iframe>-->

             <div class="toogle-btn clickable" v-if="crt_view=='2d'" @click="crt_view='3d'">3D</div>
             <div class="toogle-btn clickable" v-if="crt_view=='3d'" @click="crt_view='2d'">2D</div>
    </div>`
})