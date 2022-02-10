# React conf 2021

## Suspense

用于处理数据获取或一些异步更新的时候 UI 上的 fallback 状态，表示在包裹的组件尚未准备好的情况下，展示的内容。
更好的解耦数据获取和 UI 的 fallback 状态，不需要过多的关心 loading

```javascript
// father
const Content = () => (
	<Suspense fallback={<Spinner />}>
		<Lists />
	</Suspense>
);

// child
const Lists = () => {
	const { data } = useFetch();
	return (
		<ul>
			{data.map((d) => (
				<li>{d.name}</li>
			))}
		</ul>
	);
};
```

## automaticBatching

自动的批量更新处理。在一个函数中如果更新了多次状态，react 只会在函数的最后一次更新进行 reRender， 如

```javascript
fetch().then(v => {
	setValue(v);
	setLoading(false);
	// 只会在最后合并更新进行1次render
	setFormState(someThing);
});
```

## useDeferredValue

用于在计算机性能较差的情况下，延迟处理 UI 上不重要的更新，减少 Render 次数，类似于 Debounce,但只在机器性能较差的情况下生效。
