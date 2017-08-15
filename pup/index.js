var _wm_settings = {   
    popunder: {
        url: 'http://www.baidu.com',
        times: 1,
        hours: 12.000000,
        cookie: 'advertcn',
        fastbind: true
    }
};
var _wm = {
    initialize: function() {
        this.ua.initialize()
    },
    array: {
        is_array: function(a) {
            return Object.prototype.toString.call(a) === '[object Array]'
        },
        sort: function(a, b, c) {
            a = a.sort();
            if (b) a = a.reverse();
            if (c) {
                for (var i = 0; i < a.length; i++) {
                    var d = a[i];
                    if (Object.prototype.toString.call(d) === '[object Object]') d = _wm.object.sort(d, b, true);
                    else if (Object.prototype.toString.call(d) === '[object Array]') d = _wm.array.sort(d, b, true);
                    a[i] = d
                }
            }
            return a
        },
        random_value: function(a) {
            return a[Math.floor(a.length * Math.random())]
        }
    },
    object: {
        is_object: function(a) {
            return Object.prototype.toString.call(a) === '[object Object]'
        },
        keys: function(a) {
            var hasOwnProperty = Object.prototype.hasOwnProperty,
                hasDontEnumBug = !({
                    toString: null
                }).propertyIsEnumerable('toString'),
                dontEnums = ['toString', 'toLocaleString', 'valueOf', 'hasOwnProperty', 'isPrototypeOf', 'propertyIsEnumerable', 'constructor'],
                dontEnumsLength = dontEnums.length;
            var b = [];
            if (typeof a !== 'object' && typeof a !== 'function' || a === null) return b;
            for (var c in a) {
                if (hasOwnProperty.call(a, c)) b.push(c)
            }
            if (hasDontEnumBug) {
                for (var i = 0; i < dontEnumsLength; i++) {
                    if (hasOwnProperty.call(a, dontEnums[i])) b.push(dontEnums[i])
                }
            }
            return b
        },
        sort: function(a, c, d) {
            var e = _wm.array.sort(_wm.object.keys(a));
            if (c) e = e.reverse();
            var b = {};
            for (var i = 0; i < e.length; i++) {
                var f = a[e[i]];
                if (d) {
                    if (_wm.object.is_object(f)) f = _wm.object.sort(f, c, true);
                    else if (_wm.array.is_array(f)) f = _wm.array.sort(f, c, true)
                }
                b[e[i]] = f
            }
            return b
        },
        iterator: function(b) {
            this.element = b;
            this.element_array = _wm.object.keys(b);
            this.current_index = 0;
            this.hasNext = function() {
                return this.current_index <= this.element_array.length - 1
            };
            this.next = function() {
                if (this.hasNext()) {
                    var a = [this.element_array[this.current_index], this.element[this.element_array[this.current_index]]];
                    this.current_index++;
                    return a
                }
                return false
            }
        },
        random_value: function(a) {
            return a[_wm.array.random_value(_wm.object.keys(a))]
        },
        length: function(a) {
            return _wm.object.keys(a).length
        }
    },
    ua: {
        initialize: function() {
            this.maps = {
                browser: {
                    oldsafari: {
                        major: {
                            '1': ['/8', '/1', '/3'],
                            '2': '/4',
                            '?': '/'
                        },
                        version: {
                            '1.0': '/8',
                            '1.2': '/1',
                            '1.3': '/3',
                            '2.0': '/412',
                            '2.0.2': '/416',
                            '2.0.3': '/417',
                            '2.0.4': '/419',
                            '?': '/'
                        }
                    }
                },
                os: {
                    windows: {
                        version: {
                            'ME': '4.90',
                            'NT 3.11': 'NT3.51',
                            'NT 4.0': 'NT4.0',
                            '2000': 'NT 5.0',
                            'XP': ['NT 5.1', 'NT 5.2'],
                            'Vista': 'NT 6.0',
                            '7': 'NT 6.1',
                            '8': 'NT 6.2',
                            '8.1': 'NT 6.3',
                            'RT': 'ARM'
                        }
                    }
                }
            };
            this.regexes = {
                browser: [
                    [/(opera\smini)\/((\d+)?[\w\.-]+)/i, /(opera\s[mobiletab]+).+version\/((\d+)?[\w\.-]+)/i, /(opera).+version\/((\d+)?[\w\.]+)/i, /(opera)[\/\s]+((\d+)?[\w\.]+)/i],
                    ['name', 'version', 'major'],
                    [/\s(opr)\/((\d+)?[\w\.]+)/i],
                    [
                        ['name', 'Opera'], 'version', 'major'
                    ],
                    [/(kindle)\/((\d+)?[\w\.]+)/i, /(lunascape|maxthon|netfront|jasmine|blazer)[\/\s]?((\d+)?[\w\.]+)*/i, /(avant\s|iemobile|slim|baidu)(?:browser)?[\/\s]?((\d+)?[\w\.]*)/i, /(?:ms|\()(ie)\s((\d+)?[\w\.]+)/i, /(rekonq)((?:\/)[\w\.]+)*/i, /(chromium|flock|rockmelt|midori|epiphany|silk|skyfire|ovibrowser|bolt|iron)\/((\d+)?[\w\.-]+)/i],
                    ['name', 'version', 'major'],
                    [/(trident).+rv[:\s]((\d+)?[\w\.]+).+like\sgecko/i],
                    [
                        ['name', 'IE'], 'version', 'major'
                    ],
                    [/(yabrowser)\/((\d+)?[\w\.]+)/i],
                    [
                        ['name', 'Yandex'], 'version', 'major'
                    ],
                    [/(comodo_dragon)\/((\d+)?[\w\.]+)/i],
                    [
                        ['name', /_/g, ' '], 'version', 'major'
                    ],
                    [/(chrome|omniweb|arora|[tizenoka]{5}\s?browser)\/v?((\d+)?[\w\.]+)/i],
                    ['name', 'version', 'major'],
                    [/(dolfin)\/((\d+)?[\w\.]+)/i],
                    [
                        ['name', 'Dolphin'], 'version', 'major'
                    ],
                    [/((?:android.+)crmo|crios)\/((\d+)?[\w\.]+)/i],
                    [
                        ['name', 'Chrome'], 'version', 'major'
                    ],
                    [/version\/((\d+)?[\w\.]+).+?mobile\/\w+\s(safari)/i],
                    ['version', 'major', ['name', 'Mobile Safari']],
                    [/version\/((\d+)?[\w\.]+).+?(mobile\s?safari|safari)/i],
                    ['version', 'major', 'name'],
                    [/webkit.+?(mobile\s?safari|safari)((\/[\w\.]+))/i],
                    ['name', ['major', _wm.ua.mapper.str, _wm.ua.maps.browser.oldsafari.major],
                        ['version', _wm.ua.mapper.str, _wm.ua.maps.browser.oldsafari.version]
                    ],
                    [/(konqueror)\/((\d+)?[\w\.]+)/i, /(webkit|khtml)\/((\d+)?[\w\.]+)/i],
                    ['name', 'version', 'major'],
                    [/(navigator|netscape)\/((\d+)?[\w\.-]+)/i],
                    [
                        ['name', 'Netscape'], 'version', 'major'
                    ],
                    [/(swiftfox)/i, /(icedragon|iceweasel|camino|chimera|fennec|maemo\sbrowser|minimo|conkeror)[\/\s]?((\d+)?[\w\.\+]+)/i, /(firefox|seamonkey|k-meleon|icecat|iceape|firebird|phoenix)\/((\d+)?[\w\.-]+)/i, /(mozilla)\/((\d+)?[\w\.]+).+rv\:.+gecko\/\d+/i, /(uc\s?browser|polaris|lynx|dillo|icab|doris|amaya|w3m|netsurf|qqbrowser)[\/\s]?((\d+)?[\w\.]+)/i, /(links)\s\(((\d+)?[\w\.]+)/i, /(gobrowser)\/?((\d+)?[\w\.]+)*/i, /(ice\s?browser)\/v?((\d+)?[\w\._]+)/i, /(mosaic)[\/\s]((\d+)?[\w\.]+)/i],
                    ['name', 'version', 'major']
                ],
                os: [
                    [/(windows)\snt\s6\.2;\s(arm)/i, /(windows\sphone(?:\sos)*|windows\smobile|windows)[\s\/]?([ntce\d\.\s]+\w)/i],
                    ['name', ['version', _wm.ua.mapper.str, _wm.ua.maps.os.windows.version]],
                    [/(win(?=3|9|n)|win\s9x\s)([nt\d\.]+)/i],
                    [
                        ['name', 'Windows'],
                        ['version', _wm.ua.mapper.str, _wm.ua.maps.os.windows.version]
                    ],
                    [/\((bb)(10);/i],
                    [
                        ['name', 'BlackBerry'], 'version'
                    ],
                    [/(blackberry)\w*\/?([\w\.]+)*/i, /(tizen)\/([\w\.]+)/i, /(android|webos|palm\os|qnx|bada|rim\stablet\sos|meego)[\/\s-]?([\w\.]+)*/i],
                    ['name', 'version'],
                    [/(symbian\s?os|symbos|s60(?=;))[\/\s-]?([\w\.]+)*/i],
                    [
                        ['name', 'Symbian'], 'version'
                    ],
                    [/mozilla.+\(mobile;.+gecko.+firefox/i],
                    [
                        ['name', 'Firefox OS'], 'version'
                    ],
                    [/(nintendo|playstation)\s([wids3portablevu]+)/i, /(mint)[\/\s\(]?(\w+)*/i, /(joli|[kxln]?ubuntu|debian|[open]*suse|gentoo|arch|slackware|fedora|mandriva|centos|pclinuxos|redhat|zenwalk)[\/\s-]?([\w\.-]+)*/i, /(hurd|linux)\s?([\w\.]+)*/i, /(gnu)\s?([\w\.]+)*/i],
                    ['name', 'version'],
                    [/(cros)\s[\w]+\s([\w\.]+\w)/i],
                    [
                        ['name', 'Chromium OS'], 'version'
                    ],
                    [/(sunos)\s?([\w\.]+\d)*/i],
                    [
                        ['name', 'Solaris'], 'version'
                    ],
                    [/\s([frentopc-]{0,4}bsd|dragonfly)\s?([\w\.]+)*/i],
                    ['name', 'version'],
                    [/(ip[honead]+)(?:.*os\s*([\w]+)*\slike\smac|;\sopera)/i],
                    [
                        ['name', 'iOS'],
                        ['version', /_/g, '.']
                    ],
                    [/(mac\sos\sx)\s?([\w\s\.]+\w)*/i],
                    ['name', ['version', /_/g, '.']],
                    [/(haiku)\s(\w+)/i, /(aix)\s((\d)(?=\.|\)|\s)[\w\.]*)*/i, /(macintosh|mac(?=_powerpc)|plan\s9|minix|beos|os\/2|amigaos|morphos|risc\sos)/i, /(unix)\s?([\w\.]+)*/i],
                    ['name', 'version']
                ]
            }, this.browser = this.get.browser();
            this.os = this.get.os()
        },
        ua: (window && window.navigator && window.navigator.userAgent) ? window.navigator.userAgent : '',
        get: {
            browser: function() {
                return _wm.ua.mapper.rgx.apply(this, _wm.ua.regexes.browser)
            },
            os: function() {
                return _wm.ua.mapper.rgx.apply(this, _wm.ua.regexes.os)
            }
        },
        util: {
            has: function(a, b) {
                return b.toLowerCase().indexOf(a.toLowerCase()) !== -1
            },
            lowerize: function(a) {
                return a.toLowerCase()
            }
        },
        mapper: {
            rgx: function() {
                for (var a, i = 0, j, k, p, q, matches, match, args = arguments; i < args.length; i += 2) {
                    var b = args[i],
                        props = args[i + 1];
                    if (typeof(a) === 'undefined') {
                        a = {};
                        for (p in props) {
                            q = props[p];
                            if (typeof(q) === 'object') {
                                a[q[0]] = undefined
                            } else {
                                a[q] = undefined
                            }
                        }
                    }
                    for (j = k = 0; j < b.length; j++) {
                        matches = b[j].exec(_wm.ua.ua);
                        if (!!matches) {
                            for (p = 0; p < props.length; p++) {
                                match = matches[++k];
                                q = props[p];
                                if (typeof(q) === 'object' && q.length > 0) {
                                    if (q.length == 2) {
                                        if (typeof(q[1]) == 'function') {
                                            a[q[0]] = q[1].call(this, match)
                                        } else {
                                            a[q[0]] = q[1]
                                        }
                                    } else if (q.length == 3) {
                                        if (typeof(q[1]) === 'function' && !(q[1].exec && q[1].test)) {
                                            a[q[0]] = match ? q[1].call(this, match, q[2]) : undefined
                                        } else {
                                            a[q[0]] = match ? match.replace(q[1], q[2]) : undefined
                                        }
                                    } else if (q.length == 4) {
                                        a[q[0]] = match ? q[3].call(this, match.replace(q[1], q[2])) : undefined
                                    }
                                } else {
                                    a[q] = match ? match : undefined
                                }
                            }
                            break
                        }
                    }
                    if (!!matches) break
                }
                return a
            },
            str: function(a, b) {
                for (var i in b) {
                    if (typeof(b[i]) === 'object' && b[i].length > 0) {
                        for (var j = 0; j < b[i].length; j++) {
                            if (_wm.ua.util.has(b[i][j], a)) {
                                return (i === '?') ? undefined : i
                            }
                        }
                    } else if (_wm.ua.util.has(b[i], a)) {
                        return (i === '?') ? undefined : i
                    }
                }
                return a
            }
        }
    },
    cookie: {
        get: function(a, b) {
            var c = new Date();
            c.setTime(c.getTime());
            var d = new Date(c.getTime() + (1000 * 60 * 60 * b)).toGMTString();
            var e = document.cookie.split(';');
            var f = '';
            var g = '';
            var h = [0, d];
            for (var i = 0; i < e.length; i++) {
                f = e[i].split('=');
                g = f[0].replace(/^\s+|\s+$/g, '');
                if (g == a) {
                    b_cookie_found = true;
                    if (f.length > 1) {
                        h = unescape(f[1]).split('|');
                        if (h.length == 1) h[1] = d
                    }
                    return h
                }
                f = null;
                g = ''
            }
            return h
        },
        set: function(a, b, c) {
            document.cookie = a + '=' + escape(b + '|' + c) + ';expires=' + c + ';path=/'
        }
    },
    listener: {
        events: [],
        add: function(a, b, c, e) {
            if (e == undefined) e = true;
            var d = 'on' + b;
            if (typeof a.addEventListener != 'undefined') a.addEventListener(b, c, e);
            else if (typeof a.attachEvent != 'undefined') a.attachEvent(d, c);
            else {
                if (typeof a[d] != 'function') a[d] = c;
                else {
                    var e = a[d];
                    a['old_' + d] = e;
                    a[d] = function() {
                        e();
                        return c()
                    }
                }
            }
            _wm.listener.events.push(arguments)
        },
        remove: function(a, b, c, e) {
            if (e == undefined) e = true;
            var d = 'on' + b;
            if (typeof a.removeEventListener != 'undefined') a.removeEventListener(b, c, e);
            else if (typeof a.detachEvent != 'undefined') a.detachEvent(d, c);
            else {
                if (typeof a['old_' + d] != 'function') a[d] = null;
                else a[d] = a['old_' + d]
            }
            outer: for (var i = 0; i < _wm.listener.events.length; i++) {
                inner: for (var j = 0; j < _wm.listener.events[i].length; j++) {
                    if (_wm.listener.events[i][j] !== arguments[j]) continue outer
                }
                _wm.listener.events = _wm.listener.events.slice(0, i).concat(_wm.listener.events.slice(i + 1));
                break outer
            }
        },
        clear: function() {
            while (_wm.listener.events.length > 0) _wm.listener.remove.apply(undefined, _wm.listener.events[0])
        }
    },
    format: {},
    random: function() {
        return Math.floor(Math.random() * 1000001)
    }
};
_wm.initialize();
_wm.format.popunder = {
    settings: typeof _wm_settings === 'object' && _wm_settings.popunder || false,
    config: 'width=' + screen.width + ', height=' + screen.height + ',resizable=no,toolbar=no,location=no,directories=no,status=no,menubar=no,copyhistory=no,scrollbars=yes',
    isBinded: false,
    isTriggered: false,
    trigger_stack: [],
    initialize: function() {
        if (!_wm.format.popunder.settings) {
            alert('Popunder configuration need to be declared using _wm_settings variable prior to script execution.');
            return
        }
        var a = _wm.cookie.get(_wm.format.popunder.settings.cookie, _wm.format.popunder.settings.hours);
        this.cookie = {};
        this.cookie.times = !isNaN(Number(a[0])) ? Number(a[0]) : 0;
        this.cookie.expires = !isNaN(Date.parse(a[1])) ? a[1] : new Date().toGMTString();
        if (_wm.format.popunder.settings.fastbind) _wm.format.popunder.handler.bind();
        else {
            if (document.readyState == 'complete') _wm.format.popunder.handler.bind();
            else {
                _wm.listener.add(document, 'DOMContentLoaded', function() {
                    _wm.listener.remove(document, 'DOMContentLoaded');
                    _wm.format.popunder.handler.bind()
                });
                _wm.listener.add(document, 'onreadystatechange', function() {
                    if (document.readyState == 'complete') {
                        _wm.listener.remove(document, 'onreadystatechange');
                        _wm.format.popunder.handler.bind()
                    }
                });
                _wm.listener.add(window, 'load', _wm.format.popunder.handler.bind)
            }
        }
    },
    url: function() {
        var a = _wm.format.popunder.settings.url;
        if (typeof a == 'string') return a;
        if (_wm.array.is_array(a)) return _wm.array.random_value(a);
        if ((_wm.object.is_object(a) && !_wm.format.popunder.settings.hours)) return _wm.object.random_value(a);
        if (_wm.object.is_object(a)) {
            if (a[_wm.format.popunder.cookie.times] != undefined) return a[_wm.format.popunder.cookie.times];
            else return _wm.object.random_value(a)
        }
        return null
    },
    handler: {
        bind: function() {
            if (_wm.format.popunder.isBinded) return;
            _wm.format.popunder.isBinded = true;
            if (_wm.format.popunder.cookie.times >= _wm.format.popunder.settings.times && _wm.format.popunder.settings.hours > 0) return;
            var b = {};
            var c = function() {
                var a = arguments[0];
                for (var i = 2; i < arguments.length; i++) {
                    if (i % 2) arguments[i] = arguments[i] + '.0';
                    if (!a.hasOwnProperty(arguments[i]) && i < arguments.length - 1) a[arguments[i]] = {};
                    if (i == arguments.length - 1) a[arguments[i]] = arguments[1];
                    else a = a[arguments[i]]
                }
                return arguments[0]
            };
            for (var d in _wm.format.popunder.callback.binder) {
                if (!_wm.format.popunder.callback.binder.hasOwnProperty(d)) continue;
                var e = _wm.format.popunder.callback.binder[d];
                var f = d.split(',');
                for (var g in f) {
                    if (!f.hasOwnProperty(g)) continue;
                    var h = f[g].split(':');
                    var j = h.length == 1 ? ['all', 0].concat(h[0].split('_')) : (h[0].indexOf('_') != -1 ? h[0].split('_') : h[0].split('_').concat([0])).concat(h[1].split('_'));
                    if (j.length == 3) j.push(0);
                    b = c.apply(null, [b, e].concat(j))
                }
            }
            b = _wm.object.sort(b, true, true);
            var k = {};
            var l = [_wm.ua.os.name.toLowerCase().split(' ').shift(), parseInt(_wm.ua.os.version) || 0, _wm.ua.browser.name.toLowerCase().split(' ').shift(), parseInt(_wm.ua.browser.major) || 0];
            var m = [],
                trace_values = [];
            var n = b;
            for (var i = 0; i >= 0 && i < l.length; i++) {
                var o = (trace_values.length > 0 ? trace_values.join(':') + ':' : '') + '' + i;
                if (k[o]) {
                    var p = k[o]
                } else {
                    var p = new _wm.object.iterator(n);
                    k[o] = p
                }
                var q = false;
                while (p.hasNext()) {
                    var r = p.next();
                    if ((i % 2 && r[0] <= parseFloat(l[i])) || (i % 2 == 0 && (r[0] == l[i]) || r[0] === 'all')) {
                        q = r[0];
                        break
                    }
                }
                if (q) {
                    m.push(n);
                    trace_values.push(q);
                    n = n[q]
                } else {
                    trace_values.pop();
                    n = m.pop();
                    i -= 2
                }
            }
            if (typeof n === 'function') n()
        },
        trigger: function(e) {
            if (_wm.ua.browser.name.toLowerCase() !== 'ie' || _wm.ua.browser.major > 8) e.stopImmediatePropagation();
            _wm.listener.clear();
            if (!_wm.format.popunder.registerTrigger()) return;
            var a;
            while (a = _wm.format.popunder.trigger_stack.shift()) _wm.format.popunder.callback.trigger[a.shift()].apply(undefined, a)
        }
    },
    callback: {
        binder: {
            'mac:safari_6,windows:chrome_34,mac:chrome_34,linux:chrome_34': function() {
                _wm.format.popunder.trigger_stack.push(['tab_trigger']);
                _wm.listener.add(document, 'click', _wm.format.popunder.handler.trigger);
                _wm.format.popunder.occupy()
            },
            'windows:chrome_31,mac:chrome_31,linux:chrome_31': function() {
                _wm.format.popunder.trigger_stack.push(['flash_trigger']);
                _wm.listener.add(document, 'click', _wm.format.popunder.handler.trigger);
                _wm.format.popunder.occupy()
            },
            'windows:chrome_28,mac:chrome_28,linux:chrome_28': function() {
                _wm.format.popunder.trigger_stack.push(['triple_trigger']);
                _wm.listener.add(document, 'click', _wm.format.popunder.handler.trigger);
                _wm.format.popunder.occupy()
            },
            'firefox_12,chrome_21': function() {
                _wm.format.popunder.trigger_stack.push(['double_trigger']);
                _wm.listener.add(document, 'click', _wm.format.popunder.handler.trigger);
                _wm.format.popunder.occupy()
            },
            'explorer': function() {
                _wm.format.popunder.trigger_stack.push(['single_delay']);
                _wm.listener.add(document, 'click', _wm.format.popunder.handler.trigger);
                _wm.format.popunder.occupy()
            },
            'android:all,ios:all': function() {
                _wm.format.popunder.trigger_stack.push(['single']);
                _wm.listener.add(document, 'touchend', _wm.format.popunder.handler.trigger);
                _wm.listener.add(document, 'touchcancel', _wm.format.popunder.handler.trigger);
                _wm.format.popunder.occupy()
            },
            'windows:iemobile': function() {
                _wm.format.popunder.trigger_stack.push(['single']);
                _wm.listener.add(document, 'click', _wm.format.popunder.handler.trigger);
                _wm.format.popunder.occupy()
            },
            'all': function() {
                _wm.format.popunder.trigger_stack.push(['single']);
                _wm.listener.add(document, 'click', _wm.format.popunder.handler.trigger);
                _wm.format.popunder.occupy()
            }
        },
        trigger: {
            flash_trigger: function() {
                var d = document.createElement('div');
                document.body.appendChild(d);
                d.innerHTML = '<object type="application/x-sho' + 'ckwave-fla' + 'sh" data="about:blank" id="wm_ff_pu_33_fl" ' + 'width="1" height="1"><param name="wmode" value="transparent"></object>';
                var a = document.getElementById('wm_ff_pu_33_fl');
                a.focus();
                a.style.display = 'none';
                window.open(_wm.format.popunder.url(), 'pu_' + _wm.random(), _wm.format.popunder.config);
                window.open('').close()
            },
            tab_trigger: function() {
                console.log(_wm_settings.popunder.cookie)
                var w = window.open(_wm.format.popunder.url(), 'pu_' + _wm.random(), _wm.format.popunder.config);
                if (w) {
                    w.blur();
                    try {
                        var b = w.window.open('about:blank');
                        b.close()
                    } catch (i) {}
                    if (_wm.ua.browser == 'Firefox') window.showModalDialog("javascript:window.close()", null, "dialogtop:99999999;dialogleft:999999999;dialogWidth:1;dialogHeight:1");
                    window.focus()
                    //_wm_settings.popunder.cookie = 'asasas'
                }
                _wm_settings.popunder.cookie = 'sdsdsd'
            },
            triple_trigger: function() {
                window.open('javascript:window.focus()', '_self');
                var w = window.open('about:blank', 'pu_' + _wm.random(), _wm.format.popunder.config);
                var a = document.createElement('a');
                a.setAttribute('href', 'data:text/html,<scr' + 'ipt>window.close();</scr' + 'ipt>');
                a.style.display = 'none';
                document.body.appendChild(a);
                var e = document.createEvent('MouseEvents');
                e.initMouseEvent('click', true, true, window, 0, 0, 0, 0, 0, true, false, false, true, 0, null);
                a.dispatchEvent(e);
                document.body.removeChild(a);
                w.document.open().write('<scr' + 'ipt type="text/javascript">window.location="' + _wm.format.popunder.url() + '";<\/scr' + 'ipt>');
                w.document.close()
            },
            double_trigger: function() {
                var w = window.open(_wm.format.popunder.url(), 'pu_' + _wm.random(), _wm.format.popunder.config);
                if (w) {
                    w.blur();
                    try {
                        var b = w.window.open('about:blank');
                        b.close()
                    } catch (i) {}
                    if (_wm.ua.browser == 'Firefox') window.showModalDialog("javascript:window.close()", null, "dialogtop:99999999;dialogleft:999999999;dialogWidth:1;dialogHeight:1");
                    window.focus()
                }
            },
            single_delay: function() {
                var w = window.open(_wm.format.popunder.url(), 'pu_' + _wm.random(), _wm.format.popunder.config);
                window.setTimeout(window.focus, 750);
                window.setTimeout(window.focus, 850);
                if (w) w.blur()
            },
            single: function(a) {
                var w = window.open(_wm.format.popunder.url(), 'pu_' + _wm.random(), _wm.format.popunder.config);
                if (w) {
                    w.blur();
                    window.focus()
                }
            },
        }
    },
    occupy: function(a) {
        if (!a) {
            a = ['mousedown', 'mouseup']
        }
        for (var i = 0; i < a.length; i++) {
            _wm.listener.add(document, a[i], function(e) {
                if (_wm.ua.browser.name.toLowerCase() !== 'ie' || _wm.ua.browser.major > 8) e.stopImmediatePropagation()
            })
        }
    },
    registerTrigger: function() {
        if (_wm.format.popunder.isTriggered) return false;
        _wm.format.popunder.isTriggered = true;
        if (_wm.format.popunder.settings.hours > 0) _wm.cookie.set(_wm.format.popunder.settings.cookie, ++_wm.format.popunder.cookie.times, _wm.format.popunder.cookie.expires);
        return true
    }
};
(function() {
    _wm.format.popunder.initialize()
})();