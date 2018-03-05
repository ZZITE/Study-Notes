## PayPal

### PayPal WebProfile　API

使用这个`WebProfile API`的原因是：在完成`Payment`跳转支付后，发现在支付页面会出现
一个"Ship to"的选项(让用户选择发货地址)，这个东西让人很烦。为什么呢？
因为本站已经让用户输入过地址，结果付款页面又出现一个，麻烦不说，很容易把用户搞糊涂，影响
用户体验，以至于影响销量.

WebProfile全称"**Web experience profiles**"。作为商家，你可以使用
`WebProfile API`来自定义用户支付流程的体验。你可以创建多与产品无关(product-agnostic)
的web体验界面。

想要将自定义webprofile集成到你的支付应用中，需要如下步骤:

1. 完成必须的前置条件[https://developer.paypal.com/docs/integration/direct/payment-experience/#prerequisites-pe]
    (https://developer.paypal.com/docs/integration/direct/payment-experience/#prerequisites-pe)
2. 创建web experience profile

    必须为你的每个profile以一个唯一的名称(name)来创建.
    
3. 在PayPal Payment中使用`experience_profile_id`

4. 获取消费者验证url


### 处理PayPal支付

PayPal SDK需要依赖以下的系统库:

- libssl-dev
- libffi-dev

在debian系统下面可以这么安装：

`apt-get install libssl-dev libffi-dev`


1. 建立payment信息对象(`paypalrestsdk.Payment`)

    这个`Payment`对象包含:支付方法，交易细节，在PayPal接受支付之后把用户重定向到哪里
    等等信息...，处理支付从创建这个对象开始.
    
    想要创建PayPal支付，需要把`payer`下面的`payment_method`参数设置为`paypal`.
    
    [Payment对象的详细API文档](https://developer.paypal.com/docs/api/payments/)
    

2. 初始化payment，以及用户的重定向

    对于`Payment`对象集合，你可以在PayPal初始化它们。在你发送request创建一个
    `Payment`之后，PayPal将会返回一个JSON Response，这个response包含一个
    `links`对象(这个对象包含`approval_url`)，这两个数据用来指明应该把消费者
    重定向的位置，然后消费者就可以选择验证或者取消`Payment`了.
    
    调用`Payment.create()`之后，将会把你上一步创建的支付信息发送请求(request)。
    如果这个request成功，就可以提取出`approval_url`，然后可以把用户重定向到PayPal
    的URL来验证这个支付信息.
    
3. 完成支付

   在消费者确认支付信息以后，他将会被重定向到第一步中Payment对象指定的URL.在
   这个URL的`query string`中，将会包含两个参数，`PayerID`和`paymentId`。
   这两个参数用来确认支付的完成情况.
   


## 后台 {
    https://www.niceline.com/a4min/login
    username: nice1
    password: sdi37f723rwER2
}