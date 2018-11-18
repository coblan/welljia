require('./scss/com_login_banner.scss')
var com_login_banner={
    template:` <div class="com-login-banner" >
            <h3 style="line-height:200%"><span style="margin: 0 2rem"><img src="/static/images/log.png" alt=""></span>
            <span style="white-space: nowrap">欢迎注册威尔佳用户</span></h3>
        </div>`,
}

Vue.component('com-login-banner',com_login_banner)