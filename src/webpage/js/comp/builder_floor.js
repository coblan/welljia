require('./scss/builder_floor.scss')

Vue.component('com-builder-floor',{
    props:['building'],
    template:`<div class="com-builder-floor clickable flex-v">
          <div class="big-title"><h5 v-text="building.label"></h5></div>
          <div class="floors flex-grow">
            <div v-for="floor in building.floors" :class="['floor flex',floor.status]">
                <div style="color: #a3a3a3;padding-left: 8px"> <i class="fa fa-home"></i></div>
                <span class="flex-grow" v-text="floor.label"></span>
                <span style="display: inline-block;margin-left: 1em;">
                    <button @click="show_2d(floor.img_2d)">2D</button>
                    <button @click="show_3d(floor.img_3d)">3D</button>
                </span>

            </div>
          </div>
    </div>`,
    methods:{
        show_2d:function(img_url){
            //layer.open({
            //    type: 2,
            //    title: false,
            //    shadeClose: true,
            //    shade: 0.8,
            //    area: ['90%', '90%'],
            //    content: img_url //iframe的url
            //});
            var ctx={
                img_url:img_url
            }
            pop_layer(ctx,'com-img-shower',function(){},{
                title:false,
                area: ['90%', '90%'],
                shade: 0.8,
                shadeClose: true,
            })
        },
        show_3d:function(img_url){
            layer.open({
                type: 2,
                title: false,
                shadeClose: true,
                shade: 0.8,
                area: ['90%', '90%'],
                content: img_url //iframe的url
            });
        }

    }
})

Vue.component('com-img-shower',{
    props:['com_ctx'],
    template:`<div  style="position: absolute;top:0;left: 0;bottom: 0;right: 0;background-color: grey">
        <div class="center-vh">
            <img :src="com_ctx.img_url" style="max-width: 100%;max-height: 100%" alt="">
        </div>

    </div>`
})