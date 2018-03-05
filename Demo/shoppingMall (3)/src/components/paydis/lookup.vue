<template>
<!-- 快递查询 -->
    <div class="lookup">
        <img style="width:898px;" src="static/images/diqiu.png" alt="">
        <div class="posit">
            <input type="text">
            <button>search</button>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
.posit {
    position: relative;
    bottom: 350px;
    left: 250px;
}
.posit input {
    width: 300px;
    height: 30px;
}
.lookup img {
    opacity: 0.5;
}
.posit button {
    width: 68px;
    height: 34px;
    border: 0;
    margin-left: 20px;
    outline: none;
    color: white;
    background: #f85292;
}
.posit button:active {
    background: #E54C87;
}
</style>
