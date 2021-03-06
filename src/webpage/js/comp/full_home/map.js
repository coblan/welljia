require('./scss/map.scss')

Vue.component('com-fullhome-map',{
    props:['map_points','area_list','image_list'],
    data:function(){
        return {
            env:cfg.env,
            el_width:100,
            normed_area_list:[],
            normed_map_points:[],
            normed_image_list:[],
            draw_loop_index:null,
            delay:150,
        }
    },
    mounted:function(){
        var self=this
        this.update_size()
        this.draw()
        // 防止图片没加载完，出现不能居中。
        $(this.$el).find('#bg-map')[0].onload(function(){
            self.update_size()
        })
    },
    watch:{
        'env.width':function(){
            this.update_size()
        },
        map_points:function(){
            this.stop_draw()
            this.draw()
        },
        area_list:function(){
            this.stop_draw()
            this.draw()
        },
        image_list:function(){
            this.stop_draw()
            this.draw()
        },
        //map_points:function(v){
        //    this.start_animation()
        //}
    },
    computed:{
        main_style:function(){
            var height = $(this.$el).height()
            var scale = height /1080
            return {
                transform:'scale('+scale+')'
            }
        },
        //size:function(){
        //    var com_height = this.$el? $(this.$el).height():this.el_width
        //    var com_width = this.$el? $(this.$el).width():this.el_width
        //    var win_ratio = this.env.width / this.env.height
        //    var img_ratio = 1921/1007
        //    if(this.env.width > 900){
        //        if(com_height * img_ratio >com_width){
        //            return {
        //                //width:'100%',
        //                //height:'auto',
        //                width:com_width+'px',
        //                height:com_width / img_ratio +'px'
        //            }
        //        }else{
        //            return{
        //                height: com_height+'px',
        //                width:com_height * img_ratio + 'px'
        //            }
        //        }
        //    }else {
        //        if(win_ratio > 1){
        //            // 横屏
        //            console.log('横屏')
        //            var out_height = com_height*1.6
        //            console.log(out_height)
        //
        //        }else{
        //            // 竖屏
        //            console.log('竖屏')
        //            var out_height = com_height*0.8
        //        }
        //        return {
        //            height: out_height+'px',
        //            width:out_height * img_ratio + 'px'
        //        }
        //    }
        //},
    },
    methods:{
        update_size:function(){
            // 使得背景地图水平居中
            var self=this
            var height = $(this.$el).height()
            var scale = height /1080
            var child_width = 1980 * scale
            $(this.$el).find('.map-wrap').css('transform','scale('+scale+')')

            var par_width = $(self.$el).width()
            if(child_width > par_width){
                setTimeout(function(){
                    $(self.$el).scrollLeft( (child_width - par_width)/2)
                },10)

            }
        },

        draw:function(){
            this.normed_area_list=[]
            this.normed_map_points=[]
            this.normed_image_list=[]
            this.draw_loop_index=null
            this.draw_area().then(this.draw_point).then(this.draw_image)
            console.log('draw')
        },
        stop_draw:function(){
            if(this.draw_loop_index){
                clearInterval(this.draw_loop_index)
                this.draw_loop_index=null
            }
        },
        draw_area:function(){
            var self=this
            var p = new Promise(function(resolve,reject){
                if(self.area_list.length==0){
                    resolve()
                    return
                }
                var index = 0
                self.draw_loop_index = setInterval(function(){
                    self.normed_area_list.push(self.area_list[index])
                    index+=1
                    if(index ==self.area_list.length){
                        clearInterval(self.draw_loop_index)
                        resolve()
                    }
                },self.delay)
            })
            return p
        },
        draw_point:function(){
            var self=this
            var p = new Promise(function(resolve,reject){
                if(self.map_points.length==0){
                    resolve()
                    return
                }
                var index = 0
                self.draw_loop_index = setInterval(function(){
                    self.normed_map_points.push(self.map_points[index])
                    index+=1
                    if(index ==self.map_points.length){
                        clearInterval( self.draw_loop_index)
                        resolve()
                    }
                },self.delay)
            })
            return p
        },
        draw_image:function(){
            var self=this

            var p = new Promise(function(resolve,reject){
                if(self.image_list.length==0){
                    resolve()
                    return
                }
                var index = 0
                self.draw_loop_index = setInterval(function(){
                    self.normed_image_list.push(self.image_list[index])
                    index+=1
                    if(index ==self.image_list.length){
                        clearInterval( self.draw_loop_index)
                        resolve()
                    }
                    console.log('draw image')
                },self.delay)
            })
            return p
        }
    },
    //1921/1007   no-scroll-bar
    template:`<div class="com-fullhome-map no-scroll-bar">

        <div class="map-wrap ">
        <img class="item" id="bg-map"  src="/static/images/1_1.jpg" alt="" >
             <!--<img class="sichuan" src="/static/images/sichuan.png" alt="">-->
             <transition-group name="fade">
                <com-fullhome-area class="item" v-for="area in normed_area_list" :key="'area_'+area.pk" :area="area" ></com-fullhome-area>

             </transition-group>
        <img class="item" style="left: 886px;top:297px" src="/static/images/text.png" alt="">
         <transition-group name="fade">
                <com-fullhome-pos class="item" v-for="pos in normed_map_points" :key="'pos_'+pos.pk" :mapitem="pos"></com-fullhome-pos>
                <com-fullhome-area class="item" v-for="img in normed_image_list" :key="'img_'+img.pk" :area="img" ></com-fullhome-area>
         </transition-group>
        </div>

    </div>`
})

Vue.component('com-fullhome-area',{
    props:['area','scale'],
    template:`<div class="com-fullhome-area" :style="area_style">
        <img @click="jump_link()" :class="{clickable:area.link}" :src="area.pic" alt="">
    </div>`,
    computed:{
        area_style:function(){
            var self=this
            var out_ls=this.area.pos.split(',')
            //var out_ls= ex.map(ls,function(ss){
            //    return ss* self.scale
            //})
            //var width = this.area.width * self.scale
            return {
                position:'absolute',
                top:out_ls[1]+'px',
                left:out_ls[0]+'px',
                //width:width+'px'
            }
        }
    },
    methods:{
        jump_link:function(){
            if(this.area.link){
                location = this.area.link
            }
        }
    }
})

Vue.component('com-fullhome-pos',{
    props:['mapitem'],
    data:function(){
        return {
            is_show:true,
            show_info:false,
            parStore:ex.vueParStore(this)
        }
    },
    //@mouseleave="is_show=false"
    template:`<div :class="['com-fullhome-pos',{'show':is_show,clickable:mapitem.url}]" :style="{top:loc.y,left:loc.x}"
         @click="open_page()">
          <div >
                <div class="glow"></div>
                <img class="point" src="/static/images/4.png" alt="">
          </div>

       <div class="circle" >
                <img style="width: 100%;height: 100%" src="/static/images/4_4.png" alt="">
       </div>

    </div>`,

    computed:{
        loc:function(){
            var self=this
            var out_ls=this.mapitem.pos.split(',')
            //var out_ls= ex.map(ls,function(ss){
            //   return ss* self.scale
            //})
            return {
                x:out_ls[0] +'px',
                y:out_ls[1]+'px'
            }
        },
    },
    methods:{
        open_page:function(){
            if(this.mapitem.direct_url){
                location = this.mapitem.direct_url
            }else if(this.mapitem.url){
                var url =ex.appendSearch('/digital',{
                    projg:this.parStore.crt_proj.pk,
                    builds:this.mapitem.pk
                })
                location =url
            }

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