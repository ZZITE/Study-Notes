<template>
<!-- 导航hover框 -->
    <div class="navigate">
        <div class="cupernew">
            <ul style="float:left">
                <li v-for="(rgb,index) in rgbs" :key="index">
                    <a href="">
                        {{ rgb.namx }}
                    </a> 
                </li>
            </ul>
            <ul>
                <li v-for="(rgba,index) in rgbas" :key="index">
                    <a href="">
                        {{ rgba.maix }}
                    </a>
                </li>
            </ul>
            <div class="npmer">
                <a href="">
                    <img :src="urll" alt="">
                    <span>{{ lean }}</span>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return{
            urll: 'static/images/nvren.png',
            lean: 'Lace Up Back',
            rgbs: [
                { namx: 'New in Tody'},
                { namx: 'New in This Week'},
                { namx: 'Dresses'},
                { namx: 'Knitwear'},
                { namx: 'Tops'},
                { namx: 'Outerwear'},
                { namx: 'LlNEN CLOTH'},
                { namx: 'Bottoms'},
                { namx: 'Accessories'},
                { namx: 'Set'},
                { namx: 'Jewelry'},
            ],
            rgbas: [
                { maix: 'Handbags' },
                { maix: 'Jumpsuits'},
                { maix: '2017-09-05'},
                { maix: '2017-09-04'},
                { maix: '2017-09-03'},
                { maix: '2017-09-02'},
                { maix: '2017-09-01'},
                { maix: '2017-08-31'},
            ]
        }
    }
}
</script>

<style scoped> 
    .navigate {
        position: absolute;
        width: 100%;
        height: 470px;
        z-index: 10000;
        margin-top: 10px;
        background: #f5f5f5;
    }
    .cupernew {
        width: 1000px;
        height: 390px;
        margin: 0 auto;
        padding: 40px 40px;
        background: #fff;
    }
    .cupernew li {
        height: 36px;
    }
    .cupernew a {
        font-size: 12px;
    }
    .cupernew ul:nth-child(2) {
        float: left;
        margin-left: 200px;
    }
    .npmer span {
        position: relative;
        font-size: 14px;
        top: 320px;
        left: 290px;
        float: right;
    }
    .cupernew img {
        float: right;
    }
</style>