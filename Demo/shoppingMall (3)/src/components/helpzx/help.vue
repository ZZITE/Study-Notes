<template>
<!-- 帮助中心 -->
    <div class="help">
        <!-- 侧边 -->
        <div class="help-nav">
            <ul>
                <div style="height:25px;line-height:25px;color:#e54c87;font-size:14px;text-align:center;background:#F6F6F6;border-bottom:1px solid #E5E5E5;">
                    购买指南
                </div>
                <li v-for="(rnb,index) in rnbs" :key="index">
                    <router-link :to="rnb.to">
                        {{rnb.text}}
                    </router-link>
                </li>
            </ul>
            <ul>
                <div style="height:25px;line-height:25px;color:#e54c87;font-size:14px;text-align:center;background:#F6F6F6;border-bottom:1px solid #E5E5E5;border-top:1px solid #E5E5E5;margin:50px 0 0 0;">
                    支付与配送
                </div>
                <li v-for="(rgb,index) in rgbs" :key="index">
                    <router-link :to="rgb.to">
                        {{rgb.text}}
                    </router-link>
                </li>
            </ul>
            <ul>
                <div style="height:25px;line-height:25px;color:#e54c87;font-size:14px;text-align:center;background:#F6F6F6;border-bottom:1px solid #E5E5E5;border-top:1px solid #E5E5E5;margin:50px 0 0 0;">
                    服务体系
                </div>
                <li v-for="(ser,index) in sers" :key="index">
                    <router-link :to="ser.to">
                        {{ ser.text }}
                    </router-link>
                </li>
            </ul>
            <ul>
                <div style="height:25px;line-height:25px;color:#e54c87;font-size:14px;text-align:center;background:#F6F6F6;border-bottom:1px solid #E5E5E5;border-top:1px solid #E5E5E5;margin:50px 0 0 0;">
                    公司信息
                </div>
                <li v-for="(web,index) in webs" :key="index">
                    <router-link :to="web.to">
                        {{ web.text }}
                    </router-link>
                </li>
            </ul>
        </div>
        <!-- 主题内容 -->
        <div class="help-main">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return{
            // 第一行导航
            rnbs: [
                { text: '注册流程', to:'/help/registration-process' },
                { text: '购买流程', to:'/help/Purchase-process'},
                { text: '常见问题', to:'/help/common-problem' },
                { text: '商品组成', to:'/help/Commodity-composition' },
            ],
            // 第二行导航
            rgbs: [
                { text: '配送方式', to:'/help/Delivery-Method' },
                { text: '支付方式', to:'/help/payment-method' },
                { text: '快递查询', to:'/help/Express-inquiry' }
            ],
            // 第三行导航
            sers: [
                { text: '会员介绍', to:'/help/Member-introduction' },
                { text: '意见反馈', to:'/help/Feedback' },
                { text: '服务承诺', to:'/help/Pledge' },
            ],
            // 第四导航
            webs: [
                { text: '关于我们', to:'/help/about' },
                { text: '联系我们', to:'/help/contact' },
                { text: '条款和条件', to:'/help/Terms-Conditions' },
                { text: '隐私政策', to:'/help/Privacy-Policy' }
            ]
        }
    }
}
</script>

<style>
.help {
    width: 1080px;
    height: 800px;
    margin: 30px auto;
    /* background: skyblue; */
}
.help-nav {
    float:left;
    width:168px;
    height:998px;
    background: white;
    border: 1px solid #dedede;
}
.help-main {
    float: left;
    width: 898px;
    margin-left: 10px;
    margin-bottom: 20px;
    border: 1px solid #dedede;
}
.help-nav li {
    text-align: center;
    font-size: 14px;
    margin-top: 15px;
    border-bottom: 1px dashed #E5E5E5;
}
.help li:hover {
    background: #E5E5E5;
}
</style>
