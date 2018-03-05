<template>
    <div style="width:600px;margin:0 auto;">
      <div style="float:right;margin-right:30px;margin-top:20px;">
        <button @click="add2" style="width:20px;height:70px;">添加列</button>
      </div>
    <table border=1 width=250 align=center style="height:200;overflow:scroll;">
      <caption @click="tt">【表格】</caption>
      <tr bgcolor="#F6F6F6">
        <!-- 表头 -->
        <th v-for="(head, index) in tableData.th" :key="index" @click="inputshow = index;tableData.th[index] = '';">
          <p v-if="inputshow !== index">{{head}}</p>
          <input type="text" v-model="tableData.th[index]" v-if="inputshow == index" @blur="inputshow = -1">
        </th>
      </tr>
        <!-- 表格内容 -->
      <tr v-for="(i, todo) in tableData.tbody" :key="todo" align=center>
        <td v-for="(j, index) in i.context" :key="index" @click="inputshow2 = index;inputshow3 = todo;tableData.tbody[todo].context[index] =''">
          <p v-if="inputshow2 !== index || inputshow3 !== todo">{{j}}</p>
          <input type="text" v-model="tableData.tbody[todo].context[index]" v-if="inputshow2 == index && inputshow3 == todo" @blur="inputshow2 = -1;inputshow3 = -1">
        </td>
      </tr>

      </table>
      
      <div style="vertical-align: middle;">
        <button @click="add" style="margin:20px auto; width:70px;height:20px">添加行</button>
      </div>

    </div>
</template>
<script>
export default {
  data () {
    return {
      thshow: true,
      inputshow: -1,
      inputshow2: -1,
      inputshow3: -1,
      tableData: {
        th: ['名称/尺寸'],
        tbody: [
        ]
      }
    }
  },
  methods: {
    add: function () {
      var cc = []
      cc.length = this.tableData.th.length
      for (var i = 0; i < cc.length; i++) {
        cc[i] = '默认'
      }
      this.tableData.tbody.push({
        context: cc
      })
    },
    add2: function () {
      this.tableData.th.push('默认')
      for (var i = 0; i < this.tableData.tbody.length; i ++) {
        console.log(1)
          this.tableData.tbody[i].context.push('默认')
      }
    },
    tt: function () {
      console.log(this.tableData)
    }
  }
}
</script>

<style scoped>

table {
  border-collapse:collapse;
  width: 500px;
  height: 100%;
}
caption, th {
  text-align: center;
}
td,th{
  width: 100px;
  height: 40px;
}
input {
  width: 48px;
  height: 20px;
}
td:first-child {
  background: #F6F6F6;
}
button {
  display:block;
  border: 1px solid #E54C87;
  background:#fff;
  color:#E54C87;
}
button:focus {
  border: none;
}

</style>
