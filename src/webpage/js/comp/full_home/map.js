require('./scss/map.scss')

Vue.component('com-fullhome-map',{
    props:['map_points','area_list'],
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
            var com_height = this.$el? $(this.$el).height():this.el_width
            var com_width = this.$el? $(this.$el).width():this.el_width
            var win_ratio = this.env.width / this.env.height
            var img_ratio = 1921/1007
            if(this.env.width > 900){
                if(com_height * img_ratio >com_width){
                    return {
                        //width:'100%',
                        //height:'auto',
                        width:com_width+'px',
                        height:com_width / img_ratio +'px'
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
        },
    },
    //1921/1007
    template:`<div class="com-fullhome-map">
        <div class="map-wrap center-vh" :style="size">
             <!--<img class="sichuan" src="/static/images/sichuan.png" alt="">-->
             <transition-group name="fade">
                <com-fullhome-area v-for="area in area_list" :key="area.pk" :area="area" :scale="parseInt(size.width)/1921"></com-fullhome-area>
                <com-fullhome-pos v-for="pos in map_points" :key="pos.pk" :mapitem="pos" :scale="parseInt(size.width)/1921"></com-fullhome-pos>
  </transition-group>

        </div>
    </div>`
})

Vue.component('com-fullhome-area',{
    props:['area','scale'],
    template:`<div :style="area_style">
        <img style="width:100%" :src="area.pic" alt="">
    </div>`,
    computed:{
        area_style:function(){
            var self=this
            var ls=this.area.pos.split(',')
            var out_ls= ex.map(ls,function(ss){
                return ss* self.scale
            })
            var width = this.area.width * self.scale
            return {
                position:'absolute',
                top:out_ls[1]+'px',
                left:out_ls[0]+'px',
                width:width+'px'
            }
        }
    }
})
Vue.component('com-fullhome-pos',{
    props:['mapitem','scale'],
    data:function(){
        return {
            is_show:true,
            show_info:false,
        }
    },
    //@mouseleave="is_show=false"
    template:`<div :class="['com-fullhome-pos',{'show':is_show,}]" :style="{top:loc.y,left:loc.x}"
         @click="open_page()">
    <img class="point" src="/static/images/4.png" alt="">

    <div class="line" :style="line_block_style">
        <canvas style="width: 100%;height: 100%" :width="line_block_style.num_width" :height="line_block_style.num_height"   ></canvas>
    </div>

    <transition name="fade">
    <div v-show="show_info">
           <div class="line" :style="line_end_style">
            </div >

            <span class="title" :style="{top:label_loc.y,left:label_loc.x}">
                <img class="icon" :src="mapitem.icon" alt=""><span v-text="mapitem.title"></span>
            </span>
    </div>

    </transition>
       <div class="circle" @mouseenter="is_show=true">
                <img style="width: 100%;height: 100%" src="/static/images/4_4.png" alt="">
            </div>

    </div>`,

    mounted:function(){
        this.draw_line()
        var self=this
        self.show_info=false
        setTimeout(function(){
            self.show_info=true
        },1000)
    },

    watch:{
        line_block_style:function(v){
            this.draw_line()
            var self=this
            self.show_info=false
            setTimeout(function(){
                self.show_info=true
            },1000)
        }
    },
    computed:{
        line_end_pos:function(){
            var self=this
            var ls=this.mapitem.label_pos.split(',')
            var out_ls= ex.map(ls,function(ss){
                return ss* self.scale
            })
            return {
                x:out_ls[0] -10,
                y:out_ls[1]+8
            }
        },
        line_end_style:function(){
            if(this.line_end_pos.y<0){
                var top = this.line_end_pos.y -1
            }else{
                var top = this.line_end_pos.y -2
            }
            return {
                position:'absolute',
                top:top+'px',
                left:this.line_end_pos.x+'px',
                width:'4px',
                height:'4px',
                borderRadius:'2px',
                backgroundColor:'white'
            }
        },
        line_block_style:function(){

            var org_x=15
            var org_y=15
            var label_x = this.line_end_pos.x
            var label_y = this.line_end_pos.y

            var top = Math.min(org_y,label_y)
            var height=Math.abs(org_y-label_y)
            var left = Math.min(org_x,label_x)
            var width=Math.abs(org_x-label_x)
            //if(this.ctx){
            //    this.ctx.scale(width/100,height/100)
            //}


            var dc ={
                position:'absolute',
                top:top+'px',
                height:height+'px',
                left:left+'px',
                width:width+'px',
                num_height:height,
                num_width:width,
            }

            //if(org_y <label_y ){
            //    dc['borderBottom']='1px solid #ededed'
            //}else{
            //    dc['borderTop'] = '1px solid #ededed'
            //}
            //
            //dc['borderLeft']='1px solid #ededed'

            return dc
        },
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
        },
        label_loc:function(){
            var self=this
            var ls=this.mapitem.label_pos.split(',')
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
        },
        draw_line:function(){
            var self=this
            setTimeout(function(){
                var canvas1=$(self.$el).find('canvas')[0];
                //获得2维绘图的上下文
                var ctx=canvas1.getContext("2d");
                var endpos = self.line_end_pos
                //设置线宽
                ctx.lineWidth=2;
                //设置线的颜色
                ctx.strokeStyle="#ededed";
                if(endpos.x > 0){
                    var start_x =0
                    var end_x = canvas1.width
                }else{
                    var start_x =-canvas1.width
                    var end_x = 0
                }
                if(endpos.y>0){
                    var start_y =0
                    var end_y = canvas1.height
                }else {
                    var start_y=  canvas1.height
                    var end_y =0
                }
                console.log(start_x,start_y)
                console.log(end_x,end_y)

                //将画笔移动到00点
                var length = end_x + end_y
                var step = length /50

                ctx.moveTo(start_x,start_y);

                function draw_y(callback){
                    var last_y = start_y
                    var direction = Math.sign(end_y - start_y)
                    var yd= setInterval(function(){
                        last_y += direction * step
                        if(direction == 1){
                            if(last_y>end_y){
                                ctx.lineTo(start_x,end_y);
                                ctx.stroke();
                                clearInterval(yd)
                                callback()
                            }else{
                                ctx.lineTo(start_x,last_y);
                                ctx.stroke();
                            }
                        }else{
                            if(last_y < end_y){
                                ctx.lineTo(start_x,end_y);
                                ctx.stroke();
                                clearInterval(yd)
                                callback()
                            }else {
                                ctx.lineTo(start_x,last_y);
                                ctx.stroke();
                            }
                        }
                    },20)
                }

                function draw_x(){
                    var last_x = start_x
                    var direction = Math.sign(end_x - start_x)
                    var xd= setInterval(function(){
                        last_x += direction * step
                        if(direction == 1){
                            if(last_x>end_x){
                                clearInterval(xd)
                                ctx.lineTo(end_x,end_y);
                                ctx.stroke();
                            }else{
                                ctx.lineTo(last_x,end_y);
                                ctx.stroke();
                            }
                        }else{
                            if(last_x < end_x){
                                clearInterval(xd)
                                ctx.lineTo(end_x,end_y);
                                ctx.stroke();
                            }else {
                                ctx.lineTo(last_x,end_y);
                                ctx.stroke();
                            }
                        }
                    },20)
                }


                draw_y(draw_x)





                //画线到800，600的坐标
                //ctx.lineTo(start_x,end_y);
                //ctx.lineTo(end_x,end_y)

                //执行画线

            },10)
        }
    }
})