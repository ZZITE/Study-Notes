# 使用 Hooks 编写 React Components 时常见的五个错误

[原文链接](https://www.lorenzweiss.de/common_mistakes_react_hooks/)

## 在不需要重新渲染的情况下使用 useState

代码示例

```javascript
function ClickButton(props) {
	const [count, setCount] = useState(0);

	const onClickCount = () => {
		setCount((c) => c + 1);
	};

	const onClickRequest = () => {
		apiCall(count);
	};

	return (
		<div>
			<button onClick={onClickCount}>Counter</button>
			<button onClick={onClickRequest}>Submit</button>
		</div>
	);
}
```

### 问题

useState 造成了不必要的重复渲染，每次设置计数器都重新渲染

### 解决方案

如果你想在你的组件中使用一个变量，它应该在渲染之间保持它的值，但也不强迫重新渲染，你可以使用 useRef。它将保持值，但不会强制组件重新渲染。

```javascript
function ClickButton(props) {
	const count = useRef(0);

	const onClickCount = () => {
		count.current++;
	};

	const onClickRequest = () => {
		apiCall(count.current);
	};

	return (
		<div>
			<button onClick={onClickCount}>Counter</button>
			<button onClick={onClickRequest}>Submit</button>
		</div>
	);
}
```

## 使用 router.push 代替 a link

```javascript
function ClickButton(props) {
	const history = useHistory();

	const onClick = () => {
		history.push('/next-page');
	};

	return <button onClick={onClick}>Go to next page</button>;
}
```

### 问题

可访问性差，无法被阅读器识别，无法在新的标签页或窗口打开

### 解决方法

使用<Link>或者普通的<a>标签

```javascript
function ClickButton(props) {
	return (
		<Link to='/next-page'>
			<span>Go to next page</span>
		</Link>
	);
}
```

## 经由 useEffect 处理行为

一个组件接收 onSuccess，在请求完列表后执行

```javascript
function DataList({ onSuccess }) {
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState(null);
	const [data, setData] = useState(null);

	const fetchData = () => {
		setLoading(true);
		callApi()
			.then((res) => setData(res))
			.catch((err) => setError(err))
			.finally(() => setLoading(false));
	};

	useEffect(() => {
		fetchData();
	}, []);

	useEffect(() => {
		if (!loading && !error && data) {
			onSuccess();
		}
	}, [loading, error, data, onSuccess]);

	return <div>Data: {data}</div>;
}
```

### 问题

当不存在 Loading error 且有状态在 data 中的时候，可能意外的触发 onSuccess

### 解决方法

```javascript
function DataList({ onSuccess }) {
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState(null);
	const [data, setData] = useState(null);

	const fetchData = () => {
		setLoading(true);
		callApi()
			.then((fetchedData) => {
				setData(fetchedData);
				onSuccess();
			})
			.catch((err) => setError(err))
			.finally(() => setLoading(false));
	};

	useEffect(() => {
		fetchData();
	}, []);

	return <div>{data}</div>;
}
```

只在 api 调用成功时会触发 onSuccess

## 单一责任组件

如何组建组件，构造组件树。在设计组件时，一个常见的错误是把两个用例合成为一个组件。

```javascript
function Header({ menuItems }) {
	return (
		<header>
			<HeaderInner menuItems={menuItems} />
		</header>
	);
}

function HeaderInner({ menuItems }) {
	return isMobile() ? (
		<BurgerButton menuItems={menuItems} />
	) : (
		<Tabs tabData={menuItems} />
	);
}
```

### 问题

HeaderLnner 组件试图成为两个东西。同时成为一个以上的东西并不理想。另外也使得测试和复用组件变的更加的困难。

### 解决方法

```javascript
function Header(props) {
	return (
		<header>
			{isMobile() ? (
				<BurgerButton menuItems={menuItems} />
			) : (
				<Tabs tabData={menuItems} />
			)}
		</header>
	);
}
```

## 单一责任的 useEffects

想象一下你有一个组件，通过某种方式从后端获取一些数据，并且依赖当前的地址展示一个面包屑。

```javascript
function Example(props) {
	const location = useLocation();

	const fetchData = () => {
		/*  Calling the api */
	};

	const updateBreadcrumbs = () => {
		/* Updating the breadcrumbs*/
	};

	useEffect(() => {
		fetchData();
		updateBreadcrumbs();
	}, [location.pathname]);

	return (
		<div>
			<BreadCrumbs />
		</div>
	);
}
```

### 问题

这是 2 个用例，"data-fetching"和"displaying breadcrumbs"同时通过 useEffect hook 来更新。这个单一的 useEffect hook 将在 fetchData 和 updateBreadcrumbs 函数或 location 改变时运行。现在的主要问题是，当 location 改变时，我们也会调用 fetchData 函数。这可能是一个我们没有想到的副作用。

### 解决方法

```javascript
function Example(props) {
	const location = useLocation();

	const updateBreadcrumbs = () => {
		/* Updating the breadcrumbs*/
	};

	useEffect(() => {
		updateBreadcrumbs();
	}, [location.pathname]);

	const fetchData = () => {
		/*  Calling the api */
	};

	useEffect(() => {
		fetchData();
	}, []);

	return (
		<div>
			<BreadCrumbs />
		</div>
	);
}
```

## 结语

在书写react 组件的时候有很多的陷阱。永远不可能百分百的去理解整个原理和避开每个大大小小的错误。但是犯错也是我们学习框架和编程语言中重要的部分，没有人能够百分之百的规避这些错误。

我认为分享你的经验有助于防止其他人犯这些错误。
