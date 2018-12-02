Vue.component('com-fab-map',{
    template:`<div style="position: absolute;top:0;left: 0;right: 0;bottom: 0;">
    <canvas id="map" width="1921px" height="1007px"></canvas>
    </div>`,
    mounted:function(){
        var canvas = new fabric.Canvas('map',{
            //moveCursor:'move'
        });

        fabric.Image.fromURL('/static/images/sichuan.png', function(sunImg) {

            canvas.add(sunImg);
            sunImg.center();
            sunImg.set('selectable',false)
            sunImg.set('hoverCursor','default')
        });

        //canvas.setBackgroundImage('/static/images/sichuan.png')
        // create a rectangle object
        var rect = new fabric.Rect({
            left: 100,
            top: 100,
            fill: 'red',
            width: 20,
            height: 20,
        });
        canvas.add(rect);
        //rect.set('selectable',false)
        rect.set('hoverCursor','default')

        zoom_ctrl(canvas)


// "add" rectangle onto canvas

    }
})


function zoom_ctrl(canvas){
    canvas.on('mouse:wheel', function(opt) {
        var delta = opt.e.deltaY;
        var pointer = canvas.getPointer(opt.e);
        var zoom = canvas.getZoom();
        zoom = zoom + delta/200;
        if (zoom > 20) zoom = 20;
        if (zoom < 0.01) zoom = 0.01;
        canvas.zoomToPoint({ x: opt.e.offsetX, y: opt.e.offsetY }, zoom);
        opt.e.preventDefault();
        opt.e.stopPropagation();
    });

    canvas.on('mouse:down', function(opt) {
        var evt = opt.e;
        if (evt.altKey === true) {
            this.isDragging = true;
            this.selection = false;
            this.lastPosX = evt.clientX;
            this.lastPosY = evt.clientY;

        }
    });
    canvas.on('mouse:move', function(opt) {
        if (this.isDragging) {
            var e = opt.e;
            this.viewportTransform[4] += e.clientX - this.lastPosX;
            this.viewportTransform[5] += e.clientY - this.lastPosY;
            this.requestRenderAll();
            this.lastPosX = e.clientX;
            this.lastPosY = e.clientY;
        }
    });
    canvas.on('mouse:up', function(opt) {
        this.isDragging = false;
        this.selection = true;
    });
}