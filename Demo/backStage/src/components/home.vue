<template>
<!-- 主引入页 -->
    <div style="float:left;width:100%;height:100%;" class="wrapper">
        <div class="menuWrap">
        <v-sidebar></v-sidebar>
        </div>
        <div class="appWrap">
            <transition name="fade">
                <keep-alive>
                <router-view class="routerView"></router-view>
                </keep-alive>
            </transition>
        </div>
    </div>
</template>

<script>
    import vSidebar from '@/components/downmenu.vue';
    export default {
        components:{
            vSidebar
        }
    }
</script>
<style>
.appWrap {
    height: 100%;
    margin-left: 260px;
    min-width:1366px;
}
.menuWrap {
    height: 100%;
    float: left;
    width: 260px;
}

.fold-enter-active, .fold-leave-active {
    transition: all .5s;
}
.fold-enter, .fold-leave-active {
    transform: translate3d(0, 0, 0);
}
</style>
