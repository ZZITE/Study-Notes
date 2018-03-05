import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
	routes: [
		{
			path: '/',
			name: 'Home',
			component: resolve => require(['@/page/home'], resolve),		
		},
		{
			path: '/Login',
			name: 'login',
			component: resolve => require(['@/page/login'], resolve),				
		},
		{
			path: '/Product/:id',
			name: 'productList',
			component: resolve => require(['@/page/productList'], resolve),						
		},
		{
		path: '/My',
		component: resolve => require(['@/page/myPage/my'], resolve),		
		redirect: '/My/Profile',
		children: [
			{
				path: '/My/Profile',
				name: 'my',
				component: resolve => require(['@/page/myPage/profile'], resolve),		
			},
			{
				path: '/My/Orders',
				component: resolve => require(['@/page/myPage/orders'], resolve),									
			},
			{
				path: '/My/Favorites',
				name: '',
				component: resolve => require(['@/page/myPage/favorites'], resolve),			
			},
			{
				path: '/My/Changepwd',
				name: '',
				component: resolve => require(['@/page/myPage/changepwd'], resolve)
			},
			{
				path: '/My/Following',
				name: '',
				component: resolve => require(['@/page/myPage/following'], resolve)
			},
			{
				path: '/My/Orders/Detail',
				name: 'Orders',
				component: resolve => require(['@/page/myPage/orDetail'], resolve),
			},
			{
				path: '/My/Orders/Withdraw',
				name: 'withdraw',
				component: resolve => require(['@/page/myPage/withdraw'], resolve),			
			},
			{
				path: '/My/About',
				name: 'about',
				component: resolve => require(['@/page/myPage/about'], resolve),		
			},
			{
				path: '/My/Contact',
				name: 'contact',
				component: resolve => require(['@/page/myPage/contact'], resolve),		
			},
			{
				path: '/My/Coupon',
				name: 'coupon',
				component: resolve => require(['@/page/myPage/coupon'], resolve),		
			},
			{
				path: '/My/Service',
				name: 'service',
				component: resolve => require(['@/page/myPage/service'], resolve),	
			}
		]
		},
		{
			path: '/Designers',
			name: 'designers',
			component: resolve => require(['@/page/Designers/designers'], resolve)
		},
		{
			path: '/Designers/detail',
			name: 'Detail',
			component: resolve => require(['@/page/Designers/deDetail'], resolve)
		},
		{
			path: '/NEWIN',
			name: 'newin',
			component: resolve => require(['@/page/newin'], resolve)
		},
		{
			path: '/Cart',
			name: 'cart',
			component: resolve => require(['@/page/cart'], resolve)
		},
		{
			path: '/Payment',
			name: 'payment',
			component: resolve => require(['@/page/payment'], resolve)
		},
		{
			path: '/Goods',
			name: 'goods',
			component: resolve => require(['@/page/goods'], resolve)
		},
		{
			path: '/resetpassword',
			name: 'reset',
			component: resolve => require(['@/page/resetpassword'], resolve)
		},
		{
			path: '/transfer',
			name: 'transfer',
			component: resolve => require(['@/page/transfer'], resolve)
		},
		{
			path: '/help',
			name: 'help',
			component: resolve => require(['@/components/helpzx/help'], resolve),
			children: [
				{
					path: '/help/registration-process',
					name: '',
					component: resolve => require(['@/components/helpzx/register.vue'], resolve),          
				},
				{
					path: '/help/Purchase-process',
					name: '',
					component: resolve => require(['@/components/helpzx/purchase.vue'], resolve),          
				},
				{
					path: '/help/common-problem',
					name: '',
					component: resolve => require(['@/components/helpzx/problem.vue'], resolve),          
				},
				{
					path: '/help/Commodity-composition',
					name: '',
					component: resolve => require(['@/components/helpzx/commodity.vue'], resolve),          
				},
				{
					path: '/help/Delivery-Method',
					name: '',
					component: resolve => require(['@/components/paydis/distribution.vue'], resolve)
				},
				{
					path: '/help/payment-method',
					name: '',
					component: resolve => require(['@/components/paydis/payment.vue'], resolve)
				},
				{
					path: '/help/Express-inquiry',
					name: '',
					component: resolve => require(['@/components/paydis/lookup.vue'], resolve)
				},
				{
					path: '/help/Member-introduction',
					name: '',
					component: resolve => require(['@/components/service/member.vue'], resolve)
				},
				{
					path: '/help/Feedback',
					name: '',
					component: resolve => require(['@/components/service/feedback.vue'], resolve)
				},
				{
					path: '/help/Pledge',
					name: '',
					component: resolve => require(['@/components/service/Promise.vue'], resolve)
				},
				{
					path: '/help/about',
					name: '',
					component: resolve => require(['@/components/information/About.vue'], resolve)
				},
				{
					path: '/help/contact',
					name: '',
					component: resolve => require(['@/components/information/Contact.vue'], resolve)
				},
				{
					path: '/help/Terms-Conditions',
					name: '',
					component: resolve => require(['@/components/information/clause.vue'], resolve)
				},
				{
					path: '/help/Privacy-Policy',
					name: '',
					component: resolve => require(['@/components/information/Privacy.vue'], resolve)
				},
			]
		}
	]
})
