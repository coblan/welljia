require('./scss/header_bar.scss')

Vue.component('com-fullhome-header-bar',{
    props:['top_heads'],
    template:` <div id="header-bar" class="com-fullhome-header-bar">

            <div class="header-bar" >
                <img class="center-v" src="/static/images/full_home_logo.png" alt="">
                <div  class="sm-right-top-panel center-v">
                    <component v-for="head in top_heads" :is="head.editor" :head="head"></component>
                </div>
            </div>
        </div>`
})