const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set([]),
	mimeTypes: {},
	_: {
		client: {"start":"_app/immutable/entry/start.DFOnARUy.js","app":"_app/immutable/entry/app.Co3LTK6C.js","imports":["_app/immutable/entry/start.DFOnARUy.js","_app/immutable/chunks/client.nSHfXtwW.js","_app/immutable/entry/app.Co3LTK6C.js","_app/immutable/chunks/preload-helper.DpQnamwV.js"],"stylesheets":[],"fonts":[],"uses_env_dynamic_public":false},
		nodes: [
			__memo(() => import('./chunks/0-Ch43j9k-.js')),
			__memo(() => import('./chunks/1-xLg4h0n_.js')),
			__memo(() => import('./chunks/2-D2ULSBj6.js').then(function (n) { return n.aJ; }))
		],
		routes: [
			{
				id: "/[...catchall]",
				pattern: /^(?:\/(.*))?\/?$/,
				params: [{"name":"catchall","optional":false,"rest":true,"chained":true}],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			}
		],
		matchers: async () => {
			
			return {  };
		},
		server_assets: {}
	}
}
})();

const prerendered = new Set([]);

const base = "";

export { base, manifest, prerendered };
//# sourceMappingURL=manifest.js.map
