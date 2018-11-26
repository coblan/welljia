require('./scss/map.scss')

Vue.component('com-fullhome-map',{
    props:['map_points'],
    data:function(){
        return {
            env:cfg.env,
            el_width:100,
        }
    },
    mounted:function(){
        this.el_width = $(this.$el).height()
    },
    computed:{
        size:function(){
            console.log('ri')
            var com_height = this.$el? $(this.$el).height():this.el_width
            var win_ratio = this.env.width / this.env.height
            var img_ratio = 1921/1007
            if(this.env.width > 900){
                //return {
                //    maxWidth:'100%',
                //    maxHeight:'100%',
                //}
               if(com_height * img_ratio >this.env.width){
                   return {
                       width:this.env.width+'px',
                       height:this.env.width / img_ratio +'px'
                   }
               }else{
                   return{
                       height: com_height+'px',
                       width:com_height * img_ratio + 'px'
                   }
               }


            }else {
                if(win_ratio > 1){
                    // 横屏
                    console.log('横屏')
                    var out_height = com_height*1.6
                    console.log(out_height)

                }else{
                    // 竖屏
                    console.log('竖屏')
                    var out_height = com_height*0.8
                }
                return {
                    height: out_height+'px',
                    width:out_height * img_ratio + 'px'
                }
            }


        }
    },
    //1921/1007
    template:`<div class="com-fullhome-map">
        <div class="map-wrap center-vh" :style="size">
             <!--<img class="sichuan" src="/static/images/sichuan.png" alt="">-->
             <com-fullhome-pos v-for="pos in map_points" :mapitem="pos" :scale="parseInt(size.width)/1921"></com-fullhome-pos>
        </div>
    </div>`
})

Vue.component('com-fullhome-pos',{
    props:['mapitem','scale'],
    template:`<div class="com-fullhome-pos" :style="{top:loc.y,left:loc.x}" @click="open_page()">
    <img class="point" src="/static/images/4.png" alt="">
    <span class="title" >
    <img class="icon" :src="mapitem.icon" alt=""><span v-text="mapitem.title"></span>
    </span>
    </div>`,
    computed:{
        loc:function(){
            var self=this
            var ls=this.mapitem.pos.split(',')
            var out_ls= ex.map(ls,function(ss){
               return ss* self.scale
            })
            return {
                x:out_ls[0] +'px',
                y:out_ls[1]+'px'
            }
        }
    },
    methods:{
        open_page:function(){
            console.log('jj')
            location = this.mapitem.url
        }
    }
})