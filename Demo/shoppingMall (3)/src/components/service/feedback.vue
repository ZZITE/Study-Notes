<template>
<!-- 意见反馈 -->
    <div class="feedback">
        <h2>意见反馈</h2>
        <div class="feedback-main">
            <h3>发表咨询</h3>
            <p>声明：您可在购买前对产品包装、颜色、运输、库存等方面进行咨询，我们有专业进行回复！因厂家
                随时会更改一些产品包装、颜色、产地等参数，所以该回复仅在当时对提问者有效，其他网友仅供
                参考！咨询回复的工作时间为：周一至周五，9：00至18：00，请耐心等待工作人员回复。
            </p>
            <label for="">咨询内容：
                <input type="text">
            </label>
            <button class="buten"><em style="color:green;">√</em> 提交</button>
        </div>
        <p style="margin:20px 0 0 0;color:red;font-weight: bold;">您在购买前对产品包装、颜色、运输、库存等方面进行咨询，我们有专人进行回复。 </p>
    </div>
</template>

<script>
export default {

}
</script>

<style>
.feedback {
    padding: 10px 20px 10px 20px;
}
.feedback h2 {
    font-size: 18px;
    color: #e60211;
    height: 30px;
}
.feedback-main {
    width: 100%;
    height: 300px;
    border: 1px solid #E5E5E5;
}
.feedback-main h3 {
    margin: 10px 0 20px 20px;
}
.feedback-main p {
    margin: 10px 0 20px 30px;
}
.feedback-main label {
    float: left;
    margin: 0 0 0 30px;
    font-weight: bold;
}
.feedback-main input {
    width: 400px;
    padding-bottom: 100px;
}
.buten {
    position: relative;
    bottom: -130px;
    left: -405px;
    width: 68px;
    height: 30px;
    border: 0;
    outline: none;
    font-weight: bold;
    border: 1px solid #E5E5E5;
    background: #fbfbfb;
    border-radius: 10%;
}
.feedback-main button:active {
    background: #f4f3f3;
}
</style>
