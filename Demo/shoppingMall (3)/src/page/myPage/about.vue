<template>
<!-- 问答 -->
    <div class="answer">
        <h1>{{ about }}</h1>
        <div class="answer-main">
            <ul>
                <li v-for="(i,index) in them" :key="index">
                    <h2>{{ i.answer }}</h2>
                    <p>{{ i.anwper }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            about: 'About',
            them: [
                {
                answer: 'Fashion Designer’s Dilemma',
                anwper: 'Opening your own boutique or starting a fashion business is a dream of every inspired fashion designer. It soundswonderful to curate a store full of items that bears your label and connectwith customers who adore your designs, all while maintaining working hours thatfit in with your lifestyle.'
                },
                {
                answer: 'Fashion Designer’s Dilemma',
                anwper: 'Opening your own boutique or starting a fashion business is a dream of every inspired fashion designer. It soundswonderful to curate a store full of items that bears your label and connectwith customers who adore your designs, all while maintaining working hours thatfit in with your lifestyle.'
                }   
            ]
        }
    }
}
</script>

<style>
.answer {
    width: 860px;
    height: 421px;
    margin: 0 auto;
}
.answer h1 {
    width: 100%;
    margin-top: -20px;
    font-size: 16px;
    color: #0f0f0f;
    height: 30px;
    border-bottom: 1px solid #B7B7B7;
}
.answer-main {
    width: 860px;
    height: 370px;
    margin-top: 20px;
}
.answer-main h2 {
    font-size: 14px;
    margin-bottom: 6px;
    color: #030303;
}
.answer-main li {
    margin-top: 30px;
} 
</style>