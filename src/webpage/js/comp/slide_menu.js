require('./scss/slide_menu.scss')

var slide_menu={
    props:['menu','toggleBtn','panel'],
    template:`<div>
    </div>`,
    mounted:function(){
        var self=this
        var slideout = new Slideout({
            'panel': $(self.panel)[0], //document.getElementById('main-panel'),
            'menu':  $(self.menu)[0] ,//document.getElementById('menu'),
            'padding': 256,
            'tolerance': 70,
            touch:false
        });

        $(self.toggleBtn).click( function() {
            slideout.toggle();
        });

        document.querySelector(self.menu).addEventListener('click', function(eve) {
            if (eve.target.nodeName === 'A') { slideout.close(); }
        });
        //$(self.menu).on('click','a',function(){
        //    console.log('hehee')
        //    slideout.close()
        //})

    }
}

Vue.component('com-slide-menu',slide_menu)
