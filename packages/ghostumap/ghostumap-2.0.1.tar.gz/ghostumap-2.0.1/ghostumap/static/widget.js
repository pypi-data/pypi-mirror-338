function Et(t, e) {
  return t == null || e == null ? NaN : t < e ? -1 : t > e ? 1 : t >= e ? 0 : NaN;
}
function ii(t, e) {
  return t == null || e == null ? NaN : e < t ? -1 : e > t ? 1 : e >= t ? 0 : NaN;
}
function hn(t) {
  let e, n, i;
  t.length !== 2 ? (e = Et, n = (a, c) => Et(t(a), c), i = (a, c) => t(a) - c) : (e = t === Et || t === ii ? t : ri, n = t, i = t);
  function r(a, c, l = 0, h = a.length) {
    if (l < h) {
      if (e(c, c) !== 0) return h;
      do {
        const u = l + h >>> 1;
        n(a[u], c) < 0 ? l = u + 1 : h = u;
      } while (l < h);
    }
    return l;
  }
  function s(a, c, l = 0, h = a.length) {
    if (l < h) {
      if (e(c, c) !== 0) return h;
      do {
        const u = l + h >>> 1;
        n(a[u], c) <= 0 ? l = u + 1 : h = u;
      } while (l < h);
    }
    return l;
  }
  function o(a, c, l = 0, h = a.length) {
    const u = r(a, c, l, h - 1);
    return u > l && i(a[u - 1], c) > -i(a[u], c) ? u - 1 : u;
  }
  return { left: r, center: o, right: s };
}
function ri() {
  return 0;
}
function si(t) {
  return t === null ? NaN : +t;
}
const oi = hn(Et), ai = oi.right;
hn(si).center;
function Ce(t, e) {
  let n, i;
  if (e === void 0)
    for (const r of t)
      r != null && (n === void 0 ? r >= r && (n = i = r) : (n > r && (n = r), i < r && (i = r)));
  else {
    let r = -1;
    for (let s of t)
      (s = e(s, ++r, t)) != null && (n === void 0 ? s >= s && (n = i = s) : (n > s && (n = s), i < s && (i = s)));
  }
  return [n, i];
}
class Ee extends Map {
  constructor(e, n = ui) {
    if (super(), Object.defineProperties(this, { _intern: { value: /* @__PURE__ */ new Map() }, _key: { value: n } }), e != null) for (const [i, r] of e) this.set(i, r);
  }
  get(e) {
    return super.get(Ne(this, e));
  }
  has(e) {
    return super.has(Ne(this, e));
  }
  set(e, n) {
    return super.set(li(this, e), n);
  }
  delete(e) {
    return super.delete(ci(this, e));
  }
}
function Ne({ _intern: t, _key: e }, n) {
  const i = e(n);
  return t.has(i) ? t.get(i) : n;
}
function li({ _intern: t, _key: e }, n) {
  const i = e(n);
  return t.has(i) ? t.get(i) : (t.set(i, n), n);
}
function ci({ _intern: t, _key: e }, n) {
  const i = e(n);
  return t.has(i) && (n = t.get(i), t.delete(i)), n;
}
function ui(t) {
  return t !== null && typeof t == "object" ? t.valueOf() : t;
}
const hi = Math.sqrt(50), fi = Math.sqrt(10), di = Math.sqrt(2);
function Pt(t, e, n) {
  const i = (e - t) / Math.max(0, n), r = Math.floor(Math.log10(i)), s = i / Math.pow(10, r), o = s >= hi ? 10 : s >= fi ? 5 : s >= di ? 2 : 1;
  let a, c, l;
  return r < 0 ? (l = Math.pow(10, -r) / o, a = Math.round(t * l), c = Math.round(e * l), a / l < t && ++a, c / l > e && --c, l = -l) : (l = Math.pow(10, r) * o, a = Math.round(t / l), c = Math.round(e / l), a * l < t && ++a, c * l > e && --c), c < a && 0.5 <= n && n < 2 ? Pt(t, e, n * 2) : [a, c, l];
}
function pi(t, e, n) {
  if (e = +e, t = +t, n = +n, !(n > 0)) return [];
  if (t === e) return [t];
  const i = e < t, [r, s, o] = i ? Pt(e, t, n) : Pt(t, e, n);
  if (!(s >= r)) return [];
  const a = s - r + 1, c = new Array(a);
  if (i)
    if (o < 0) for (let l = 0; l < a; ++l) c[l] = (s - l) / -o;
    else for (let l = 0; l < a; ++l) c[l] = (s - l) * o;
  else if (o < 0) for (let l = 0; l < a; ++l) c[l] = (r + l) / -o;
  else for (let l = 0; l < a; ++l) c[l] = (r + l) * o;
  return c;
}
function ne(t, e, n) {
  return e = +e, t = +t, n = +n, Pt(t, e, n)[2];
}
function gi(t, e, n) {
  e = +e, t = +t, n = +n;
  const i = e < t, r = i ? ne(e, t, n) : ne(t, e, n);
  return (i ? -1 : 1) * (r < 0 ? 1 / -r : r);
}
function mi(t, e) {
  let n;
  for (const i of t)
    i != null && (n < i || n === void 0 && i >= i) && (n = i);
  return n;
}
function fn(t, e, n) {
  t = +t, e = +e, n = (r = arguments.length) < 2 ? (e = t, t = 0, 1) : r < 3 ? 1 : +n;
  for (var i = -1, r = Math.max(0, Math.ceil((e - t) / n)) | 0, s = new Array(r); ++i < r; )
    s[i] = t + i * n;
  return s;
}
var yi = { value: () => {
} };
function dn() {
  for (var t = 0, e = arguments.length, n = {}, i; t < e; ++t) {
    if (!(i = arguments[t] + "") || i in n || /[\s.]/.test(i)) throw new Error("illegal type: " + i);
    n[i] = [];
  }
  return new Nt(n);
}
function Nt(t) {
  this._ = t;
}
function _i(t, e) {
  return t.trim().split(/^|\s+/).map(function(n) {
    var i = "", r = n.indexOf(".");
    if (r >= 0 && (i = n.slice(r + 1), n = n.slice(0, r)), n && !e.hasOwnProperty(n)) throw new Error("unknown type: " + n);
    return { type: n, name: i };
  });
}
Nt.prototype = dn.prototype = {
  constructor: Nt,
  on: function(t, e) {
    var n = this._, i = _i(t + "", n), r, s = -1, o = i.length;
    if (arguments.length < 2) {
      for (; ++s < o; ) if ((r = (t = i[s]).type) && (r = xi(n[r], t.name))) return r;
      return;
    }
    if (e != null && typeof e != "function") throw new Error("invalid callback: " + e);
    for (; ++s < o; )
      if (r = (t = i[s]).type) n[r] = Te(n[r], t.name, e);
      else if (e == null) for (r in n) n[r] = Te(n[r], t.name, null);
    return this;
  },
  copy: function() {
    var t = {}, e = this._;
    for (var n in e) t[n] = e[n].slice();
    return new Nt(t);
  },
  call: function(t, e) {
    if ((r = arguments.length - 2) > 0) for (var n = new Array(r), i = 0, r, s; i < r; ++i) n[i] = arguments[i + 2];
    if (!this._.hasOwnProperty(t)) throw new Error("unknown type: " + t);
    for (s = this._[t], i = 0, r = s.length; i < r; ++i) s[i].value.apply(e, n);
  },
  apply: function(t, e, n) {
    if (!this._.hasOwnProperty(t)) throw new Error("unknown type: " + t);
    for (var i = this._[t], r = 0, s = i.length; r < s; ++r) i[r].value.apply(e, n);
  }
};
function xi(t, e) {
  for (var n = 0, i = t.length, r; n < i; ++n)
    if ((r = t[n]).name === e)
      return r.value;
}
function Te(t, e, n) {
  for (var i = 0, r = t.length; i < r; ++i)
    if (t[i].name === e) {
      t[i] = yi, t = t.slice(0, i).concat(t.slice(i + 1));
      break;
    }
  return n != null && t.push({ name: e, value: n }), t;
}
var ie = "http://www.w3.org/1999/xhtml";
const Le = {
  svg: "http://www.w3.org/2000/svg",
  xhtml: ie,
  xlink: "http://www.w3.org/1999/xlink",
  xml: "http://www.w3.org/XML/1998/namespace",
  xmlns: "http://www.w3.org/2000/xmlns/"
};
function Ot(t) {
  var e = t += "", n = e.indexOf(":");
  return n >= 0 && (e = t.slice(0, n)) !== "xmlns" && (t = t.slice(n + 1)), Le.hasOwnProperty(e) ? { space: Le[e], local: t } : t;
}
function bi(t) {
  return function() {
    var e = this.ownerDocument, n = this.namespaceURI;
    return n === ie && e.documentElement.namespaceURI === ie ? e.createElement(t) : e.createElementNS(n, t);
  };
}
function vi(t) {
  return function() {
    return this.ownerDocument.createElementNS(t.space, t.local);
  };
}
function ge(t) {
  var e = Ot(t);
  return (e.local ? vi : bi)(e);
}
function wi() {
}
function me(t) {
  return t == null ? wi : function() {
    return this.querySelector(t);
  };
}
function $i(t) {
  typeof t != "function" && (t = me(t));
  for (var e = this._groups, n = e.length, i = new Array(n), r = 0; r < n; ++r)
    for (var s = e[r], o = s.length, a = i[r] = new Array(o), c, l, h = 0; h < o; ++h)
      (c = s[h]) && (l = t.call(c, c.__data__, h, s)) && ("__data__" in c && (l.__data__ = c.__data__), a[h] = l);
  return new k(i, this._parents);
}
function Ai(t) {
  return t == null ? [] : Array.isArray(t) ? t : Array.from(t);
}
function ki() {
  return [];
}
function pn(t) {
  return t == null ? ki : function() {
    return this.querySelectorAll(t);
  };
}
function Mi(t) {
  return function() {
    return Ai(t.apply(this, arguments));
  };
}
function Si(t) {
  typeof t == "function" ? t = Mi(t) : t = pn(t);
  for (var e = this._groups, n = e.length, i = [], r = [], s = 0; s < n; ++s)
    for (var o = e[s], a = o.length, c, l = 0; l < a; ++l)
      (c = o[l]) && (i.push(t.call(c, c.__data__, l, o)), r.push(c));
  return new k(i, r);
}
function gn(t) {
  return function() {
    return this.matches(t);
  };
}
function mn(t) {
  return function(e) {
    return e.matches(t);
  };
}
var Ci = Array.prototype.find;
function Ei(t) {
  return function() {
    return Ci.call(this.children, t);
  };
}
function Ni() {
  return this.firstElementChild;
}
function Ti(t) {
  return this.select(t == null ? Ni : Ei(typeof t == "function" ? t : mn(t)));
}
var Li = Array.prototype.filter;
function Pi() {
  return Array.from(this.children);
}
function Ri(t) {
  return function() {
    return Li.call(this.children, t);
  };
}
function Ui(t) {
  return this.selectAll(t == null ? Pi : Ri(typeof t == "function" ? t : mn(t)));
}
function Ii(t) {
  typeof t != "function" && (t = gn(t));
  for (var e = this._groups, n = e.length, i = new Array(n), r = 0; r < n; ++r)
    for (var s = e[r], o = s.length, a = i[r] = [], c, l = 0; l < o; ++l)
      (c = s[l]) && t.call(c, c.__data__, l, s) && a.push(c);
  return new k(i, this._parents);
}
function yn(t) {
  return new Array(t.length);
}
function Di() {
  return new k(this._enter || this._groups.map(yn), this._parents);
}
function Rt(t, e) {
  this.ownerDocument = t.ownerDocument, this.namespaceURI = t.namespaceURI, this._next = null, this._parent = t, this.__data__ = e;
}
Rt.prototype = {
  constructor: Rt,
  appendChild: function(t) {
    return this._parent.insertBefore(t, this._next);
  },
  insertBefore: function(t, e) {
    return this._parent.insertBefore(t, e);
  },
  querySelector: function(t) {
    return this._parent.querySelector(t);
  },
  querySelectorAll: function(t) {
    return this._parent.querySelectorAll(t);
  }
};
function Bi(t) {
  return function() {
    return t;
  };
}
function zi(t, e, n, i, r, s) {
  for (var o = 0, a, c = e.length, l = s.length; o < l; ++o)
    (a = e[o]) ? (a.__data__ = s[o], i[o] = a) : n[o] = new Rt(t, s[o]);
  for (; o < c; ++o)
    (a = e[o]) && (r[o] = a);
}
function Fi(t, e, n, i, r, s, o) {
  var a, c, l = /* @__PURE__ */ new Map(), h = e.length, u = s.length, f = new Array(h), d;
  for (a = 0; a < h; ++a)
    (c = e[a]) && (f[a] = d = o.call(c, c.__data__, a, e) + "", l.has(d) ? r[a] = c : l.set(d, c));
  for (a = 0; a < u; ++a)
    d = o.call(t, s[a], a, s) + "", (c = l.get(d)) ? (i[a] = c, c.__data__ = s[a], l.delete(d)) : n[a] = new Rt(t, s[a]);
  for (a = 0; a < h; ++a)
    (c = e[a]) && l.get(f[a]) === c && (r[a] = c);
}
function Hi(t) {
  return t.__data__;
}
function Wi(t, e) {
  if (!arguments.length) return Array.from(this, Hi);
  var n = e ? Fi : zi, i = this._parents, r = this._groups;
  typeof t != "function" && (t = Bi(t));
  for (var s = r.length, o = new Array(s), a = new Array(s), c = new Array(s), l = 0; l < s; ++l) {
    var h = i[l], u = r[l], f = u.length, d = Oi(t.call(h, h && h.__data__, l, i)), p = d.length, g = a[l] = new Array(p), y = o[l] = new Array(p), w = c[l] = new Array(f);
    n(h, u, g, y, w, d, e);
    for (var b = 0, v = 0, M, _; b < p; ++b)
      if (M = g[b]) {
        for (b >= v && (v = b + 1); !(_ = y[v]) && ++v < p; ) ;
        M._next = _ || null;
      }
  }
  return o = new k(o, i), o._enter = a, o._exit = c, o;
}
function Oi(t) {
  return typeof t == "object" && "length" in t ? t : Array.from(t);
}
function Vi() {
  return new k(this._exit || this._groups.map(yn), this._parents);
}
function qi(t, e, n) {
  var i = this.enter(), r = this, s = this.exit();
  return typeof t == "function" ? (i = t(i), i && (i = i.selection())) : i = i.append(t + ""), e != null && (r = e(r), r && (r = r.selection())), n == null ? s.remove() : n(s), i && r ? i.merge(r).order() : r;
}
function Xi(t) {
  for (var e = t.selection ? t.selection() : t, n = this._groups, i = e._groups, r = n.length, s = i.length, o = Math.min(r, s), a = new Array(r), c = 0; c < o; ++c)
    for (var l = n[c], h = i[c], u = l.length, f = a[c] = new Array(u), d, p = 0; p < u; ++p)
      (d = l[p] || h[p]) && (f[p] = d);
  for (; c < r; ++c)
    a[c] = n[c];
  return new k(a, this._parents);
}
function Gi() {
  for (var t = this._groups, e = -1, n = t.length; ++e < n; )
    for (var i = t[e], r = i.length - 1, s = i[r], o; --r >= 0; )
      (o = i[r]) && (s && o.compareDocumentPosition(s) ^ 4 && s.parentNode.insertBefore(o, s), s = o);
  return this;
}
function Yi(t) {
  t || (t = Zi);
  function e(u, f) {
    return u && f ? t(u.__data__, f.__data__) : !u - !f;
  }
  for (var n = this._groups, i = n.length, r = new Array(i), s = 0; s < i; ++s) {
    for (var o = n[s], a = o.length, c = r[s] = new Array(a), l, h = 0; h < a; ++h)
      (l = o[h]) && (c[h] = l);
    c.sort(e);
  }
  return new k(r, this._parents).order();
}
function Zi(t, e) {
  return t < e ? -1 : t > e ? 1 : t >= e ? 0 : NaN;
}
function Ki() {
  var t = arguments[0];
  return arguments[0] = this, t.apply(null, arguments), this;
}
function Qi() {
  return Array.from(this);
}
function Ji() {
  for (var t = this._groups, e = 0, n = t.length; e < n; ++e)
    for (var i = t[e], r = 0, s = i.length; r < s; ++r) {
      var o = i[r];
      if (o) return o;
    }
  return null;
}
function ji() {
  let t = 0;
  for (const e of this) ++t;
  return t;
}
function tr() {
  return !this.node();
}
function er(t) {
  for (var e = this._groups, n = 0, i = e.length; n < i; ++n)
    for (var r = e[n], s = 0, o = r.length, a; s < o; ++s)
      (a = r[s]) && t.call(a, a.__data__, s, r);
  return this;
}
function nr(t) {
  return function() {
    this.removeAttribute(t);
  };
}
function ir(t) {
  return function() {
    this.removeAttributeNS(t.space, t.local);
  };
}
function rr(t, e) {
  return function() {
    this.setAttribute(t, e);
  };
}
function sr(t, e) {
  return function() {
    this.setAttributeNS(t.space, t.local, e);
  };
}
function or(t, e) {
  return function() {
    var n = e.apply(this, arguments);
    n == null ? this.removeAttribute(t) : this.setAttribute(t, n);
  };
}
function ar(t, e) {
  return function() {
    var n = e.apply(this, arguments);
    n == null ? this.removeAttributeNS(t.space, t.local) : this.setAttributeNS(t.space, t.local, n);
  };
}
function lr(t, e) {
  var n = Ot(t);
  if (arguments.length < 2) {
    var i = this.node();
    return n.local ? i.getAttributeNS(n.space, n.local) : i.getAttribute(n);
  }
  return this.each((e == null ? n.local ? ir : nr : typeof e == "function" ? n.local ? ar : or : n.local ? sr : rr)(n, e));
}
function _n(t) {
  return t.ownerDocument && t.ownerDocument.defaultView || t.document && t || t.defaultView;
}
function cr(t) {
  return function() {
    this.style.removeProperty(t);
  };
}
function ur(t, e, n) {
  return function() {
    this.style.setProperty(t, e, n);
  };
}
function hr(t, e, n) {
  return function() {
    var i = e.apply(this, arguments);
    i == null ? this.style.removeProperty(t) : this.style.setProperty(t, i, n);
  };
}
function fr(t, e, n) {
  return arguments.length > 1 ? this.each((e == null ? cr : typeof e == "function" ? hr : ur)(t, e, n ?? "")) : K(this.node(), t);
}
function K(t, e) {
  return t.style.getPropertyValue(e) || _n(t).getComputedStyle(t, null).getPropertyValue(e);
}
function dr(t) {
  return function() {
    delete this[t];
  };
}
function pr(t, e) {
  return function() {
    this[t] = e;
  };
}
function gr(t, e) {
  return function() {
    var n = e.apply(this, arguments);
    n == null ? delete this[t] : this[t] = n;
  };
}
function mr(t, e) {
  return arguments.length > 1 ? this.each((e == null ? dr : typeof e == "function" ? gr : pr)(t, e)) : this.node()[t];
}
function xn(t) {
  return t.trim().split(/^|\s+/);
}
function ye(t) {
  return t.classList || new bn(t);
}
function bn(t) {
  this._node = t, this._names = xn(t.getAttribute("class") || "");
}
bn.prototype = {
  add: function(t) {
    var e = this._names.indexOf(t);
    e < 0 && (this._names.push(t), this._node.setAttribute("class", this._names.join(" ")));
  },
  remove: function(t) {
    var e = this._names.indexOf(t);
    e >= 0 && (this._names.splice(e, 1), this._node.setAttribute("class", this._names.join(" ")));
  },
  contains: function(t) {
    return this._names.indexOf(t) >= 0;
  }
};
function vn(t, e) {
  for (var n = ye(t), i = -1, r = e.length; ++i < r; ) n.add(e[i]);
}
function wn(t, e) {
  for (var n = ye(t), i = -1, r = e.length; ++i < r; ) n.remove(e[i]);
}
function yr(t) {
  return function() {
    vn(this, t);
  };
}
function _r(t) {
  return function() {
    wn(this, t);
  };
}
function xr(t, e) {
  return function() {
    (e.apply(this, arguments) ? vn : wn)(this, t);
  };
}
function br(t, e) {
  var n = xn(t + "");
  if (arguments.length < 2) {
    for (var i = ye(this.node()), r = -1, s = n.length; ++r < s; ) if (!i.contains(n[r])) return !1;
    return !0;
  }
  return this.each((typeof e == "function" ? xr : e ? yr : _r)(n, e));
}
function vr() {
  this.textContent = "";
}
function wr(t) {
  return function() {
    this.textContent = t;
  };
}
function $r(t) {
  return function() {
    var e = t.apply(this, arguments);
    this.textContent = e ?? "";
  };
}
function Ar(t) {
  return arguments.length ? this.each(t == null ? vr : (typeof t == "function" ? $r : wr)(t)) : this.node().textContent;
}
function kr() {
  this.innerHTML = "";
}
function Mr(t) {
  return function() {
    this.innerHTML = t;
  };
}
function Sr(t) {
  return function() {
    var e = t.apply(this, arguments);
    this.innerHTML = e ?? "";
  };
}
function Cr(t) {
  return arguments.length ? this.each(t == null ? kr : (typeof t == "function" ? Sr : Mr)(t)) : this.node().innerHTML;
}
function Er() {
  this.nextSibling && this.parentNode.appendChild(this);
}
function Nr() {
  return this.each(Er);
}
function Tr() {
  this.previousSibling && this.parentNode.insertBefore(this, this.parentNode.firstChild);
}
function Lr() {
  return this.each(Tr);
}
function Pr(t) {
  var e = typeof t == "function" ? t : ge(t);
  return this.select(function() {
    return this.appendChild(e.apply(this, arguments));
  });
}
function Rr() {
  return null;
}
function Ur(t, e) {
  var n = typeof t == "function" ? t : ge(t), i = e == null ? Rr : typeof e == "function" ? e : me(e);
  return this.select(function() {
    return this.insertBefore(n.apply(this, arguments), i.apply(this, arguments) || null);
  });
}
function Ir() {
  var t = this.parentNode;
  t && t.removeChild(this);
}
function Dr() {
  return this.each(Ir);
}
function Br() {
  var t = this.cloneNode(!1), e = this.parentNode;
  return e ? e.insertBefore(t, this.nextSibling) : t;
}
function zr() {
  var t = this.cloneNode(!0), e = this.parentNode;
  return e ? e.insertBefore(t, this.nextSibling) : t;
}
function Fr(t) {
  return this.select(t ? zr : Br);
}
function Hr(t) {
  return arguments.length ? this.property("__data__", t) : this.node().__data__;
}
function Wr(t) {
  return function(e) {
    t.call(this, e, this.__data__);
  };
}
function Or(t) {
  return t.trim().split(/^|\s+/).map(function(e) {
    var n = "", i = e.indexOf(".");
    return i >= 0 && (n = e.slice(i + 1), e = e.slice(0, i)), { type: e, name: n };
  });
}
function Vr(t) {
  return function() {
    var e = this.__on;
    if (e) {
      for (var n = 0, i = -1, r = e.length, s; n < r; ++n)
        s = e[n], (!t.type || s.type === t.type) && s.name === t.name ? this.removeEventListener(s.type, s.listener, s.options) : e[++i] = s;
      ++i ? e.length = i : delete this.__on;
    }
  };
}
function qr(t, e, n) {
  return function() {
    var i = this.__on, r, s = Wr(e);
    if (i) {
      for (var o = 0, a = i.length; o < a; ++o)
        if ((r = i[o]).type === t.type && r.name === t.name) {
          this.removeEventListener(r.type, r.listener, r.options), this.addEventListener(r.type, r.listener = s, r.options = n), r.value = e;
          return;
        }
    }
    this.addEventListener(t.type, s, n), r = { type: t.type, name: t.name, value: e, listener: s, options: n }, i ? i.push(r) : this.__on = [r];
  };
}
function Xr(t, e, n) {
  var i = Or(t + ""), r, s = i.length, o;
  if (arguments.length < 2) {
    var a = this.node().__on;
    if (a) {
      for (var c = 0, l = a.length, h; c < l; ++c)
        for (r = 0, h = a[c]; r < s; ++r)
          if ((o = i[r]).type === h.type && o.name === h.name)
            return h.value;
    }
    return;
  }
  for (a = e ? qr : Vr, r = 0; r < s; ++r) this.each(a(i[r], e, n));
  return this;
}
function $n(t, e, n) {
  var i = _n(t), r = i.CustomEvent;
  typeof r == "function" ? r = new r(e, n) : (r = i.document.createEvent("Event"), n ? (r.initEvent(e, n.bubbles, n.cancelable), r.detail = n.detail) : r.initEvent(e, !1, !1)), t.dispatchEvent(r);
}
function Gr(t, e) {
  return function() {
    return $n(this, t, e);
  };
}
function Yr(t, e) {
  return function() {
    return $n(this, t, e.apply(this, arguments));
  };
}
function Zr(t, e) {
  return this.each((typeof e == "function" ? Yr : Gr)(t, e));
}
function* Kr() {
  for (var t = this._groups, e = 0, n = t.length; e < n; ++e)
    for (var i = t[e], r = 0, s = i.length, o; r < s; ++r)
      (o = i[r]) && (yield o);
}
var An = [null];
function k(t, e) {
  this._groups = t, this._parents = e;
}
function yt() {
  return new k([[document.documentElement]], An);
}
function Qr() {
  return this;
}
k.prototype = yt.prototype = {
  constructor: k,
  select: $i,
  selectAll: Si,
  selectChild: Ti,
  selectChildren: Ui,
  filter: Ii,
  data: Wi,
  enter: Di,
  exit: Vi,
  join: qi,
  merge: Xi,
  selection: Qr,
  order: Gi,
  sort: Yi,
  call: Ki,
  nodes: Qi,
  node: Ji,
  size: ji,
  empty: tr,
  each: er,
  attr: lr,
  style: fr,
  property: mr,
  classed: br,
  text: Ar,
  html: Cr,
  raise: Nr,
  lower: Lr,
  append: Pr,
  insert: Ur,
  remove: Dr,
  clone: Fr,
  datum: Hr,
  on: Xr,
  dispatch: Zr,
  [Symbol.iterator]: Kr
};
function _e(t) {
  return typeof t == "string" ? new k([[document.querySelector(t)]], [document.documentElement]) : new k([[t]], An);
}
function Jr(t) {
  return _e(ge(t).call(document.documentElement));
}
function Pe(t) {
  return new k([document.querySelectorAll(t)], [document.documentElement]);
}
function xe(t, e, n) {
  t.prototype = e.prototype = n, n.constructor = t;
}
function kn(t, e) {
  var n = Object.create(t.prototype);
  for (var i in e) n[i] = e[i];
  return n;
}
function _t() {
}
var ht = 0.7, Ut = 1 / ht, Z = "\\s*([+-]?\\d+)\\s*", ft = "\\s*([+-]?(?:\\d*\\.)?\\d+(?:[eE][+-]?\\d+)?)\\s*", T = "\\s*([+-]?(?:\\d*\\.)?\\d+(?:[eE][+-]?\\d+)?)%\\s*", jr = /^#([0-9a-f]{3,8})$/, ts = new RegExp(`^rgb\\(${Z},${Z},${Z}\\)$`), es = new RegExp(`^rgb\\(${T},${T},${T}\\)$`), ns = new RegExp(`^rgba\\(${Z},${Z},${Z},${ft}\\)$`), is = new RegExp(`^rgba\\(${T},${T},${T},${ft}\\)$`), rs = new RegExp(`^hsl\\(${ft},${T},${T}\\)$`), ss = new RegExp(`^hsla\\(${ft},${T},${T},${ft}\\)$`), Re = {
  aliceblue: 15792383,
  antiquewhite: 16444375,
  aqua: 65535,
  aquamarine: 8388564,
  azure: 15794175,
  beige: 16119260,
  bisque: 16770244,
  black: 0,
  blanchedalmond: 16772045,
  blue: 255,
  blueviolet: 9055202,
  brown: 10824234,
  burlywood: 14596231,
  cadetblue: 6266528,
  chartreuse: 8388352,
  chocolate: 13789470,
  coral: 16744272,
  cornflowerblue: 6591981,
  cornsilk: 16775388,
  crimson: 14423100,
  cyan: 65535,
  darkblue: 139,
  darkcyan: 35723,
  darkgoldenrod: 12092939,
  darkgray: 11119017,
  darkgreen: 25600,
  darkgrey: 11119017,
  darkkhaki: 12433259,
  darkmagenta: 9109643,
  darkolivegreen: 5597999,
  darkorange: 16747520,
  darkorchid: 10040012,
  darkred: 9109504,
  darksalmon: 15308410,
  darkseagreen: 9419919,
  darkslateblue: 4734347,
  darkslategray: 3100495,
  darkslategrey: 3100495,
  darkturquoise: 52945,
  darkviolet: 9699539,
  deeppink: 16716947,
  deepskyblue: 49151,
  dimgray: 6908265,
  dimgrey: 6908265,
  dodgerblue: 2003199,
  firebrick: 11674146,
  floralwhite: 16775920,
  forestgreen: 2263842,
  fuchsia: 16711935,
  gainsboro: 14474460,
  ghostwhite: 16316671,
  gold: 16766720,
  goldenrod: 14329120,
  gray: 8421504,
  green: 32768,
  greenyellow: 11403055,
  grey: 8421504,
  honeydew: 15794160,
  hotpink: 16738740,
  indianred: 13458524,
  indigo: 4915330,
  ivory: 16777200,
  khaki: 15787660,
  lavender: 15132410,
  lavenderblush: 16773365,
  lawngreen: 8190976,
  lemonchiffon: 16775885,
  lightblue: 11393254,
  lightcoral: 15761536,
  lightcyan: 14745599,
  lightgoldenrodyellow: 16448210,
  lightgray: 13882323,
  lightgreen: 9498256,
  lightgrey: 13882323,
  lightpink: 16758465,
  lightsalmon: 16752762,
  lightseagreen: 2142890,
  lightskyblue: 8900346,
  lightslategray: 7833753,
  lightslategrey: 7833753,
  lightsteelblue: 11584734,
  lightyellow: 16777184,
  lime: 65280,
  limegreen: 3329330,
  linen: 16445670,
  magenta: 16711935,
  maroon: 8388608,
  mediumaquamarine: 6737322,
  mediumblue: 205,
  mediumorchid: 12211667,
  mediumpurple: 9662683,
  mediumseagreen: 3978097,
  mediumslateblue: 8087790,
  mediumspringgreen: 64154,
  mediumturquoise: 4772300,
  mediumvioletred: 13047173,
  midnightblue: 1644912,
  mintcream: 16121850,
  mistyrose: 16770273,
  moccasin: 16770229,
  navajowhite: 16768685,
  navy: 128,
  oldlace: 16643558,
  olive: 8421376,
  olivedrab: 7048739,
  orange: 16753920,
  orangered: 16729344,
  orchid: 14315734,
  palegoldenrod: 15657130,
  palegreen: 10025880,
  paleturquoise: 11529966,
  palevioletred: 14381203,
  papayawhip: 16773077,
  peachpuff: 16767673,
  peru: 13468991,
  pink: 16761035,
  plum: 14524637,
  powderblue: 11591910,
  purple: 8388736,
  rebeccapurple: 6697881,
  red: 16711680,
  rosybrown: 12357519,
  royalblue: 4286945,
  saddlebrown: 9127187,
  salmon: 16416882,
  sandybrown: 16032864,
  seagreen: 3050327,
  seashell: 16774638,
  sienna: 10506797,
  silver: 12632256,
  skyblue: 8900331,
  slateblue: 6970061,
  slategray: 7372944,
  slategrey: 7372944,
  snow: 16775930,
  springgreen: 65407,
  steelblue: 4620980,
  tan: 13808780,
  teal: 32896,
  thistle: 14204888,
  tomato: 16737095,
  turquoise: 4251856,
  violet: 15631086,
  wheat: 16113331,
  white: 16777215,
  whitesmoke: 16119285,
  yellow: 16776960,
  yellowgreen: 10145074
};
xe(_t, q, {
  copy(t) {
    return Object.assign(new this.constructor(), this, t);
  },
  displayable() {
    return this.rgb().displayable();
  },
  hex: Ue,
  // Deprecated! Use color.formatHex.
  formatHex: Ue,
  formatHex8: os,
  formatHsl: as,
  formatRgb: Ie,
  toString: Ie
});
function Ue() {
  return this.rgb().formatHex();
}
function os() {
  return this.rgb().formatHex8();
}
function as() {
  return Mn(this).formatHsl();
}
function Ie() {
  return this.rgb().formatRgb();
}
function q(t) {
  var e, n;
  return t = (t + "").trim().toLowerCase(), (e = jr.exec(t)) ? (n = e[1].length, e = parseInt(e[1], 16), n === 6 ? De(e) : n === 3 ? new A(e >> 8 & 15 | e >> 4 & 240, e >> 4 & 15 | e & 240, (e & 15) << 4 | e & 15, 1) : n === 8 ? At(e >> 24 & 255, e >> 16 & 255, e >> 8 & 255, (e & 255) / 255) : n === 4 ? At(e >> 12 & 15 | e >> 8 & 240, e >> 8 & 15 | e >> 4 & 240, e >> 4 & 15 | e & 240, ((e & 15) << 4 | e & 15) / 255) : null) : (e = ts.exec(t)) ? new A(e[1], e[2], e[3], 1) : (e = es.exec(t)) ? new A(e[1] * 255 / 100, e[2] * 255 / 100, e[3] * 255 / 100, 1) : (e = ns.exec(t)) ? At(e[1], e[2], e[3], e[4]) : (e = is.exec(t)) ? At(e[1] * 255 / 100, e[2] * 255 / 100, e[3] * 255 / 100, e[4]) : (e = rs.exec(t)) ? Fe(e[1], e[2] / 100, e[3] / 100, 1) : (e = ss.exec(t)) ? Fe(e[1], e[2] / 100, e[3] / 100, e[4]) : Re.hasOwnProperty(t) ? De(Re[t]) : t === "transparent" ? new A(NaN, NaN, NaN, 0) : null;
}
function De(t) {
  return new A(t >> 16 & 255, t >> 8 & 255, t & 255, 1);
}
function At(t, e, n, i) {
  return i <= 0 && (t = e = n = NaN), new A(t, e, n, i);
}
function ls(t) {
  return t instanceof _t || (t = q(t)), t ? (t = t.rgb(), new A(t.r, t.g, t.b, t.opacity)) : new A();
}
function re(t, e, n, i) {
  return arguments.length === 1 ? ls(t) : new A(t, e, n, i ?? 1);
}
function A(t, e, n, i) {
  this.r = +t, this.g = +e, this.b = +n, this.opacity = +i;
}
xe(A, re, kn(_t, {
  brighter(t) {
    return t = t == null ? Ut : Math.pow(Ut, t), new A(this.r * t, this.g * t, this.b * t, this.opacity);
  },
  darker(t) {
    return t = t == null ? ht : Math.pow(ht, t), new A(this.r * t, this.g * t, this.b * t, this.opacity);
  },
  rgb() {
    return this;
  },
  clamp() {
    return new A(V(this.r), V(this.g), V(this.b), It(this.opacity));
  },
  displayable() {
    return -0.5 <= this.r && this.r < 255.5 && -0.5 <= this.g && this.g < 255.5 && -0.5 <= this.b && this.b < 255.5 && 0 <= this.opacity && this.opacity <= 1;
  },
  hex: Be,
  // Deprecated! Use color.formatHex.
  formatHex: Be,
  formatHex8: cs,
  formatRgb: ze,
  toString: ze
}));
function Be() {
  return `#${W(this.r)}${W(this.g)}${W(this.b)}`;
}
function cs() {
  return `#${W(this.r)}${W(this.g)}${W(this.b)}${W((isNaN(this.opacity) ? 1 : this.opacity) * 255)}`;
}
function ze() {
  const t = It(this.opacity);
  return `${t === 1 ? "rgb(" : "rgba("}${V(this.r)}, ${V(this.g)}, ${V(this.b)}${t === 1 ? ")" : `, ${t})`}`;
}
function It(t) {
  return isNaN(t) ? 1 : Math.max(0, Math.min(1, t));
}
function V(t) {
  return Math.max(0, Math.min(255, Math.round(t) || 0));
}
function W(t) {
  return t = V(t), (t < 16 ? "0" : "") + t.toString(16);
}
function Fe(t, e, n, i) {
  return i <= 0 ? t = e = n = NaN : n <= 0 || n >= 1 ? t = e = NaN : e <= 0 && (t = NaN), new E(t, e, n, i);
}
function Mn(t) {
  if (t instanceof E) return new E(t.h, t.s, t.l, t.opacity);
  if (t instanceof _t || (t = q(t)), !t) return new E();
  if (t instanceof E) return t;
  t = t.rgb();
  var e = t.r / 255, n = t.g / 255, i = t.b / 255, r = Math.min(e, n, i), s = Math.max(e, n, i), o = NaN, a = s - r, c = (s + r) / 2;
  return a ? (e === s ? o = (n - i) / a + (n < i) * 6 : n === s ? o = (i - e) / a + 2 : o = (e - n) / a + 4, a /= c < 0.5 ? s + r : 2 - s - r, o *= 60) : a = c > 0 && c < 1 ? 0 : o, new E(o, a, c, t.opacity);
}
function us(t, e, n, i) {
  return arguments.length === 1 ? Mn(t) : new E(t, e, n, i ?? 1);
}
function E(t, e, n, i) {
  this.h = +t, this.s = +e, this.l = +n, this.opacity = +i;
}
xe(E, us, kn(_t, {
  brighter(t) {
    return t = t == null ? Ut : Math.pow(Ut, t), new E(this.h, this.s, this.l * t, this.opacity);
  },
  darker(t) {
    return t = t == null ? ht : Math.pow(ht, t), new E(this.h, this.s, this.l * t, this.opacity);
  },
  rgb() {
    var t = this.h % 360 + (this.h < 0) * 360, e = isNaN(t) || isNaN(this.s) ? 0 : this.s, n = this.l, i = n + (n < 0.5 ? n : 1 - n) * e, r = 2 * n - i;
    return new A(
      Kt(t >= 240 ? t - 240 : t + 120, r, i),
      Kt(t, r, i),
      Kt(t < 120 ? t + 240 : t - 120, r, i),
      this.opacity
    );
  },
  clamp() {
    return new E(He(this.h), kt(this.s), kt(this.l), It(this.opacity));
  },
  displayable() {
    return (0 <= this.s && this.s <= 1 || isNaN(this.s)) && 0 <= this.l && this.l <= 1 && 0 <= this.opacity && this.opacity <= 1;
  },
  formatHsl() {
    const t = It(this.opacity);
    return `${t === 1 ? "hsl(" : "hsla("}${He(this.h)}, ${kt(this.s) * 100}%, ${kt(this.l) * 100}%${t === 1 ? ")" : `, ${t})`}`;
  }
}));
function He(t) {
  return t = (t || 0) % 360, t < 0 ? t + 360 : t;
}
function kt(t) {
  return Math.max(0, Math.min(1, t || 0));
}
function Kt(t, e, n) {
  return (t < 60 ? e + (n - e) * t / 60 : t < 180 ? n : t < 240 ? e + (n - e) * (240 - t) / 60 : e) * 255;
}
const be = (t) => () => t;
function hs(t, e) {
  return function(n) {
    return t + n * e;
  };
}
function fs(t, e, n) {
  return t = Math.pow(t, n), e = Math.pow(e, n) - t, n = 1 / n, function(i) {
    return Math.pow(t + i * e, n);
  };
}
function ds(t) {
  return (t = +t) == 1 ? Sn : function(e, n) {
    return n - e ? fs(e, n, t) : be(isNaN(e) ? n : e);
  };
}
function Sn(t, e) {
  var n = e - t;
  return n ? hs(t, n) : be(isNaN(t) ? e : t);
}
const Q = function t(e) {
  var n = ds(e);
  function i(r, s) {
    var o = n((r = re(r)).r, (s = re(s)).r), a = n(r.g, s.g), c = n(r.b, s.b), l = Sn(r.opacity, s.opacity);
    return function(h) {
      return r.r = o(h), r.g = a(h), r.b = c(h), r.opacity = l(h), r + "";
    };
  }
  return i.gamma = t, i;
}(1);
function ps(t, e) {
  e || (e = []);
  var n = t ? Math.min(e.length, t.length) : 0, i = e.slice(), r;
  return function(s) {
    for (r = 0; r < n; ++r) i[r] = t[r] * (1 - s) + e[r] * s;
    return i;
  };
}
function gs(t) {
  return ArrayBuffer.isView(t) && !(t instanceof DataView);
}
function ms(t, e) {
  var n = e ? e.length : 0, i = t ? Math.min(n, t.length) : 0, r = new Array(i), s = new Array(n), o;
  for (o = 0; o < i; ++o) r[o] = Vt(t[o], e[o]);
  for (; o < n; ++o) s[o] = e[o];
  return function(a) {
    for (o = 0; o < i; ++o) s[o] = r[o](a);
    return s;
  };
}
function ys(t, e) {
  var n = /* @__PURE__ */ new Date();
  return t = +t, e = +e, function(i) {
    return n.setTime(t * (1 - i) + e * i), n;
  };
}
function C(t, e) {
  return t = +t, e = +e, function(n) {
    return t * (1 - n) + e * n;
  };
}
function _s(t, e) {
  var n = {}, i = {}, r;
  (t === null || typeof t != "object") && (t = {}), (e === null || typeof e != "object") && (e = {});
  for (r in e)
    r in t ? n[r] = Vt(t[r], e[r]) : i[r] = e[r];
  return function(s) {
    for (r in n) i[r] = n[r](s);
    return i;
  };
}
var se = /[-+]?(?:\d+\.?\d*|\.?\d+)(?:[eE][-+]?\d+)?/g, Qt = new RegExp(se.source, "g");
function xs(t) {
  return function() {
    return t;
  };
}
function bs(t) {
  return function(e) {
    return t(e) + "";
  };
}
function Cn(t, e) {
  var n = se.lastIndex = Qt.lastIndex = 0, i, r, s, o = -1, a = [], c = [];
  for (t = t + "", e = e + ""; (i = se.exec(t)) && (r = Qt.exec(e)); )
    (s = r.index) > n && (s = e.slice(n, s), a[o] ? a[o] += s : a[++o] = s), (i = i[0]) === (r = r[0]) ? a[o] ? a[o] += r : a[++o] = r : (a[++o] = null, c.push({ i: o, x: C(i, r) })), n = Qt.lastIndex;
  return n < e.length && (s = e.slice(n), a[o] ? a[o] += s : a[++o] = s), a.length < 2 ? c[0] ? bs(c[0].x) : xs(e) : (e = c.length, function(l) {
    for (var h = 0, u; h < e; ++h) a[(u = c[h]).i] = u.x(l);
    return a.join("");
  });
}
function Vt(t, e) {
  var n = typeof e, i;
  return e == null || n === "boolean" ? be(e) : (n === "number" ? C : n === "string" ? (i = q(e)) ? (e = i, Q) : Cn : e instanceof q ? Q : e instanceof Date ? ys : gs(e) ? ps : Array.isArray(e) ? ms : typeof e.valueOf != "function" && typeof e.toString != "function" || isNaN(e) ? _s : C)(t, e);
}
function En(t, e) {
  return t = +t, e = +e, function(n) {
    return Math.round(t * (1 - n) + e * n);
  };
}
var We = 180 / Math.PI, oe = {
  translateX: 0,
  translateY: 0,
  rotate: 0,
  skewX: 0,
  scaleX: 1,
  scaleY: 1
};
function Nn(t, e, n, i, r, s) {
  var o, a, c;
  return (o = Math.sqrt(t * t + e * e)) && (t /= o, e /= o), (c = t * n + e * i) && (n -= t * c, i -= e * c), (a = Math.sqrt(n * n + i * i)) && (n /= a, i /= a, c /= a), t * i < e * n && (t = -t, e = -e, c = -c, o = -o), {
    translateX: r,
    translateY: s,
    rotate: Math.atan2(e, t) * We,
    skewX: Math.atan(c) * We,
    scaleX: o,
    scaleY: a
  };
}
var Mt;
function vs(t) {
  const e = new (typeof DOMMatrix == "function" ? DOMMatrix : WebKitCSSMatrix)(t + "");
  return e.isIdentity ? oe : Nn(e.a, e.b, e.c, e.d, e.e, e.f);
}
function ws(t) {
  return t == null || (Mt || (Mt = document.createElementNS("http://www.w3.org/2000/svg", "g")), Mt.setAttribute("transform", t), !(t = Mt.transform.baseVal.consolidate())) ? oe : (t = t.matrix, Nn(t.a, t.b, t.c, t.d, t.e, t.f));
}
function Tn(t, e, n, i) {
  function r(l) {
    return l.length ? l.pop() + " " : "";
  }
  function s(l, h, u, f, d, p) {
    if (l !== u || h !== f) {
      var g = d.push("translate(", null, e, null, n);
      p.push({ i: g - 4, x: C(l, u) }, { i: g - 2, x: C(h, f) });
    } else (u || f) && d.push("translate(" + u + e + f + n);
  }
  function o(l, h, u, f) {
    l !== h ? (l - h > 180 ? h += 360 : h - l > 180 && (l += 360), f.push({ i: u.push(r(u) + "rotate(", null, i) - 2, x: C(l, h) })) : h && u.push(r(u) + "rotate(" + h + i);
  }
  function a(l, h, u, f) {
    l !== h ? f.push({ i: u.push(r(u) + "skewX(", null, i) - 2, x: C(l, h) }) : h && u.push(r(u) + "skewX(" + h + i);
  }
  function c(l, h, u, f, d, p) {
    if (l !== u || h !== f) {
      var g = d.push(r(d) + "scale(", null, ",", null, ")");
      p.push({ i: g - 4, x: C(l, u) }, { i: g - 2, x: C(h, f) });
    } else (u !== 1 || f !== 1) && d.push(r(d) + "scale(" + u + "," + f + ")");
  }
  return function(l, h) {
    var u = [], f = [];
    return l = t(l), h = t(h), s(l.translateX, l.translateY, h.translateX, h.translateY, u, f), o(l.rotate, h.rotate, u, f), a(l.skewX, h.skewX, u, f), c(l.scaleX, l.scaleY, h.scaleX, h.scaleY, u, f), l = h = null, function(d) {
      for (var p = -1, g = f.length, y; ++p < g; ) u[(y = f[p]).i] = y.x(d);
      return u.join("");
    };
  };
}
var $s = Tn(vs, "px, ", "px)", "deg)"), As = Tn(ws, ", ", ")", ")"), J = 0, ot = 0, rt = 0, Ln = 1e3, Dt, at, Bt = 0, X = 0, qt = 0, dt = typeof performance == "object" && performance.now ? performance : Date, Pn = typeof window == "object" && window.requestAnimationFrame ? window.requestAnimationFrame.bind(window) : function(t) {
  setTimeout(t, 17);
};
function ve() {
  return X || (Pn(ks), X = dt.now() + qt);
}
function ks() {
  X = 0;
}
function zt() {
  this._call = this._time = this._next = null;
}
zt.prototype = Rn.prototype = {
  constructor: zt,
  restart: function(t, e, n) {
    if (typeof t != "function") throw new TypeError("callback is not a function");
    n = (n == null ? ve() : +n) + (e == null ? 0 : +e), !this._next && at !== this && (at ? at._next = this : Dt = this, at = this), this._call = t, this._time = n, ae();
  },
  stop: function() {
    this._call && (this._call = null, this._time = 1 / 0, ae());
  }
};
function Rn(t, e, n) {
  var i = new zt();
  return i.restart(t, e, n), i;
}
function Ms() {
  ve(), ++J;
  for (var t = Dt, e; t; )
    (e = X - t._time) >= 0 && t._call.call(void 0, e), t = t._next;
  --J;
}
function Oe() {
  X = (Bt = dt.now()) + qt, J = ot = 0;
  try {
    Ms();
  } finally {
    J = 0, Cs(), X = 0;
  }
}
function Ss() {
  var t = dt.now(), e = t - Bt;
  e > Ln && (qt -= e, Bt = t);
}
function Cs() {
  for (var t, e = Dt, n, i = 1 / 0; e; )
    e._call ? (i > e._time && (i = e._time), t = e, e = e._next) : (n = e._next, e._next = null, e = t ? t._next = n : Dt = n);
  at = t, ae(i);
}
function ae(t) {
  if (!J) {
    ot && (ot = clearTimeout(ot));
    var e = t - X;
    e > 24 ? (t < 1 / 0 && (ot = setTimeout(Oe, t - dt.now() - qt)), rt && (rt = clearInterval(rt))) : (rt || (Bt = dt.now(), rt = setInterval(Ss, Ln)), J = 1, Pn(Oe));
  }
}
function Ve(t, e, n) {
  var i = new zt();
  return e = e == null ? 0 : +e, i.restart((r) => {
    i.stop(), t(r + e);
  }, e, n), i;
}
var Es = dn("start", "end", "cancel", "interrupt"), Ns = [], Un = 0, qe = 1, le = 2, Tt = 3, Xe = 4, ce = 5, Lt = 6;
function Xt(t, e, n, i, r, s) {
  var o = t.__transition;
  if (!o) t.__transition = {};
  else if (n in o) return;
  Ts(t, n, {
    name: e,
    index: i,
    // For context during callback.
    group: r,
    // For context during callback.
    on: Es,
    tween: Ns,
    time: s.time,
    delay: s.delay,
    duration: s.duration,
    ease: s.ease,
    timer: null,
    state: Un
  });
}
function we(t, e) {
  var n = N(t, e);
  if (n.state > Un) throw new Error("too late; already scheduled");
  return n;
}
function P(t, e) {
  var n = N(t, e);
  if (n.state > Tt) throw new Error("too late; already running");
  return n;
}
function N(t, e) {
  var n = t.__transition;
  if (!n || !(n = n[e])) throw new Error("transition not found");
  return n;
}
function Ts(t, e, n) {
  var i = t.__transition, r;
  i[e] = n, n.timer = Rn(s, 0, n.time);
  function s(l) {
    n.state = qe, n.timer.restart(o, n.delay, n.time), n.delay <= l && o(l - n.delay);
  }
  function o(l) {
    var h, u, f, d;
    if (n.state !== qe) return c();
    for (h in i)
      if (d = i[h], d.name === n.name) {
        if (d.state === Tt) return Ve(o);
        d.state === Xe ? (d.state = Lt, d.timer.stop(), d.on.call("interrupt", t, t.__data__, d.index, d.group), delete i[h]) : +h < e && (d.state = Lt, d.timer.stop(), d.on.call("cancel", t, t.__data__, d.index, d.group), delete i[h]);
      }
    if (Ve(function() {
      n.state === Tt && (n.state = Xe, n.timer.restart(a, n.delay, n.time), a(l));
    }), n.state = le, n.on.call("start", t, t.__data__, n.index, n.group), n.state === le) {
      for (n.state = Tt, r = new Array(f = n.tween.length), h = 0, u = -1; h < f; ++h)
        (d = n.tween[h].value.call(t, t.__data__, n.index, n.group)) && (r[++u] = d);
      r.length = u + 1;
    }
  }
  function a(l) {
    for (var h = l < n.duration ? n.ease.call(null, l / n.duration) : (n.timer.restart(c), n.state = ce, 1), u = -1, f = r.length; ++u < f; )
      r[u].call(t, h);
    n.state === ce && (n.on.call("end", t, t.__data__, n.index, n.group), c());
  }
  function c() {
    n.state = Lt, n.timer.stop(), delete i[e];
    for (var l in i) return;
    delete t.__transition;
  }
}
function Ls(t, e) {
  var n = t.__transition, i, r, s = !0, o;
  if (n) {
    e = e == null ? null : e + "";
    for (o in n) {
      if ((i = n[o]).name !== e) {
        s = !1;
        continue;
      }
      r = i.state > le && i.state < ce, i.state = Lt, i.timer.stop(), i.on.call(r ? "interrupt" : "cancel", t, t.__data__, i.index, i.group), delete n[o];
    }
    s && delete t.__transition;
  }
}
function Ps(t) {
  return this.each(function() {
    Ls(this, t);
  });
}
function Rs(t, e) {
  var n, i;
  return function() {
    var r = P(this, t), s = r.tween;
    if (s !== n) {
      i = n = s;
      for (var o = 0, a = i.length; o < a; ++o)
        if (i[o].name === e) {
          i = i.slice(), i.splice(o, 1);
          break;
        }
    }
    r.tween = i;
  };
}
function Us(t, e, n) {
  var i, r;
  if (typeof n != "function") throw new Error();
  return function() {
    var s = P(this, t), o = s.tween;
    if (o !== i) {
      r = (i = o).slice();
      for (var a = { name: e, value: n }, c = 0, l = r.length; c < l; ++c)
        if (r[c].name === e) {
          r[c] = a;
          break;
        }
      c === l && r.push(a);
    }
    s.tween = r;
  };
}
function Is(t, e) {
  var n = this._id;
  if (t += "", arguments.length < 2) {
    for (var i = N(this.node(), n).tween, r = 0, s = i.length, o; r < s; ++r)
      if ((o = i[r]).name === t)
        return o.value;
    return null;
  }
  return this.each((e == null ? Rs : Us)(n, t, e));
}
function $e(t, e, n) {
  var i = t._id;
  return t.each(function() {
    var r = P(this, i);
    (r.value || (r.value = {}))[e] = n.apply(this, arguments);
  }), function(r) {
    return N(r, i).value[e];
  };
}
function In(t, e) {
  var n;
  return (typeof e == "number" ? C : e instanceof q ? Q : (n = q(e)) ? (e = n, Q) : Cn)(t, e);
}
function Ds(t) {
  return function() {
    this.removeAttribute(t);
  };
}
function Bs(t) {
  return function() {
    this.removeAttributeNS(t.space, t.local);
  };
}
function zs(t, e, n) {
  var i, r = n + "", s;
  return function() {
    var o = this.getAttribute(t);
    return o === r ? null : o === i ? s : s = e(i = o, n);
  };
}
function Fs(t, e, n) {
  var i, r = n + "", s;
  return function() {
    var o = this.getAttributeNS(t.space, t.local);
    return o === r ? null : o === i ? s : s = e(i = o, n);
  };
}
function Hs(t, e, n) {
  var i, r, s;
  return function() {
    var o, a = n(this), c;
    return a == null ? void this.removeAttribute(t) : (o = this.getAttribute(t), c = a + "", o === c ? null : o === i && c === r ? s : (r = c, s = e(i = o, a)));
  };
}
function Ws(t, e, n) {
  var i, r, s;
  return function() {
    var o, a = n(this), c;
    return a == null ? void this.removeAttributeNS(t.space, t.local) : (o = this.getAttributeNS(t.space, t.local), c = a + "", o === c ? null : o === i && c === r ? s : (r = c, s = e(i = o, a)));
  };
}
function Os(t, e) {
  var n = Ot(t), i = n === "transform" ? As : In;
  return this.attrTween(t, typeof e == "function" ? (n.local ? Ws : Hs)(n, i, $e(this, "attr." + t, e)) : e == null ? (n.local ? Bs : Ds)(n) : (n.local ? Fs : zs)(n, i, e));
}
function Vs(t, e) {
  return function(n) {
    this.setAttribute(t, e.call(this, n));
  };
}
function qs(t, e) {
  return function(n) {
    this.setAttributeNS(t.space, t.local, e.call(this, n));
  };
}
function Xs(t, e) {
  var n, i;
  function r() {
    var s = e.apply(this, arguments);
    return s !== i && (n = (i = s) && qs(t, s)), n;
  }
  return r._value = e, r;
}
function Gs(t, e) {
  var n, i;
  function r() {
    var s = e.apply(this, arguments);
    return s !== i && (n = (i = s) && Vs(t, s)), n;
  }
  return r._value = e, r;
}
function Ys(t, e) {
  var n = "attr." + t;
  if (arguments.length < 2) return (n = this.tween(n)) && n._value;
  if (e == null) return this.tween(n, null);
  if (typeof e != "function") throw new Error();
  var i = Ot(t);
  return this.tween(n, (i.local ? Xs : Gs)(i, e));
}
function Zs(t, e) {
  return function() {
    we(this, t).delay = +e.apply(this, arguments);
  };
}
function Ks(t, e) {
  return e = +e, function() {
    we(this, t).delay = e;
  };
}
function Qs(t) {
  var e = this._id;
  return arguments.length ? this.each((typeof t == "function" ? Zs : Ks)(e, t)) : N(this.node(), e).delay;
}
function Js(t, e) {
  return function() {
    P(this, t).duration = +e.apply(this, arguments);
  };
}
function js(t, e) {
  return e = +e, function() {
    P(this, t).duration = e;
  };
}
function to(t) {
  var e = this._id;
  return arguments.length ? this.each((typeof t == "function" ? Js : js)(e, t)) : N(this.node(), e).duration;
}
function eo(t, e) {
  if (typeof e != "function") throw new Error();
  return function() {
    P(this, t).ease = e;
  };
}
function no(t) {
  var e = this._id;
  return arguments.length ? this.each(eo(e, t)) : N(this.node(), e).ease;
}
function io(t, e) {
  return function() {
    var n = e.apply(this, arguments);
    if (typeof n != "function") throw new Error();
    P(this, t).ease = n;
  };
}
function ro(t) {
  if (typeof t != "function") throw new Error();
  return this.each(io(this._id, t));
}
function so(t) {
  typeof t != "function" && (t = gn(t));
  for (var e = this._groups, n = e.length, i = new Array(n), r = 0; r < n; ++r)
    for (var s = e[r], o = s.length, a = i[r] = [], c, l = 0; l < o; ++l)
      (c = s[l]) && t.call(c, c.__data__, l, s) && a.push(c);
  return new I(i, this._parents, this._name, this._id);
}
function oo(t) {
  if (t._id !== this._id) throw new Error();
  for (var e = this._groups, n = t._groups, i = e.length, r = n.length, s = Math.min(i, r), o = new Array(i), a = 0; a < s; ++a)
    for (var c = e[a], l = n[a], h = c.length, u = o[a] = new Array(h), f, d = 0; d < h; ++d)
      (f = c[d] || l[d]) && (u[d] = f);
  for (; a < i; ++a)
    o[a] = e[a];
  return new I(o, this._parents, this._name, this._id);
}
function ao(t) {
  return (t + "").trim().split(/^|\s+/).every(function(e) {
    var n = e.indexOf(".");
    return n >= 0 && (e = e.slice(0, n)), !e || e === "start";
  });
}
function lo(t, e, n) {
  var i, r, s = ao(e) ? we : P;
  return function() {
    var o = s(this, t), a = o.on;
    a !== i && (r = (i = a).copy()).on(e, n), o.on = r;
  };
}
function co(t, e) {
  var n = this._id;
  return arguments.length < 2 ? N(this.node(), n).on.on(t) : this.each(lo(n, t, e));
}
function uo(t) {
  return function() {
    var e = this.parentNode;
    for (var n in this.__transition) if (+n !== t) return;
    e && e.removeChild(this);
  };
}
function ho() {
  return this.on("end.remove", uo(this._id));
}
function fo(t) {
  var e = this._name, n = this._id;
  typeof t != "function" && (t = me(t));
  for (var i = this._groups, r = i.length, s = new Array(r), o = 0; o < r; ++o)
    for (var a = i[o], c = a.length, l = s[o] = new Array(c), h, u, f = 0; f < c; ++f)
      (h = a[f]) && (u = t.call(h, h.__data__, f, a)) && ("__data__" in h && (u.__data__ = h.__data__), l[f] = u, Xt(l[f], e, n, f, l, N(h, n)));
  return new I(s, this._parents, e, n);
}
function po(t) {
  var e = this._name, n = this._id;
  typeof t != "function" && (t = pn(t));
  for (var i = this._groups, r = i.length, s = [], o = [], a = 0; a < r; ++a)
    for (var c = i[a], l = c.length, h, u = 0; u < l; ++u)
      if (h = c[u]) {
        for (var f = t.call(h, h.__data__, u, c), d, p = N(h, n), g = 0, y = f.length; g < y; ++g)
          (d = f[g]) && Xt(d, e, n, g, f, p);
        s.push(f), o.push(h);
      }
  return new I(s, o, e, n);
}
var go = yt.prototype.constructor;
function mo() {
  return new go(this._groups, this._parents);
}
function yo(t, e) {
  var n, i, r;
  return function() {
    var s = K(this, t), o = (this.style.removeProperty(t), K(this, t));
    return s === o ? null : s === n && o === i ? r : r = e(n = s, i = o);
  };
}
function Dn(t) {
  return function() {
    this.style.removeProperty(t);
  };
}
function _o(t, e, n) {
  var i, r = n + "", s;
  return function() {
    var o = K(this, t);
    return o === r ? null : o === i ? s : s = e(i = o, n);
  };
}
function xo(t, e, n) {
  var i, r, s;
  return function() {
    var o = K(this, t), a = n(this), c = a + "";
    return a == null && (c = a = (this.style.removeProperty(t), K(this, t))), o === c ? null : o === i && c === r ? s : (r = c, s = e(i = o, a));
  };
}
function bo(t, e) {
  var n, i, r, s = "style." + e, o = "end." + s, a;
  return function() {
    var c = P(this, t), l = c.on, h = c.value[s] == null ? a || (a = Dn(e)) : void 0;
    (l !== n || r !== h) && (i = (n = l).copy()).on(o, r = h), c.on = i;
  };
}
function vo(t, e, n) {
  var i = (t += "") == "transform" ? $s : In;
  return e == null ? this.styleTween(t, yo(t, i)).on("end.style." + t, Dn(t)) : typeof e == "function" ? this.styleTween(t, xo(t, i, $e(this, "style." + t, e))).each(bo(this._id, t)) : this.styleTween(t, _o(t, i, e), n).on("end.style." + t, null);
}
function wo(t, e, n) {
  return function(i) {
    this.style.setProperty(t, e.call(this, i), n);
  };
}
function $o(t, e, n) {
  var i, r;
  function s() {
    var o = e.apply(this, arguments);
    return o !== r && (i = (r = o) && wo(t, o, n)), i;
  }
  return s._value = e, s;
}
function Ao(t, e, n) {
  var i = "style." + (t += "");
  if (arguments.length < 2) return (i = this.tween(i)) && i._value;
  if (e == null) return this.tween(i, null);
  if (typeof e != "function") throw new Error();
  return this.tween(i, $o(t, e, n ?? ""));
}
function ko(t) {
  return function() {
    this.textContent = t;
  };
}
function Mo(t) {
  return function() {
    var e = t(this);
    this.textContent = e ?? "";
  };
}
function So(t) {
  return this.tween("text", typeof t == "function" ? Mo($e(this, "text", t)) : ko(t == null ? "" : t + ""));
}
function Co(t) {
  return function(e) {
    this.textContent = t.call(this, e);
  };
}
function Eo(t) {
  var e, n;
  function i() {
    var r = t.apply(this, arguments);
    return r !== n && (e = (n = r) && Co(r)), e;
  }
  return i._value = t, i;
}
function No(t) {
  var e = "text";
  if (arguments.length < 1) return (e = this.tween(e)) && e._value;
  if (t == null) return this.tween(e, null);
  if (typeof t != "function") throw new Error();
  return this.tween(e, Eo(t));
}
function To() {
  for (var t = this._name, e = this._id, n = Bn(), i = this._groups, r = i.length, s = 0; s < r; ++s)
    for (var o = i[s], a = o.length, c, l = 0; l < a; ++l)
      if (c = o[l]) {
        var h = N(c, e);
        Xt(c, t, n, l, o, {
          time: h.time + h.delay + h.duration,
          delay: 0,
          duration: h.duration,
          ease: h.ease
        });
      }
  return new I(i, this._parents, t, n);
}
function Lo() {
  var t, e, n = this, i = n._id, r = n.size();
  return new Promise(function(s, o) {
    var a = { value: o }, c = { value: function() {
      --r === 0 && s();
    } };
    n.each(function() {
      var l = P(this, i), h = l.on;
      h !== t && (e = (t = h).copy(), e._.cancel.push(a), e._.interrupt.push(a), e._.end.push(c)), l.on = e;
    }), r === 0 && s();
  });
}
var Po = 0;
function I(t, e, n, i) {
  this._groups = t, this._parents = e, this._name = n, this._id = i;
}
function Bn() {
  return ++Po;
}
var U = yt.prototype;
I.prototype = {
  constructor: I,
  select: fo,
  selectAll: po,
  selectChild: U.selectChild,
  selectChildren: U.selectChildren,
  filter: so,
  merge: oo,
  selection: mo,
  transition: To,
  call: U.call,
  nodes: U.nodes,
  node: U.node,
  size: U.size,
  empty: U.empty,
  each: U.each,
  on: co,
  attr: Os,
  attrTween: Ys,
  style: vo,
  styleTween: Ao,
  text: So,
  textTween: No,
  remove: ho,
  tween: Is,
  delay: Qs,
  duration: to,
  ease: no,
  easeVarying: ro,
  end: Lo,
  [Symbol.iterator]: U[Symbol.iterator]
};
function Ro(t) {
  return ((t *= 2) <= 1 ? t * t * t : (t -= 2) * t * t + 2) / 2;
}
var Uo = {
  time: null,
  // Set on use.
  delay: 0,
  duration: 250,
  ease: Ro
};
function Io(t, e) {
  for (var n; !(n = t.__transition) || !(n = n[e]); )
    if (!(t = t.parentNode))
      throw new Error(`transition ${e} not found`);
  return n;
}
function Do(t) {
  var e, n;
  t instanceof I ? (e = t._id, t = t._name) : (e = Bn(), (n = Uo).time = ve(), t = t == null ? null : t + "");
  for (var i = this._groups, r = i.length, s = 0; s < r; ++s)
    for (var o = i[s], a = o.length, c, l = 0; l < a; ++l)
      (c = o[l]) && Xt(c, t, e, l, o, n || Io(c, e));
  return new I(i, this._parents, t, e);
}
yt.prototype.interrupt = Ps;
yt.prototype.transition = Do;
const ue = Math.PI, he = 2 * ue, H = 1e-6, Bo = he - H;
function zn(t) {
  this._ += t[0];
  for (let e = 1, n = t.length; e < n; ++e)
    this._ += arguments[e] + t[e];
}
function zo(t) {
  let e = Math.floor(t);
  if (!(e >= 0)) throw new Error(`invalid digits: ${t}`);
  if (e > 15) return zn;
  const n = 10 ** e;
  return function(i) {
    this._ += i[0];
    for (let r = 1, s = i.length; r < s; ++r)
      this._ += Math.round(arguments[r] * n) / n + i[r];
  };
}
class Fo {
  constructor(e) {
    this._x0 = this._y0 = // start of current subpath
    this._x1 = this._y1 = null, this._ = "", this._append = e == null ? zn : zo(e);
  }
  moveTo(e, n) {
    this._append`M${this._x0 = this._x1 = +e},${this._y0 = this._y1 = +n}`;
  }
  closePath() {
    this._x1 !== null && (this._x1 = this._x0, this._y1 = this._y0, this._append`Z`);
  }
  lineTo(e, n) {
    this._append`L${this._x1 = +e},${this._y1 = +n}`;
  }
  quadraticCurveTo(e, n, i, r) {
    this._append`Q${+e},${+n},${this._x1 = +i},${this._y1 = +r}`;
  }
  bezierCurveTo(e, n, i, r, s, o) {
    this._append`C${+e},${+n},${+i},${+r},${this._x1 = +s},${this._y1 = +o}`;
  }
  arcTo(e, n, i, r, s) {
    if (e = +e, n = +n, i = +i, r = +r, s = +s, s < 0) throw new Error(`negative radius: ${s}`);
    let o = this._x1, a = this._y1, c = i - e, l = r - n, h = o - e, u = a - n, f = h * h + u * u;
    if (this._x1 === null)
      this._append`M${this._x1 = e},${this._y1 = n}`;
    else if (f > H) if (!(Math.abs(u * c - l * h) > H) || !s)
      this._append`L${this._x1 = e},${this._y1 = n}`;
    else {
      let d = i - o, p = r - a, g = c * c + l * l, y = d * d + p * p, w = Math.sqrt(g), b = Math.sqrt(f), v = s * Math.tan((ue - Math.acos((g + f - y) / (2 * w * b))) / 2), M = v / b, _ = v / w;
      Math.abs(M - 1) > H && this._append`L${e + M * h},${n + M * u}`, this._append`A${s},${s},0,0,${+(u * d > h * p)},${this._x1 = e + _ * c},${this._y1 = n + _ * l}`;
    }
  }
  arc(e, n, i, r, s, o) {
    if (e = +e, n = +n, i = +i, o = !!o, i < 0) throw new Error(`negative radius: ${i}`);
    let a = i * Math.cos(r), c = i * Math.sin(r), l = e + a, h = n + c, u = 1 ^ o, f = o ? r - s : s - r;
    this._x1 === null ? this._append`M${l},${h}` : (Math.abs(this._x1 - l) > H || Math.abs(this._y1 - h) > H) && this._append`L${l},${h}`, i && (f < 0 && (f = f % he + he), f > Bo ? this._append`A${i},${i},0,1,${u},${e - a},${n - c}A${i},${i},0,1,${u},${this._x1 = l},${this._y1 = h}` : f > H && this._append`A${i},${i},0,${+(f >= ue)},${u},${this._x1 = e + i * Math.cos(s)},${this._y1 = n + i * Math.sin(s)}`);
  }
  rect(e, n, i, r) {
    this._append`M${this._x0 = this._x1 = +e},${this._y0 = this._y1 = +n}h${i = +i}v${+r}h${-i}Z`;
  }
  toString() {
    return this._;
  }
}
function Ho(t) {
  return Math.abs(t = Math.round(t)) >= 1e21 ? t.toLocaleString("en").replace(/,/g, "") : t.toString(10);
}
function Ft(t, e) {
  if ((n = (t = e ? t.toExponential(e - 1) : t.toExponential()).indexOf("e")) < 0) return null;
  var n, i = t.slice(0, n);
  return [
    i.length > 1 ? i[0] + i.slice(2) : i,
    +t.slice(n + 1)
  ];
}
function j(t) {
  return t = Ft(Math.abs(t)), t ? t[1] : NaN;
}
function Wo(t, e) {
  return function(n, i) {
    for (var r = n.length, s = [], o = 0, a = t[0], c = 0; r > 0 && a > 0 && (c + a + 1 > i && (a = Math.max(1, i - c)), s.push(n.substring(r -= a, r + a)), !((c += a + 1) > i)); )
      a = t[o = (o + 1) % t.length];
    return s.reverse().join(e);
  };
}
function Oo(t) {
  return function(e) {
    return e.replace(/[0-9]/g, function(n) {
      return t[+n];
    });
  };
}
var Vo = /^(?:(.)?([<>=^]))?([+\-( ])?([$#])?(0)?(\d+)?(,)?(\.\d+)?(~)?([a-z%])?$/i;
function Ht(t) {
  if (!(e = Vo.exec(t))) throw new Error("invalid format: " + t);
  var e;
  return new Ae({
    fill: e[1],
    align: e[2],
    sign: e[3],
    symbol: e[4],
    zero: e[5],
    width: e[6],
    comma: e[7],
    precision: e[8] && e[8].slice(1),
    trim: e[9],
    type: e[10]
  });
}
Ht.prototype = Ae.prototype;
function Ae(t) {
  this.fill = t.fill === void 0 ? " " : t.fill + "", this.align = t.align === void 0 ? ">" : t.align + "", this.sign = t.sign === void 0 ? "-" : t.sign + "", this.symbol = t.symbol === void 0 ? "" : t.symbol + "", this.zero = !!t.zero, this.width = t.width === void 0 ? void 0 : +t.width, this.comma = !!t.comma, this.precision = t.precision === void 0 ? void 0 : +t.precision, this.trim = !!t.trim, this.type = t.type === void 0 ? "" : t.type + "";
}
Ae.prototype.toString = function() {
  return this.fill + this.align + this.sign + this.symbol + (this.zero ? "0" : "") + (this.width === void 0 ? "" : Math.max(1, this.width | 0)) + (this.comma ? "," : "") + (this.precision === void 0 ? "" : "." + Math.max(0, this.precision | 0)) + (this.trim ? "~" : "") + this.type;
};
function qo(t) {
  t: for (var e = t.length, n = 1, i = -1, r; n < e; ++n)
    switch (t[n]) {
      case ".":
        i = r = n;
        break;
      case "0":
        i === 0 && (i = n), r = n;
        break;
      default:
        if (!+t[n]) break t;
        i > 0 && (i = 0);
        break;
    }
  return i > 0 ? t.slice(0, i) + t.slice(r + 1) : t;
}
var Fn;
function Xo(t, e) {
  var n = Ft(t, e);
  if (!n) return t + "";
  var i = n[0], r = n[1], s = r - (Fn = Math.max(-8, Math.min(8, Math.floor(r / 3))) * 3) + 1, o = i.length;
  return s === o ? i : s > o ? i + new Array(s - o + 1).join("0") : s > 0 ? i.slice(0, s) + "." + i.slice(s) : "0." + new Array(1 - s).join("0") + Ft(t, Math.max(0, e + s - 1))[0];
}
function Ge(t, e) {
  var n = Ft(t, e);
  if (!n) return t + "";
  var i = n[0], r = n[1];
  return r < 0 ? "0." + new Array(-r).join("0") + i : i.length > r + 1 ? i.slice(0, r + 1) + "." + i.slice(r + 1) : i + new Array(r - i.length + 2).join("0");
}
const Ye = {
  "%": (t, e) => (t * 100).toFixed(e),
  b: (t) => Math.round(t).toString(2),
  c: (t) => t + "",
  d: Ho,
  e: (t, e) => t.toExponential(e),
  f: (t, e) => t.toFixed(e),
  g: (t, e) => t.toPrecision(e),
  o: (t) => Math.round(t).toString(8),
  p: (t, e) => Ge(t * 100, e),
  r: Ge,
  s: Xo,
  X: (t) => Math.round(t).toString(16).toUpperCase(),
  x: (t) => Math.round(t).toString(16)
};
function Ze(t) {
  return t;
}
var Ke = Array.prototype.map, Qe = ["y", "z", "a", "f", "p", "n", "µ", "m", "", "k", "M", "G", "T", "P", "E", "Z", "Y"];
function Go(t) {
  var e = t.grouping === void 0 || t.thousands === void 0 ? Ze : Wo(Ke.call(t.grouping, Number), t.thousands + ""), n = t.currency === void 0 ? "" : t.currency[0] + "", i = t.currency === void 0 ? "" : t.currency[1] + "", r = t.decimal === void 0 ? "." : t.decimal + "", s = t.numerals === void 0 ? Ze : Oo(Ke.call(t.numerals, String)), o = t.percent === void 0 ? "%" : t.percent + "", a = t.minus === void 0 ? "−" : t.minus + "", c = t.nan === void 0 ? "NaN" : t.nan + "";
  function l(u) {
    u = Ht(u);
    var f = u.fill, d = u.align, p = u.sign, g = u.symbol, y = u.zero, w = u.width, b = u.comma, v = u.precision, M = u.trim, _ = u.type;
    _ === "n" ? (b = !0, _ = "g") : Ye[_] || (v === void 0 && (v = 12), M = !0, _ = "g"), (y || f === "0" && d === "=") && (y = !0, f = "0", d = "=");
    var Yt = g === "$" ? n : g === "#" && /[boxX]/.test(_) ? "0" + _.toLowerCase() : "", Zt = g === "$" ? i : /[%p]/.test(_) ? o : "", bt = Ye[_], ni = /[defgprs%]/.test(_);
    v = v === void 0 ? 6 : /[gprs]/.test(_) ? Math.max(1, Math.min(21, v)) : Math.max(0, Math.min(20, v));
    function Me(m) {
      var z = Yt, S = Zt, Y, Se, vt;
      if (_ === "c")
        S = bt(m) + S, m = "";
      else {
        m = +m;
        var wt = m < 0 || 1 / m < 0;
        if (m = isNaN(m) ? c : bt(Math.abs(m), v), M && (m = qo(m)), wt && +m == 0 && p !== "+" && (wt = !1), z = (wt ? p === "(" ? p : a : p === "-" || p === "(" ? "" : p) + z, S = (_ === "s" ? Qe[8 + Fn / 3] : "") + S + (wt && p === "(" ? ")" : ""), ni) {
          for (Y = -1, Se = m.length; ++Y < Se; )
            if (vt = m.charCodeAt(Y), 48 > vt || vt > 57) {
              S = (vt === 46 ? r + m.slice(Y + 1) : m.slice(Y)) + S, m = m.slice(0, Y);
              break;
            }
        }
      }
      b && !y && (m = e(m, 1 / 0));
      var $t = z.length + m.length + S.length, R = $t < w ? new Array(w - $t + 1).join(f) : "";
      switch (b && y && (m = e(R + m, R.length ? w - S.length : 1 / 0), R = ""), d) {
        case "<":
          m = z + m + S + R;
          break;
        case "=":
          m = z + R + m + S;
          break;
        case "^":
          m = R.slice(0, $t = R.length >> 1) + z + m + S + R.slice($t);
          break;
        default:
          m = R + z + m + S;
          break;
      }
      return s(m);
    }
    return Me.toString = function() {
      return u + "";
    }, Me;
  }
  function h(u, f) {
    var d = l((u = Ht(u), u.type = "f", u)), p = Math.max(-8, Math.min(8, Math.floor(j(f) / 3))) * 3, g = Math.pow(10, -p), y = Qe[8 + p / 3];
    return function(w) {
      return d(g * w) + y;
    };
  }
  return {
    format: l,
    formatPrefix: h
  };
}
var St, Hn, Wn;
Yo({
  thousands: ",",
  grouping: [3],
  currency: ["$", ""]
});
function Yo(t) {
  return St = Go(t), Hn = St.format, Wn = St.formatPrefix, St;
}
function Zo(t) {
  return Math.max(0, -j(Math.abs(t)));
}
function Ko(t, e) {
  return Math.max(0, Math.max(-8, Math.min(8, Math.floor(j(e) / 3))) * 3 - j(Math.abs(t)));
}
function Qo(t, e) {
  return t = Math.abs(t), e = Math.abs(e) - t, Math.max(0, j(e) - j(t)) + 1;
}
function On(t, e) {
  switch (arguments.length) {
    case 0:
      break;
    case 1:
      this.range(t);
      break;
    default:
      this.range(e).domain(t);
      break;
  }
  return this;
}
function Jo(t, e) {
  switch (arguments.length) {
    case 0:
      break;
    case 1: {
      typeof t == "function" ? this.interpolator(t) : this.range(t);
      break;
    }
    default: {
      this.domain(t), typeof e == "function" ? this.interpolator(e) : this.range(e);
      break;
    }
  }
  return this;
}
const Je = Symbol("implicit");
function Vn() {
  var t = new Ee(), e = [], n = [], i = Je;
  function r(s) {
    let o = t.get(s);
    if (o === void 0) {
      if (i !== Je) return i;
      t.set(s, o = e.push(s) - 1);
    }
    return n[o % n.length];
  }
  return r.domain = function(s) {
    if (!arguments.length) return e.slice();
    e = [], t = new Ee();
    for (const o of s)
      t.has(o) || t.set(o, e.push(o) - 1);
    return r;
  }, r.range = function(s) {
    return arguments.length ? (n = Array.from(s), r) : n.slice();
  }, r.unknown = function(s) {
    return arguments.length ? (i = s, r) : i;
  }, r.copy = function() {
    return Vn(e, n).unknown(i);
  }, On.apply(r, arguments), r;
}
function jo(t) {
  return function() {
    return t;
  };
}
function ta(t) {
  return +t;
}
var je = [0, 1];
function B(t) {
  return t;
}
function fe(t, e) {
  return (e -= t = +t) ? function(n) {
    return (n - t) / e;
  } : jo(isNaN(e) ? NaN : 0.5);
}
function ea(t, e) {
  var n;
  return t > e && (n = t, t = e, e = n), function(i) {
    return Math.max(t, Math.min(e, i));
  };
}
function na(t, e, n) {
  var i = t[0], r = t[1], s = e[0], o = e[1];
  return r < i ? (i = fe(r, i), s = n(o, s)) : (i = fe(i, r), s = n(s, o)), function(a) {
    return s(i(a));
  };
}
function ia(t, e, n) {
  var i = Math.min(t.length, e.length) - 1, r = new Array(i), s = new Array(i), o = -1;
  for (t[i] < t[0] && (t = t.slice().reverse(), e = e.slice().reverse()); ++o < i; )
    r[o] = fe(t[o], t[o + 1]), s[o] = n(e[o], e[o + 1]);
  return function(a) {
    var c = ai(t, a, 1, i) - 1;
    return s[c](r[c](a));
  };
}
function ra(t, e) {
  return e.domain(t.domain()).range(t.range()).interpolate(t.interpolate()).clamp(t.clamp()).unknown(t.unknown());
}
function sa() {
  var t = je, e = je, n = Vt, i, r, s, o = B, a, c, l;
  function h() {
    var f = Math.min(t.length, e.length);
    return o !== B && (o = ea(t[0], t[f - 1])), a = f > 2 ? ia : na, c = l = null, u;
  }
  function u(f) {
    return f == null || isNaN(f = +f) ? s : (c || (c = a(t.map(i), e, n)))(i(o(f)));
  }
  return u.invert = function(f) {
    return o(r((l || (l = a(e, t.map(i), C)))(f)));
  }, u.domain = function(f) {
    return arguments.length ? (t = Array.from(f, ta), h()) : t.slice();
  }, u.range = function(f) {
    return arguments.length ? (e = Array.from(f), h()) : e.slice();
  }, u.rangeRound = function(f) {
    return e = Array.from(f), n = En, h();
  }, u.clamp = function(f) {
    return arguments.length ? (o = f ? !0 : B, h()) : o !== B;
  }, u.interpolate = function(f) {
    return arguments.length ? (n = f, h()) : n;
  }, u.unknown = function(f) {
    return arguments.length ? (s = f, u) : s;
  }, function(f, d) {
    return i = f, r = d, h();
  };
}
function oa() {
  return sa()(B, B);
}
function aa(t, e, n, i) {
  var r = gi(t, e, n), s;
  switch (i = Ht(i ?? ",f"), i.type) {
    case "s": {
      var o = Math.max(Math.abs(t), Math.abs(e));
      return i.precision == null && !isNaN(s = Ko(r, o)) && (i.precision = s), Wn(i, o);
    }
    case "":
    case "e":
    case "g":
    case "p":
    case "r": {
      i.precision == null && !isNaN(s = Qo(r, Math.max(Math.abs(t), Math.abs(e)))) && (i.precision = s - (i.type === "e"));
      break;
    }
    case "f":
    case "%": {
      i.precision == null && !isNaN(s = Zo(r)) && (i.precision = s - (i.type === "%") * 2);
      break;
    }
  }
  return Hn(i);
}
function qn(t) {
  var e = t.domain;
  return t.ticks = function(n) {
    var i = e();
    return pi(i[0], i[i.length - 1], n ?? 10);
  }, t.tickFormat = function(n, i) {
    var r = e();
    return aa(r[0], r[r.length - 1], n ?? 10, i);
  }, t.nice = function(n) {
    n == null && (n = 10);
    var i = e(), r = 0, s = i.length - 1, o = i[r], a = i[s], c, l, h = 10;
    for (a < o && (l = o, o = a, a = l, l = r, r = s, s = l); h-- > 0; ) {
      if (l = ne(o, a, n), l === c)
        return i[r] = o, i[s] = a, e(i);
      if (l > 0)
        o = Math.floor(o / l) * l, a = Math.ceil(a / l) * l;
      else if (l < 0)
        o = Math.ceil(o * l) / l, a = Math.floor(a * l) / l;
      else
        break;
      c = l;
    }
    return t;
  }, t;
}
function de() {
  var t = oa();
  return t.copy = function() {
    return ra(t, de());
  }, On.apply(t, arguments), qn(t);
}
function la() {
  var t = 0, e = 1, n, i, r, s, o = B, a = !1, c;
  function l(u) {
    return u == null || isNaN(u = +u) ? c : o(r === 0 ? 0.5 : (u = (s(u) - n) * r, a ? Math.max(0, Math.min(1, u)) : u));
  }
  l.domain = function(u) {
    return arguments.length ? ([t, e] = u, n = s(t = +t), i = s(e = +e), r = n === i ? 0 : 1 / (i - n), l) : [t, e];
  }, l.clamp = function(u) {
    return arguments.length ? (a = !!u, l) : a;
  }, l.interpolator = function(u) {
    return arguments.length ? (o = u, l) : o;
  };
  function h(u) {
    return function(f) {
      var d, p;
      return arguments.length ? ([d, p] = f, o = u(d, p), l) : [o(0), o(1)];
    };
  }
  return l.range = h(Vt), l.rangeRound = h(En), l.unknown = function(u) {
    return arguments.length ? (c = u, l) : c;
  }, function(u) {
    return s = u, n = u(t), i = u(e), r = n === i ? 0 : 1 / (i - n), l;
  };
}
function ca(t, e) {
  return e.domain(t.domain()).interpolator(t.interpolator()).clamp(t.clamp()).unknown(t.unknown());
}
function Xn() {
  var t = qn(la()(B));
  return t.copy = function() {
    return ca(t, Xn());
  }, Jo.apply(t, arguments);
}
function ua(t) {
  for (var e = t.length / 6 | 0, n = new Array(e), i = 0; i < e; ) n[i] = "#" + t.slice(i * 6, ++i * 6);
  return n;
}
const Gn = ua("4e79a7f28e2ce1575976b7b259a14fedc949af7aa1ff9da79c755fbab0ab");
function Ct(t) {
  return function() {
    return t;
  };
}
const nt = Math.sqrt, Yn = Math.PI, ha = 2 * Yn;
function fa(t) {
  let e = 3;
  return t.digits = function(n) {
    if (!arguments.length) return e;
    if (n == null)
      e = null;
    else {
      const i = Math.floor(n);
      if (!(i >= 0)) throw new RangeError(`invalid digits: ${n}`);
      e = i;
    }
    return t;
  }, () => new Fo(e);
}
const da = {
  draw(t, e) {
    const n = nt(e / Yn);
    t.moveTo(n, 0), t.arc(0, 0, n, 0, ha);
  }
}, pa = {
  draw(t, e) {
    const n = nt(e / 5) / 2;
    t.moveTo(-3 * n, -n), t.lineTo(-n, -n), t.lineTo(-n, -3 * n), t.lineTo(n, -3 * n), t.lineTo(n, -n), t.lineTo(3 * n, -n), t.lineTo(3 * n, n), t.lineTo(n, n), t.lineTo(n, 3 * n), t.lineTo(-n, 3 * n), t.lineTo(-n, n), t.lineTo(-3 * n, n), t.closePath();
  }
}, Zn = nt(1 / 3), ga = Zn * 2, ma = {
  draw(t, e) {
    const n = nt(e / ga), i = n * Zn;
    t.moveTo(0, -n), t.lineTo(i, 0), t.lineTo(0, n), t.lineTo(-i, 0), t.closePath();
  }
}, Jt = nt(3), ya = {
  draw(t, e) {
    const n = -nt(e / (Jt * 3));
    t.moveTo(0, n * 2), t.lineTo(-Jt * n, -n), t.lineTo(Jt * n, -n), t.closePath();
  }
};
function _a(t, e) {
  let n = null, i = fa(r);
  t = typeof t == "function" ? t : Ct(t || da), e = typeof e == "function" ? e : Ct(e === void 0 ? 64 : +e);
  function r() {
    let s;
    if (n || (n = s = i()), t.apply(this, arguments).draw(n, +e.apply(this, arguments)), s) return n = null, s + "" || null;
  }
  return r.type = function(s) {
    return arguments.length ? (t = typeof s == "function" ? s : Ct(s), r) : t;
  }, r.size = function(s) {
    return arguments.length ? (e = typeof s == "function" ? s : Ct(+s), r) : e;
  }, r.context = function(s) {
    return arguments.length ? (n = s ?? null, r) : n;
  }, r;
}
function lt(t, e, n) {
  this.k = t, this.x = e, this.y = n;
}
lt.prototype = {
  constructor: lt,
  scale: function(t) {
    return t === 1 ? this : new lt(this.k * t, this.x, this.y);
  },
  translate: function(t, e) {
    return t === 0 & e === 0 ? this : new lt(this.k, this.x + this.k * t, this.y + this.k * e);
  },
  apply: function(t) {
    return [t[0] * this.k + this.x, t[1] * this.k + this.y];
  },
  applyX: function(t) {
    return t * this.k + this.x;
  },
  applyY: function(t) {
    return t * this.k + this.y;
  },
  invert: function(t) {
    return [(t[0] - this.x) / this.k, (t[1] - this.y) / this.k];
  },
  invertX: function(t) {
    return (t - this.x) / this.k;
  },
  invertY: function(t) {
    return (t - this.y) / this.k;
  },
  rescaleX: function(t) {
    return t.copy().domain(t.range().map(this.invertX, this).map(t.invert, t));
  },
  rescaleY: function(t) {
    return t.copy().domain(t.range().map(this.invertY, this).map(t.invert, t));
  },
  toString: function() {
    return "translate(" + this.x + "," + this.y + ") scale(" + this.k + ")";
  }
};
lt.prototype;
const xa = (t, e, n, i, r, s) => {
  const [o, a] = Ce(t, (g) => g.x), [c, l] = Ce(t, (g) => g.y), h = de().domain([o * 1.1, a * 1.1]).range([0, e]), u = de().domain([c * 1.1, l * 1.1]).range([n, 0]);
  let f = Vn().domain(fn(i.length).map(String)).range(Gn);
  return { xScale: h, yScale: u, colorScale: f, range: {
    xMin: o,
    xMax: a,
    yMin: c,
    yMax: l
  }, ghostColorScale: (g) => {
    const y = r[g] || f(g);
    return (w) => {
      const b = w / s;
      return Q(y, "#ffffff")(1 - b);
    };
  } };
}, ct = (t) => {
  const e = t.get("embedding_id"), [n, i] = [t.get("width"), t.get("height")], {
    original_embedding: r,
    ghost_embedding: s,
    n_ghosts: o,
    r: a,
    legend: c,
    colors: l
  } = t.get("embedding_set")[e], h = xa(r, n, i, c, l, a), u = h.range, f = t.get("distance"), d = t.get("sensitivity"), p = Math.ceil(d * (o - 1));
  console.log("ghostEmb", s);
  const g = f * mi([u.xMax - u.xMin, u.yMax - u.yMin]);
  console.log(p, g);
  const y = r.filter((w) => w.radii[p] > g);
  return {
    origEmb: r,
    ghostEmb: s,
    radius: a,
    unstEmb: y,
    scales: h,
    range: u,
    scaledDist: g,
    scaledSens: p,
    legend: c,
    colors: l
  };
}, pe = (t, e, n) => {
  const i = { ...t.get("unstableInfo") };
  return i.unstableEmb = e, i.numUnstables = e.length, i.percentUnstables = e.length / n * 100, t.set("unstableInfo", i), t.save_changes(), i;
};
/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
const ut = globalThis, Wt = ut.trustedTypes, tn = Wt ? Wt.createPolicy("lit-html", { createHTML: (t) => t }) : void 0, Kn = "$lit$", D = `lit$${Math.random().toFixed(9).slice(2)}$`, Qn = "?" + D, ba = `<${Qn}>`, G = document, pt = () => G.createComment(""), gt = (t) => t === null || typeof t != "object" && typeof t != "function", ke = Array.isArray, va = (t) => ke(t) || typeof (t == null ? void 0 : t[Symbol.iterator]) == "function", jt = `[ 	
\f\r]`, st = /<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g, en = /-->/g, nn = />/g, F = RegExp(`>|${jt}(?:([^\\s"'>=/]+)(${jt}*=${jt}*(?:[^ 	
\f\r"'\`<>=]|("|')|))|$)`, "g"), rn = /'/g, sn = /"/g, Jn = /^(?:script|style|textarea|title)$/i, wa = (t) => (e, ...n) => ({ _$litType$: t, strings: e, values: n }), L = wa(1), tt = Symbol.for("lit-noChange"), $ = Symbol.for("lit-nothing"), on = /* @__PURE__ */ new WeakMap(), O = G.createTreeWalker(G, 129);
function jn(t, e) {
  if (!ke(t) || !t.hasOwnProperty("raw")) throw Error("invalid template strings array");
  return tn !== void 0 ? tn.createHTML(e) : e;
}
const $a = (t, e) => {
  const n = t.length - 1, i = [];
  let r, s = e === 2 ? "<svg>" : e === 3 ? "<math>" : "", o = st;
  for (let a = 0; a < n; a++) {
    const c = t[a];
    let l, h, u = -1, f = 0;
    for (; f < c.length && (o.lastIndex = f, h = o.exec(c), h !== null); ) f = o.lastIndex, o === st ? h[1] === "!--" ? o = en : h[1] !== void 0 ? o = nn : h[2] !== void 0 ? (Jn.test(h[2]) && (r = RegExp("</" + h[2], "g")), o = F) : h[3] !== void 0 && (o = F) : o === F ? h[0] === ">" ? (o = r ?? st, u = -1) : h[1] === void 0 ? u = -2 : (u = o.lastIndex - h[2].length, l = h[1], o = h[3] === void 0 ? F : h[3] === '"' ? sn : rn) : o === sn || o === rn ? o = F : o === en || o === nn ? o = st : (o = F, r = void 0);
    const d = o === F && t[a + 1].startsWith("/>") ? " " : "";
    s += o === st ? c + ba : u >= 0 ? (i.push(l), c.slice(0, u) + Kn + c.slice(u) + D + d) : c + D + (u === -2 ? a : d);
  }
  return [jn(t, s + (t[n] || "<?>") + (e === 2 ? "</svg>" : e === 3 ? "</math>" : "")), i];
};
class mt {
  constructor({ strings: e, _$litType$: n }, i) {
    let r;
    this.parts = [];
    let s = 0, o = 0;
    const a = e.length - 1, c = this.parts, [l, h] = $a(e, n);
    if (this.el = mt.createElement(l, i), O.currentNode = this.el.content, n === 2 || n === 3) {
      const u = this.el.content.firstChild;
      u.replaceWith(...u.childNodes);
    }
    for (; (r = O.nextNode()) !== null && c.length < a; ) {
      if (r.nodeType === 1) {
        if (r.hasAttributes()) for (const u of r.getAttributeNames()) if (u.endsWith(Kn)) {
          const f = h[o++], d = r.getAttribute(u).split(D), p = /([.?@])?(.*)/.exec(f);
          c.push({ type: 1, index: s, name: p[2], strings: d, ctor: p[1] === "." ? ka : p[1] === "?" ? Ma : p[1] === "@" ? Sa : Gt }), r.removeAttribute(u);
        } else u.startsWith(D) && (c.push({ type: 6, index: s }), r.removeAttribute(u));
        if (Jn.test(r.tagName)) {
          const u = r.textContent.split(D), f = u.length - 1;
          if (f > 0) {
            r.textContent = Wt ? Wt.emptyScript : "";
            for (let d = 0; d < f; d++) r.append(u[d], pt()), O.nextNode(), c.push({ type: 2, index: ++s });
            r.append(u[f], pt());
          }
        }
      } else if (r.nodeType === 8) if (r.data === Qn) c.push({ type: 2, index: s });
      else {
        let u = -1;
        for (; (u = r.data.indexOf(D, u + 1)) !== -1; ) c.push({ type: 7, index: s }), u += D.length - 1;
      }
      s++;
    }
  }
  static createElement(e, n) {
    const i = G.createElement("template");
    return i.innerHTML = e, i;
  }
}
function et(t, e, n = t, i) {
  var o, a;
  if (e === tt) return e;
  let r = i !== void 0 ? (o = n._$Co) == null ? void 0 : o[i] : n._$Cl;
  const s = gt(e) ? void 0 : e._$litDirective$;
  return (r == null ? void 0 : r.constructor) !== s && ((a = r == null ? void 0 : r._$AO) == null || a.call(r, !1), s === void 0 ? r = void 0 : (r = new s(t), r._$AT(t, n, i)), i !== void 0 ? (n._$Co ?? (n._$Co = []))[i] = r : n._$Cl = r), r !== void 0 && (e = et(t, r._$AS(t, e.values), r, i)), e;
}
class Aa {
  constructor(e, n) {
    this._$AV = [], this._$AN = void 0, this._$AD = e, this._$AM = n;
  }
  get parentNode() {
    return this._$AM.parentNode;
  }
  get _$AU() {
    return this._$AM._$AU;
  }
  u(e) {
    const { el: { content: n }, parts: i } = this._$AD, r = ((e == null ? void 0 : e.creationScope) ?? G).importNode(n, !0);
    O.currentNode = r;
    let s = O.nextNode(), o = 0, a = 0, c = i[0];
    for (; c !== void 0; ) {
      if (o === c.index) {
        let l;
        c.type === 2 ? l = new xt(s, s.nextSibling, this, e) : c.type === 1 ? l = new c.ctor(s, c.name, c.strings, this, e) : c.type === 6 && (l = new Ca(s, this, e)), this._$AV.push(l), c = i[++a];
      }
      o !== (c == null ? void 0 : c.index) && (s = O.nextNode(), o++);
    }
    return O.currentNode = G, r;
  }
  p(e) {
    let n = 0;
    for (const i of this._$AV) i !== void 0 && (i.strings !== void 0 ? (i._$AI(e, i, n), n += i.strings.length - 2) : i._$AI(e[n])), n++;
  }
}
class xt {
  get _$AU() {
    var e;
    return ((e = this._$AM) == null ? void 0 : e._$AU) ?? this._$Cv;
  }
  constructor(e, n, i, r) {
    this.type = 2, this._$AH = $, this._$AN = void 0, this._$AA = e, this._$AB = n, this._$AM = i, this.options = r, this._$Cv = (r == null ? void 0 : r.isConnected) ?? !0;
  }
  get parentNode() {
    let e = this._$AA.parentNode;
    const n = this._$AM;
    return n !== void 0 && (e == null ? void 0 : e.nodeType) === 11 && (e = n.parentNode), e;
  }
  get startNode() {
    return this._$AA;
  }
  get endNode() {
    return this._$AB;
  }
  _$AI(e, n = this) {
    e = et(this, e, n), gt(e) ? e === $ || e == null || e === "" ? (this._$AH !== $ && this._$AR(), this._$AH = $) : e !== this._$AH && e !== tt && this._(e) : e._$litType$ !== void 0 ? this.$(e) : e.nodeType !== void 0 ? this.T(e) : va(e) ? this.k(e) : this._(e);
  }
  O(e) {
    return this._$AA.parentNode.insertBefore(e, this._$AB);
  }
  T(e) {
    this._$AH !== e && (this._$AR(), this._$AH = this.O(e));
  }
  _(e) {
    this._$AH !== $ && gt(this._$AH) ? this._$AA.nextSibling.data = e : this.T(G.createTextNode(e)), this._$AH = e;
  }
  $(e) {
    var s;
    const { values: n, _$litType$: i } = e, r = typeof i == "number" ? this._$AC(e) : (i.el === void 0 && (i.el = mt.createElement(jn(i.h, i.h[0]), this.options)), i);
    if (((s = this._$AH) == null ? void 0 : s._$AD) === r) this._$AH.p(n);
    else {
      const o = new Aa(r, this), a = o.u(this.options);
      o.p(n), this.T(a), this._$AH = o;
    }
  }
  _$AC(e) {
    let n = on.get(e.strings);
    return n === void 0 && on.set(e.strings, n = new mt(e)), n;
  }
  k(e) {
    ke(this._$AH) || (this._$AH = [], this._$AR());
    const n = this._$AH;
    let i, r = 0;
    for (const s of e) r === n.length ? n.push(i = new xt(this.O(pt()), this.O(pt()), this, this.options)) : i = n[r], i._$AI(s), r++;
    r < n.length && (this._$AR(i && i._$AB.nextSibling, r), n.length = r);
  }
  _$AR(e = this._$AA.nextSibling, n) {
    var i;
    for ((i = this._$AP) == null ? void 0 : i.call(this, !1, !0, n); e && e !== this._$AB; ) {
      const r = e.nextSibling;
      e.remove(), e = r;
    }
  }
  setConnected(e) {
    var n;
    this._$AM === void 0 && (this._$Cv = e, (n = this._$AP) == null || n.call(this, e));
  }
}
class Gt {
  get tagName() {
    return this.element.tagName;
  }
  get _$AU() {
    return this._$AM._$AU;
  }
  constructor(e, n, i, r, s) {
    this.type = 1, this._$AH = $, this._$AN = void 0, this.element = e, this.name = n, this._$AM = r, this.options = s, i.length > 2 || i[0] !== "" || i[1] !== "" ? (this._$AH = Array(i.length - 1).fill(new String()), this.strings = i) : this._$AH = $;
  }
  _$AI(e, n = this, i, r) {
    const s = this.strings;
    let o = !1;
    if (s === void 0) e = et(this, e, n, 0), o = !gt(e) || e !== this._$AH && e !== tt, o && (this._$AH = e);
    else {
      const a = e;
      let c, l;
      for (e = s[0], c = 0; c < s.length - 1; c++) l = et(this, a[i + c], n, c), l === tt && (l = this._$AH[c]), o || (o = !gt(l) || l !== this._$AH[c]), l === $ ? e = $ : e !== $ && (e += (l ?? "") + s[c + 1]), this._$AH[c] = l;
    }
    o && !r && this.j(e);
  }
  j(e) {
    e === $ ? this.element.removeAttribute(this.name) : this.element.setAttribute(this.name, e ?? "");
  }
}
class ka extends Gt {
  constructor() {
    super(...arguments), this.type = 3;
  }
  j(e) {
    this.element[this.name] = e === $ ? void 0 : e;
  }
}
class Ma extends Gt {
  constructor() {
    super(...arguments), this.type = 4;
  }
  j(e) {
    this.element.toggleAttribute(this.name, !!e && e !== $);
  }
}
class Sa extends Gt {
  constructor(e, n, i, r, s) {
    super(e, n, i, r, s), this.type = 5;
  }
  _$AI(e, n = this) {
    if ((e = et(this, e, n, 0) ?? $) === tt) return;
    const i = this._$AH, r = e === $ && i !== $ || e.capture !== i.capture || e.once !== i.once || e.passive !== i.passive, s = e !== $ && (i === $ || r);
    r && this.element.removeEventListener(this.name, this, i), s && this.element.addEventListener(this.name, this, e), this._$AH = e;
  }
  handleEvent(e) {
    var n;
    typeof this._$AH == "function" ? this._$AH.call(((n = this.options) == null ? void 0 : n.host) ?? this.element, e) : this._$AH.handleEvent(e);
  }
}
class Ca {
  constructor(e, n, i) {
    this.element = e, this.type = 6, this._$AN = void 0, this._$AM = n, this.options = i;
  }
  get _$AU() {
    return this._$AM._$AU;
  }
  _$AI(e) {
    et(this, e);
  }
}
const te = ut.litHtmlPolyfillSupport;
te == null || te(mt, xt), (ut.litHtmlVersions ?? (ut.litHtmlVersions = [])).push("3.2.1");
const it = (t, e, n) => {
  const i = e;
  let r = i._$litPart$;
  return r === void 0 && (i._$litPart$ = r = new xt(e.insertBefore(pt(), null), null, void 0, {})), r._$AI(t), r;
};
/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
const Ea = { ATTRIBUTE: 1 }, Na = (t) => (...e) => ({ _$litDirective$: t, values: e });
let Ta = class {
  constructor(e) {
  }
  get _$AU() {
    return this._$AM._$AU;
  }
  _$AT(e, n, i) {
    this._$Ct = e, this._$AM = n, this._$Ci = i;
  }
  _$AS(e, n) {
    return this.update(e, n);
  }
  update(e, n) {
    return this.render(...n);
  }
};
/**
 * @license
 * Copyright 2018 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
const ti = "important", La = " !" + ti, x = Na(class extends Ta {
  constructor(t) {
    var e;
    if (super(t), t.type !== Ea.ATTRIBUTE || t.name !== "style" || ((e = t.strings) == null ? void 0 : e.length) > 2) throw Error("The `styleMap` directive must be used in the `style` attribute and must be the only part in the attribute.");
  }
  render(t) {
    return Object.keys(t).reduce((e, n) => {
      const i = t[n];
      return i == null ? e : e + `${n = n.includes("-") ? n : n.replace(/(?:^(webkit|moz|ms|o)|)(?=[A-Z])/g, "-$&").toLowerCase()}:${i};`;
    }, "");
  }
  update(t, [e]) {
    const { style: n } = t.element;
    if (this.ft === void 0) return this.ft = new Set(Object.keys(e)), this.render(e);
    for (const i of this.ft) e[i] == null && (this.ft.delete(i), i.includes("-") ? n.removeProperty(i) : n[i] = null);
    for (const i in e) {
      const r = e[i];
      if (r != null) {
        this.ft.add(i);
        const s = typeof r == "string" && r.endsWith(La);
        i.includes("-") || s ? n.setProperty(i, s ? r.slice(0, -11) : r, s ? ti : "") : n[i] = r;
      }
    }
    return tt;
  }
}), Pa = {
  display: "flex",
  flexDirection: "column",
  justifyContent: "space-between",
  height: "100%",
  "padding-right": "30px"
}, Ra = {
  display: "flex",
  flexDirection: "row"
}, Ua = {
  display: "flex",
  flexDirection: "row",
  justifyContent: "center",
  alignItems: "center",
  border: "none",
  width: "100%",
  margin: 0,
  padding: 0,
  backgroundColor: "#fff",
  color: "#333"
}, Ia = {
  width: "100%",
  padding: "5px"
}, Da = {
  padding: "5px"
};
function Ba(t, e, n, i, r, s) {
  const o = () => {
    const { origEmb: l, unstEmb: h, ghostEmb: u, scales: f, legend: d, colors: p } = ct(t);
    s([]);
    const g = pe(t, h, l.length);
    e.update(l, h, u, f), n.update(d, p, f), i.update("distance", t.get("distance")), r.update(
      h,
      g.numUnstables,
      g.percentUnstables,
      () => t.get("checkedUnstables"),
      s
    );
  }, a = (l) => {
    const { origEmb: h, unstEmb: u, ghostEmb: f, scales: d } = ct(t), { numUnstables: p, percentUnstables: g } = pe(
      t,
      u,
      h.length
    );
    s([]), e.update(h, u, f, d), i.update(l, t.get(l)), r.update(
      u,
      p,
      g,
      () => t.get("checkedUnstables"),
      s
    );
  }, c = (l) => {
    ct(t);
    const h = `show_${l}`;
    e.updateVisibility(l, t.get(h)), i.update(h, t.get(h));
  };
  t.on("change:embedding_id", o), t.on("change:distance", () => a("distance")), t.on("change:sensitivity", () => a("sensitivity")), t.on("change:show_unstables", () => c("unstables")), t.on("change:show_neighbors", () => c("neighbors")), t.on("change:show_ghosts", () => c("ghosts")), t.on("change:unstableInfo", () => {
    const { unstEmb: l } = ct(t), h = t.get("unstableInfo");
    r.update(
      l,
      h.numUnstables,
      h.percentUnstables,
      () => t.get("checkedUnstables"),
      s
    );
  }), t.on("change:checkedUnstables", () => {
    const l = t.get("checkedUnstables");
    e.updateUnstList(l), r.updateCheckbox(l);
  });
}
function an(t) {
  const e = Math.min(...t), n = Math.max(...t);
  return { min: e, max: n, range: n - e || 1 };
}
function ei(t) {
  let e, n;
  if (Array.isArray(t) && Array.isArray(t[0]))
    e = t.map((u) => u[0]), n = t.map((u) => u[1]);
  else if ("x" in t && "y" in t)
    e = t.x, n = t.y;
  else
    throw new Error("Invalid points format.");
  const { min: i, max: r, range: s } = an(e), { min: o, max: a, range: c } = an(n), l = 0.9;
  return { pointArray: new Float32Array(
    e.map((u, f) => [
      ((u - i) / s * 2 - 1) * l,
      ((n[f] - o) / c * 2 - 1) * l
    ]).flat()
  ), xMin: i, xMax: r, yMin: o, yMax: a };
}
function za(t) {
  const n = document.createElement("canvas").getContext("2d");
  if (!n) return [0, 0, 0];
  n.fillStyle = t;
  const i = n.fillStyle;
  if (i.startsWith("#")) {
    const r = parseInt(i.slice(1), 16);
    return [
      (r >> 16 & 255) / 255,
      (r >> 8 & 255) / 255,
      (r & 255) / 255
    ];
  }
  return [0, 0, 0];
}
function ln(t, e, n) {
  if (t = Array.isArray(t) ? t : Array(n).fill(t), e = Array.isArray(e) ? e : Array(n).fill(e), n !== t.length || n !== e.length)
    throw new Error("Mismatch between number of points and colors or opacity.");
  const i = new Float32Array(t.length * 4);
  return t.forEach((r, s) => {
    const [o, a, c] = za(r);
    i.set([o, a, c, e[s]], s * 4);
  }), i;
}
function Fa(t, e) {
  if (t = Array.isArray(t) ? t : Array(e).fill(t), t.length !== e)
    throw new Error("Mismatch between number of points and sizes.");
  return new Float32Array(t);
}
function Ha(t, e) {
  const n = {
    circle: 0,
    square: 1,
    triangle: 2,
    diamond: 3,
    cross: 4
  };
  return {
    symbolData: Array.isArray(t) ? new Uint32Array(t.map((r) => n[r])) : new Uint32Array(e).fill(n[t]),
    symbolOffset: new Float32Array([
      -0.5,
      -0.5,
      -0.5,
      0.5,
      0.5,
      -0.5,
      0.5,
      0.5
    ])
  };
}
function Wa(t, e) {
  const {
    color: n = "#FF0000",
    size: i = 10,
    opacity: r = 1,
    strokeColor: s = "#000000",
    strokeWidth: o = 0,
    symbol: a = "circle"
  } = e ?? {}, { pointArray: c } = ei(t), l = ln(n, r, c.length / 2), h = Fa(i, c.length / 2), u = ln(
    s,
    r,
    c.length / 2
  ), f = Array.isArray(o) ? new Float32Array(o) : new Float32Array(Array(c.length / 2).fill(o)), { symbolData: d, symbolOffset: p } = Ha(
    a,
    c.length / 2
  );
  return {
    vertex: c,
    color: l,
    size: h,
    strokeColor: u,
    strokeWidth: f,
    offset: p,
    symbol: d
  };
}
async function Oa(t) {
  if (!navigator.gpu)
    throw new Error("WebGPU is not supported.");
  const e = await navigator.gpu.requestAdapter();
  if (!e)
    throw new Error("No appropriate GPUAdapter found.");
  const n = await e.requestDevice(), i = t.getContext("webgpu"), r = navigator.gpu.getPreferredCanvasFormat();
  return i.configure({ device: n, format: r }), { device: n, context: i, format: r };
}
const Va = `struct InstanceData {
  @location(0) position: vec2<f32>,   
  @location(1) color: vec4<f32>,      
  @location(2) size: f32,             
  @location(3) strokeColor: vec4<f32>, 
  @location(4) strokeWidth: f32,
  @location(5) symbol: u32

};

struct SymbolVertex {
  @location(6) offset: vec2<f32>
};

struct VertexOutput {
  @builtin(position) position: vec4<f32>,
  @location(0) color: vec4<f32>,
  @location(1) localPos: vec2<f32>,   
  @location(2) strokeColor: vec4<f32>, 
  @location(3) strokeWidth: f32, 
  @location(4) @interpolate(flat)symbol: u32,
};

struct CanvasSize {
  width: f32,
  height: f32,
};

struct Transform {
  scale: f32,
  translateX: f32,
  translateY: f32,
};

@group(0) @binding(0) var<uniform> canvas: CanvasSize;
@group(0) @binding(1) var<uniform> transform: Transform;

@vertex
fn vs_main(@builtin(vertex_index) VertexIndex: u32, instance: InstanceData, vertex: SymbolVertex) -> VertexOutput {
    var output: VertexOutput;

    // transform px to clip space 
    let size_clip = (instance.size / min(canvas.width, canvas.height)) * 2.0;
    let stroke_clip = instance.strokeWidth / instance.size;

    let scaledOffset = vertex.offset * size_clip;
    let pos = (instance.position * transform.scale) + vec2<f32>(transform.translateX, transform.translateY) + scaledOffset;

    output.position = vec4<f32>(pos, 0.0, 1.0);
    output.color = instance.color;

    // Convert local position to clip space
    output.localPos = vertex.offset * 2.0;

    output.strokeColor = instance.strokeColor;
    output.strokeWidth = stroke_clip;

    output.symbol = instance.symbol;


    return output;
}`, qa = `struct VertexOutput {
  @builtin(position) position: vec4<f32>,
  @location(0) color: vec4<f32>,
  @location(1) localPos: vec2<f32>,   
  @location(2) strokeColor: vec4<f32>, 
  @location(3) strokeWidth: f32, 
  @location(4) @interpolate(flat) symbol: u32      
};

fn is_inside_circle_stroke(pos: vec2<f32 >, strokeWidth: f32) -> bool {
    let innerRadius = 1.0 - strokeWidth * 2.0;
    let dist = length(pos);
    return dist > innerRadius && dist <= 1.0;
}



fn is_inside_square_stroke(pos: vec2<f32>, strokeWidth: f32) -> bool {
    let innerSize = 1.0 - strokeWidth * 2.0;
    return (abs(pos.x) > innerSize || abs(pos.y) > innerSize) && abs(pos.x) <= 1.0 && abs(pos.y) <= 1.0;
}


//triangle: [-0.5, -0.5, 0.0, 0.433, 0.5, -0.5],
//TODO: 
fn is_inside_triangle_stroke(pos: vec2<f32>, strokeWidth: f32) -> bool {
    // 삼각형의 꼭짓점들 (로컬 좌표 공간에서)
    let A = vec2<f32>(-1.0, -1.0);
    let B = vec2<f32>(0.0, 0.73);
    let C = vec2<f32>(1.0, -1.0);
    
    // 삼각형 면적 계산 (절대값)
    let area = abs((B.x - A.x) * (C.y - A.y) - (C.x - A.x) * (B.y - A.y));
    
    // 각 꼭짓점에 대한 픽셀 p의 barycentric 좌표를 계산
    let lambda1 = abs((B.x - pos.x) * (C.y - pos.y) - (C.x - pos.x) * (B.y - pos.y)) / area;
    let lambda2 = abs((C.x - pos.x) * (A.y - pos.y) - (A.x - pos.x) * (C.y - pos.y)) / area;
    let lambda3 = abs((A.x - pos.x) * (B.y - pos.y) - (B.x - pos.x) * (A.y - pos.y)) / area;
    
    // 최소의 barycentric 값: 모서리에 가까울수록 이 값이 작아짐
    let minLambda = min(lambda1, min(lambda2, lambda3));
    
    // minLambda가 strokeWidth보다 작으면 모서리 영역으로 판단
    return minLambda < strokeWidth;
}

fn is_inside_diamond_stroke(pos: vec2<f32>, strokeWidth: f32) -> bool {
    let outerSize = 1.0;
    let innerSize = outerSize - strokeWidth * 2.0;

    let dist = abs(pos.x) + abs(pos.y);

    return dist > innerSize && dist <= outerSize;
}

fn is_inside_cross_stroke(pos: vec2<f32>, strokeWidth: f32) -> bool {
    let inner_cross = abs(pos.x) <= (0.4 - strokeWidth) || abs(pos.y) <= (0.4 - strokeWidth);
    let boundary = abs(pos.x) >= 1.0 - strokeWidth || abs(pos.y) >= 1.0 - strokeWidth;
    
    // stroke 영역은 경계에서 strokeWidth 이내인 영역으로 정의
    return (!inner_cross || boundary) && (abs(pos.x) <= 0.4 || abs(pos.y) <= 0.4);
}

fn soft_edge_circle(pos: vec2<f32>, strokeWidth: f32) -> f32 {
    let dist = length(pos);
    let edge = 1.0; // 원의 경계
    let fadeStart = 0.95; // 부드러워지는 시작점
    return smoothstep(edge, fadeStart, dist);
}

@fragment
fn fs_main(input: VertexOutput) -> @location(0) vec4<f32> {
    var inside: bool = false;
    var isStroke: bool = false;
    let pos = input.localPos;

    var finalColor: vec4<f32> = input.color;
    var alpha: f32 = input.color.a;

    switch input.symbol {
        case 0u: { // Circle
            inside = length(pos) <= 1.0;
            isStroke = is_inside_circle_stroke(input.localPos, input.strokeWidth);
            let edgeFactor = soft_edge_circle(pos, input.strokeWidth);
            alpha *= edgeFactor;
        }
        case 1u: { // Square
            inside = abs(pos.x) <= 1.0 && abs(pos.y) <= 1.0;
            isStroke = is_inside_square_stroke(input.localPos, input.strokeWidth);
        }
        case 2u: { // Triangle
            inside = pos.y >= -1.0 && 1.73 * pos.x + 0.73 >= pos.y && -1.73 * pos.x + 0.73 >= pos.y;
            isStroke = is_inside_triangle_stroke(input.localPos, input.strokeWidth);

        }
        case 3u: { // Diamond
            inside = abs(pos.x) + abs(pos.y) <= 1.0;
            isStroke = is_inside_diamond_stroke(input.localPos, input.strokeWidth);
        }
        case 4u: { // Cross
            inside = (abs(pos.x) <= 0.4) || (abs(pos.y) <= 0.4);
            isStroke = is_inside_cross_stroke(input.localPos, input.strokeWidth);
        }
        default: {
            discard;
        }
    }

    if !inside {
        discard;
    }


    if input.strokeWidth > 0.0 && isStroke {
        finalColor = input.strokeColor;
    }

    return vec4<f32>(finalColor.rgb, alpha);
}
`;
async function Xa(t, e) {
  const n = t.createBindGroupLayout({
    entries: [
      {
        binding: 0,
        visibility: GPUShaderStage.VERTEX,
        buffer: { type: "uniform" }
      },
      {
        binding: 1,
        visibility: GPUShaderStage.VERTEX,
        buffer: { type: "uniform" }
      }
    ]
  }), i = t.createPipelineLayout({
    bindGroupLayouts: [n]
  });
  return t.createRenderPipeline({
    layout: i,
    vertex: {
      module: t.createShaderModule({
        code: Va
      }),
      entryPoint: "vs_main",
      buffers: [
        {
          arrayStride: 8,
          stepMode: "instance",
          attributes: [{ shaderLocation: 0, offset: 0, format: "float32x2" }]
        },
        // position
        {
          arrayStride: 16,
          stepMode: "instance",
          attributes: [{ shaderLocation: 1, offset: 0, format: "float32x4" }]
        },
        // color
        {
          arrayStride: 4,
          stepMode: "instance",
          attributes: [{ shaderLocation: 2, offset: 0, format: "float32" }]
        },
        // size
        {
          arrayStride: 16,
          stepMode: "instance",
          attributes: [{ shaderLocation: 3, offset: 0, format: "float32x4" }]
        },
        // stroke color
        {
          arrayStride: 4,
          stepMode: "instance",
          attributes: [{ shaderLocation: 4, offset: 0, format: "float32" }]
        },
        // stroke width
        {
          arrayStride: 4,
          stepMode: "instance",
          attributes: [{ shaderLocation: 5, offset: 0, format: "uint32" }]
        },
        // symbol
        {
          arrayStride: 8,
          stepMode: "vertex",
          attributes: [{ shaderLocation: 6, offset: 0, format: "float32x2" }]
        }
        // offset
      ]
    },
    fragment: {
      module: t.createShaderModule({
        code: qa
      }),
      entryPoint: "fs_main",
      targets: [
        {
          format: e,
          blend: {
            color: {
              srcFactor: "src-alpha",
              dstFactor: "one-minus-src-alpha",
              operation: "add"
            },
            alpha: {
              srcFactor: "one",
              dstFactor: "one-minus-src-alpha",
              operation: "add"
            }
          }
        }
      ]
    },
    primitive: {
      topology: "triangle-strip"
    }
  });
}
class Ga {
  constructor(e) {
    this.bindGroup = null, this.canvas = e;
  }
  async init() {
    const { device: e, context: n, format: i } = await Oa(this.canvas);
    this.device = e, this.context = n, this.pipeline = await Xa(e, i);
  }
}
class Ya {
  constructor(e) {
    this.buffers = {}, this.device = e;
  }
  createBuffer(e, n, i) {
    this.buffers[e] = this.device.createBuffer({
      size: n.byteLength,
      usage: i
    }), this.device.queue.writeBuffer(this.buffers[e], 0, n);
  }
  updateBuffer(e, n) {
    this.device.queue.writeBuffer(this.buffers[e], 0, n);
  }
}
class Za {
  constructor(e, n, i, r, s, o) {
    this.clickCallback = null, this.isDragging = !1, this.lastMousePos = { x: 0, y: 0 }, this.dragStart = null, this.lastZoomTime = 0, this.canvas = e, this.onZoom = n, this.onPan = i, this.onReset = r, this.getTransform = s, this.getDataRange = o, this.addEventListeners();
  }
  setOnClick(e) {
    this.clickCallback = e;
  }
  addEventListeners() {
    this.canvas.addEventListener("wheel", (e) => this.handleZoom(e)), this.canvas.addEventListener("mousedown", (e) => this.handlePanStart(e)), window.addEventListener("mousemove", (e) => this.handlePanMove(e)), window.addEventListener("mouseup", (e) => this.handlePanEnd(e)), this.canvas.addEventListener("dblclick", () => this.onReset());
  }
  handleZoom(e) {
    e.preventDefault();
    const n = performance.now();
    if (n - this.lastZoomTime < 30) return;
    this.lastZoomTime = n;
    const i = 1.1, r = e.deltaY < 0 ? i : 1 / i, s = this.canvas.getBoundingClientRect(), o = (e.clientX - s.left) / s.width * 2 - 1, a = (e.clientY - s.top) / s.height * 2 - 1;
    requestAnimationFrame(() => {
      this.onZoom(r, { x: o, y: a });
    });
  }
  handlePanStart(e) {
    this.isDragging = !0, this.dragStart = { x: e.clientX, y: e.clientY }, this.lastMousePos = { x: e.clientX, y: e.clientY };
  }
  handlePanMove(e) {
    if (!this.isDragging) return;
    let n = e.clientX - this.lastMousePos.x, i = e.clientY - this.lastMousePos.y;
    n = Math.max(-50, Math.min(50, n)), i = Math.max(-50, Math.min(50, i)), this.lastMousePos = { x: e.clientX, y: e.clientY }, requestAnimationFrame(() => {
      this.onPan({ x: n, y: i });
    });
  }
  handlePanEnd(e) {
    if (this.isDragging) {
      if (this.dragStart) {
        const n = e.clientX - this.dragStart.x, i = e.clientY - this.dragStart.y;
        if (Math.sqrt(n * n + i * i) < 5 && this.clickCallback) {
          const o = this.canvas.getBoundingClientRect(), a = e.clientX - o.left, c = o.bottom - e.clientY, l = a / o.width * 2 - 1, h = c / o.height * 2 - 1, u = this.getTransform(), f = (l - u.x) / u.scale, d = (h - u.y) / u.scale, p = 0.9, g = this.getDataRange();
          if (!g)
            console.warn("Data range is not set.");
          else {
            const { xMin: y, xMax: w, yMin: b, yMax: v } = g, M = w - y, _ = v - b, Yt = (f / p + 1) / 2 * M + y, Zt = (d / p + 1) / 2 * _ + b, bt = 10 / Math.min(o.width, o.height) * M * p;
            this.clickCallback([Yt, Zt], bt);
          }
        }
      }
      this.isDragging = !1, this.dragStart = null;
    }
  }
}
class Ka {
  constructor(e) {
    this.pointCount = 0, this.transform = {
      scale: 1,
      x: 0,
      y: 0
    }, this.dataRange = null, this.canvas = e, this.gpu = new Ga(e);
  }
  async init() {
    await this.gpu.init(), this.buffer = new Ya(this.gpu.device), this.initBuffers(), this.createBindGroup(), this.interaction = new Za(
      this.canvas,
      (e, n) => this.handleZoom(e, n),
      (e) => this.handlePan(e),
      () => this.handleReset(),
      () => this.transform,
      () => this.dataRange
    );
  }
  initBuffers() {
    this.buffer.createBuffer(
      "canvasSize",
      new Float32Array([this.canvas.width, this.canvas.height]),
      GPUBufferUsage.UNIFORM | GPUBufferUsage.COPY_DST
    ), this.buffer.createBuffer(
      "transform",
      new Float32Array([1, 0, 0]),
      GPUBufferUsage.UNIFORM | GPUBufferUsage.COPY_DST
    );
  }
  createBindGroup() {
    !this.gpu.device || !this.buffer.buffers.canvasSize || (this.gpu.bindGroup = this.gpu.device.createBindGroup({
      layout: this.gpu.pipeline.getBindGroupLayout(0),
      entries: [
        {
          binding: 0,
          resource: { buffer: this.buffer.buffers.canvasSize }
        },
        { binding: 1, resource: { buffer: this.buffer.buffers.transform } }
      ]
    }));
  }
  setData(e, n) {
    if (!this.gpu.device) {
      console.error("WebGPU device is not initialized.");
      return;
    }
    const i = Wa(e, n), { xMin: r, xMax: s, yMin: o, yMax: a } = ei(e);
    this.dataRange = { xMin: r, xMax: s, yMin: o, yMax: a }, this.bufferMap = Object.freeze(i), Object.entries(this.bufferMap).forEach(([c, l]) => {
      this.buffer.createBuffer(
        c,
        l,
        GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST
      );
    }), this.pointCount = this.bufferMap.vertex.length / 2;
  }
  handleZoom(e, n) {
    this.transform.scale *= e, this.transform.x = n.x - (n.x - this.transform.x) * e, this.transform.y = n.y - (n.y - this.transform.y) * e, this.updateTransformBuffer(), this.render();
  }
  handlePan(e) {
    this.transform.x += e.x / this.canvas.width * 1.5, this.transform.y -= e.y / this.canvas.height * 1.5, this.updateTransformBuffer(), this.render();
  }
  handleReset() {
    this.transform = { scale: 1, x: 0, y: 0 }, this.updateTransformBuffer(), this.render();
  }
  setOnClick(e) {
    this.interaction.setOnClick(e);
  }
  updateTransformBuffer() {
    if (!this.gpu.device) return;
    const e = new Float32Array([
      this.transform.scale,
      this.transform.x,
      this.transform.y
    ]);
    this.gpu.device.queue.writeBuffer(
      this.buffer.buffers.transform,
      0,
      e
    );
  }
  render() {
    if (!this.pointCount) {
      console.warn("No points to render.");
      return;
    }
    const e = this.gpu.device.createCommandEncoder(), n = e.beginRenderPass({
      colorAttachments: [
        {
          view: this.gpu.context.getCurrentTexture().createView(),
          clearValue: { r: 1, g: 1, b: 1, a: 1 },
          loadOp: "clear",
          storeOp: "store"
        }
      ]
    });
    n.setPipeline(this.gpu.pipeline), n.setBindGroup(0, this.gpu.bindGroup), n.setVertexBuffer(0, this.buffer.buffers.vertex), n.setVertexBuffer(1, this.buffer.buffers.color), n.setVertexBuffer(2, this.buffer.buffers.size), n.setVertexBuffer(3, this.buffer.buffers.strokeColor), n.setVertexBuffer(4, this.buffer.buffers.strokeWidth), n.setVertexBuffer(5, this.buffer.buffers.symbol), n.setVertexBuffer(6, this.buffer.buffers.offset), n.draw(this.bufferMap.offset.length / 2, this.pointCount), n.end(), this.gpu.device.queue.submit([e.finish()]);
  }
}
const Qa = {
  maxWidth: "250px",
  width: "100%"
}, Ja = {
  display: "flex",
  "flex-direction": "column",
  "margin-bottom": "10px",
  maxWidth: "300px",
  "font-size": "16px"
  // 추가된 기본 폰트 크기
}, ja = {
  "font-size": "18px",
  // label 폰트 크기
  "margin-bottom": "5px"
}, cn = {
  "font-size": "16px"
  // min/max 값 폰트 크기
};
class tl {
  constructor(e, n, i, r, s) {
    this.id = e, this.label = n, this.min = i, this.max = r, this.step = s, this.component = document.createElement("div");
  }
  render(e) {
    const n = e.get(this.id), i = typeof n == "number" ? n.toFixed(2) : "N/A", r = L`
      <div class="slider-container" style=${x(Ja)}>
        <label
          for="${this.id}"
          id="${this.id}-label"
          style=${x(ja)}
          >${this.label}: ${i}</label
        >

        <div style="display: flex; justify-content: space-between;">
          <span style=${x(cn)}>0</span>
          <input
            type="range"
            id="${this.id}"
            min="${this.min}"
            max="${this.max}"
            step="${this.step}"
            style=${x(Qa)}
            .value="${typeof n == "number" ? n : 0}"
            @change="${(s) => {
      e.set(this.id, +s.target.value), e.save_changes();
    }}"
          />
          <span style=${x(cn)}>1</span>
        </div>
      </div>
    `;
    return it(r, this.component), this.component;
  }
  update(e) {
    console.log("update", e);
    const n = e.toFixed(2), i = this.component.querySelector("label"), r = this.component.querySelector("input"), s = document.getElementById("rd-title");
    console.log(i, r), i && (i.textContent = `${this.label}: ${n}`), r && (r.value = e.toString()), console.log(s), s && s.textContent && (s.textContent = `${s.textContent.split(",")[0]}, ${e})-Stable Projection`);
  }
}
class ee {
  constructor(e, n) {
    this.id = e, this.label = n;
  }
  render(e) {
    return L`
      <label style="font-size: 18px;">
        <input
          type="checkbox"
          id="${this.id}"
          .checked="${e.get(this.id)}"
          width="100%"
          @change="${(n) => {
      e.set(this.id, n.target.checked), e.save_changes();
    }}"
        />
        ${this.label}
      </label>
    `;
  }
}
const el = {
  maxWidth: "350px",
  width: "300px"
}, nl = {
  "font-size": "2.5em",
  "font-weight": "bold",
  "margin-bottom": "10px"
}, il = {
  display: "flex",
  "flex-direction": "row",
  "justify-content": "space-between",
  "align-items": "center",
  "margin-bottom": "10px",
  maxWidth: "300px",
  width: "100%"
}, rl = {
  display: "flex",
  "flex-direction": "column",
  "margin-bottom": "10px",
  maxWidth: "300px",
  width: "100%"
};
class sl {
  constructor() {
    this.container = document.createElement("div"), this.sliders = [
      new tl("distance", "Distance", 0, 1, 0.01)
      // new Slider("sensitivity", "Sensitivity", 0.01, 1, 0.01),
    ], this.checkboxes = [
      new ee("show_unstables", "Unstables"),
      new ee("show_neighbors", "Neighbors"),
      new ee("show_ghosts", "Ghosts")
    ];
  }
  update(e, n) {
    var r;
    ["distance", "sensitivity"].includes(e) && typeof n == "number" && ((r = this.sliders.find((s) => s.id === e)) == null || r.update(n), console.log(this.sliders.find((s) => s.id === e))), ["show_neighbors", "show_ghosts", "show_unstables"].includes(e) && _e("#" + e).attr("checked", n);
  }
  render(e) {
    const n = L`
      <div class="settings-container" style=${x(el)}>
        <div style=${x(nl)}>Settings</div>
        <div style=${x(il)}>
          ${this.checkboxes.map((i) => i.render(e))}
        </div>
        <div style=${x(rl)}>
          ${this.sliders.map(
      (i) => L` <div>${i.render(e)}</div> `
    )}
        </div>
      </div>
    `;
    return it(n, this.container), this.container;
  }
}
class ol {
  constructor() {
    this.container = document.createElement("div");
  }
  update(e, n) {
    const i = L`
      <div id="unstableInfo">
        Number of Unstables: ${e || 0}
        (${(n == null ? void 0 : n.toFixed(4)) || 0}%)
      </div>
    `;
    it(i, this.container);
  }
  render(e, n) {
    return this.update(e, n), this.container;
  }
}
const al = {
  height: "100%",
  maxHeight: "360px",
  "max-width": "250px",
  "overflow-y": "auto",
  border: "1px solid #ccc",
  padding: "5px",
  "margin-top": "5px",
  "font-size": "0.9em",
  color: "#555"
}, ll = {
  display: "flex",
  "align-items": "center",
  "margin-bottom": "2px"
};
class cl {
  constructor() {
    this.container = document.createElement("div");
  }
  onClick(e, n, i, r) {
    const s = i();
    console.log(s), r(
      n ? [...s, e] : s.filter((o) => o !== e)
    );
  }
  updateCheckbox(e) {
    console.log("updateCheckbox", e), Pe(".unstable-list input").property("checked", !1), e.forEach((n) => {
      _e(`#unstable-${n}`).property("checked", !0);
    });
  }
  reset() {
    Pe(".unstable-list input").property("checked", !1);
  }
  update(e, n, i) {
    const r = e.sort((o, a) => a.instability - o.instability), s = L`
      <div class="unstable-list" style=${x(al)}>
        ${r.length ? r.map(
      (o) => L`
                <div style=${x(ll)}>
                  <input
                    type="checkbox"
                    id="unstable-${o.id}"
                    name="unstable-${o.id}"
                    @click=${(a) => this.onClick(
        o.id,
        a.target.checked,
        n,
        i
      )}
                  />
                  <label for="unstable-${o.id}" style="margin-left: 5px;"
                    >${o.id}
                  </label>
                </div>
              `
    ) : L`<div>None</div>`}
      </div>
    `;
    it(s, this.container);
  }
  render(e, n, i) {
    return this.update(e, n, i), this.container;
  }
}
const un = {
  "margin-top": "10px",
  "font-size": "18px"
}, ul = {
  "font-size": "2.5em",
  "font-weight": "bold"
}, hl = {
  maxWidth: "300px",
  width: "300px"
};
class fl {
  constructor() {
    this.container = document.createElement("div"), this.unstableCounter = new ol(), this.unstableIDList = new cl();
  }
  update(e, n, i, r, s) {
    this.unstableCounter.update(n, i), this.unstableIDList.update(e, r, s);
  }
  updateCheckbox(e) {
    this.unstableIDList.updateCheckbox(e);
  }
  render(e, n, i, r, s) {
    const o = L`
      <div style=${x(hl)}>
        <div style=${x(ul)}>Unstable Points</div>
        <div style=${x(un)}>
          ${this.unstableCounter.render(n, i)}
        </div>
        <div style=${x(un)}>
          ${this.unstableIDList.render(e, r, s)}
        </div>
      </div>
    `;
    return it(o, this.container), this.container;
  }
}
class dl {
  constructor(e, n) {
    this.width = e, this.height = n, this.svg = this.createSVG(), this.symbolLegend = this.svg.append("g"), this.labelLegend = this.svg.append("g"), this.ghostColorLegend = this.svg.append("g");
  }
  createSVG() {
    return Jr("svg").attr("class", "legend").attr("width", `${this.width}px`).attr("height", `${this.height}px`);
  }
  renderSymbolLegend() {
    const e = [
      { label: "Unstable", symbol: pa },
      { label: "Ghost", symbol: ya },
      { label: "Neighbor", symbol: ma }
    ];
    this.symbolLegend.attr("transform", "translate(20, 150)"), this.symbolLegend.selectAll("path").data(e).join("path").attr(
      "d",
      _a().type((n) => n.symbol).size(200)
    ).attr("transform", (n, i) => `translate(0, ${20 + i * 28})`).attr("fill", "none").attr("stroke", "black").attr("stroke-width", 1), this.symbolLegend.selectAll("text").data(e).join("text").text((n) => n.label).attr("x", 20).attr("y", (n, i) => 22 + i * 28).attr("alignment-baseline", "middle").attr("font-size", "18px");
  }
  renderLabelLegend(e, n, i) {
    e.length === 0 && Object.keys(n).length === 0 || (this.labelLegend.attr("transform", "translate(20, 260)"), e.length ? n = e.reduce((r, s, o) => (r[s] = Gn[o % 10], r), {}) : e = Object.keys(n), this.labelLegend.selectAll("circle").data(e).join("circle").attr("cx", 0).attr("cy", (r, s) => 10 + s * 23).attr("r", 7).attr("fill", (r, s) => i.colorScale(s.toString())), this.labelLegend.selectAll("text").data(e).join("text").text((r) => r).attr("x", 15).attr("y", (r, s) => 11 + s * 23).attr("alignment-baseline", "middle").attr("font-size", "18px"));
  }
  renderGhostLegend(e) {
    const n = Xn(Q("#000000", "#ffffff")).domain([0, 1]);
    this.ghostColorLegend.attr("transform", "translate(10, 80)"), this.svg.append("defs").append("linearGradient").attr("id", "ghost-gradient").attr("x1", "0%").attr("x2", "100%").attr("y1", "0%").attr("y2", "0%").selectAll("stop").data(fn(0, 1.01, 0.01)).enter().append("stop").attr("offset", (r) => `${r * 100}%`).attr("stop-color", (r) => n(r)), this.ghostColorLegend.append("rect").attr("x", 0).attr("y", 20).attr("width", 150).attr("height", 20).style("fill", "url(#ghost-gradient)"), this.ghostColorLegend.append("text").attr("x", 0).attr("y", 10).attr("alignment-baseline", "middle").attr("font-size", "18px").text("Ghost Color Scale"), this.ghostColorLegend.append("text").attr("x", 0).attr("y", 50).attr("alignment-baseline", "middle").attr("font-size", "16px").text("0"), this.ghostColorLegend.append("text").attr("x", 160).attr("y", 50).attr("alignment-baseline", "middle").attr("font-size", "16px").attr("text-anchor", "middle").text(`${e.toString()} (r)`);
  }
  render(e, n, i, r) {
    return this.renderSymbolLegend(), this.renderLabelLegend(e, n, r), this.renderGhostLegend(i), this.svg.node();
  }
  update(e, n, i) {
    this.renderLabelLegend(e, n, i);
  }
}
function pl(t, e, n, i, r, s) {
  const o = new dl(r, s);
  return {
    legendView: o,
    renderedLegend: o.render(t, e, n, i)
  };
}
class gl {
  constructor(e) {
    this.visibility = {
      neighbors: !1,
      ghosts: !0,
      unstables: !0
    }, this.unstList = [], this.externalUpdateUnstList = () => {
    }, this.canvas = document.createElement("canvas"), this.canvas.width = e.width, this.canvas.height = e.height, this.scatterplot = new Ka(this.canvas);
  }
  async init(e) {
    await this.scatterplot.init(), this.externalUpdateUnstList = e, this.scatterplot.setOnClick(this.onClick.bind(this));
  }
  update(e, n, i, r) {
    console.log(i), this.origEmb = e, this.unstEmb = n, this.ghostEmb = i, this.scales = r, this.rebuildEmbeddingConfig(), this.render();
  }
  updateUnstList(e) {
    this.unstList = e, console.log(this.unstList, "unstList"), this.rebuildEmbeddingConfig(), this.render();
  }
  updateVisibility(e, n) {
    this.visibility[e] = n, this.rebuildEmbeddingConfig(), this.render();
  }
  initializeEmbeddingConfig() {
    this.embeddingConfig = {
      coords: this.origEmb.map((e) => [e.x, e.y]),
      color: this.origEmb.map((e) => this.scales.colorScale(e.label)),
      size: this.origEmb.map((e) => 2),
      symbol: this.origEmb.map((e) => "circle"),
      opacity: this.origEmb.map((e) => 1),
      strokeWidth: this.origEmb.map((e) => 0)
    };
  }
  rebuildEmbeddingConfig() {
    this.initializeEmbeddingConfig(), this.visibility.neighbors && this.addNeighborEmbedding(), this.visibility.ghosts && this.addGhostEmbedding(), this.visibility.unstables && this.addUnstEmbedding(), this.render();
  }
  addUnstEmbedding() {
    const e = this.unstList.length ? this.unstList.map((n) => this.origEmb[n]) : this.unstEmb;
    console.log(e), e.forEach((n) => {
      this.embeddingConfig.opacity[n.id] = 0, this.embeddingConfig.coords.push([n.x, n.y]), this.embeddingConfig.color.push(this.scales.colorScale(n.label)), this.embeddingConfig.size.push(25), this.embeddingConfig.symbol.push("cross"), this.embeddingConfig.strokeWidth.push(4), this.embeddingConfig.opacity.push(1);
    });
  }
  addGhostEmbedding() {
    this.unstList.length !== 0 && this.unstList.forEach((e) => {
      const { coords: n, label: i } = this.ghostEmb[e];
      n.forEach((r) => {
        this.embeddingConfig.coords.push([r.x, r.y]), this.embeddingConfig.color.push(
          this.scales.ghostColorScale(i)(r.r)
        ), this.embeddingConfig.size.push(20), this.embeddingConfig.symbol.push("triangle"), this.embeddingConfig.strokeWidth.push(2), this.embeddingConfig.opacity.push(1);
      });
    });
  }
  addNeighborEmbedding() {
    if (this.unstList.length === 0) return;
    const e = new Set(
      this.unstList.flatMap((n) => this.origEmb[n].neighbors)
    );
    console.log(e, "activatedNeighborIds"), e.forEach((n) => {
      const { x: i, y: r, label: s } = this.origEmb[n];
      this.embeddingConfig.coords.push([i, r]), this.embeddingConfig.color.push(this.scales.colorScale(s)), this.embeddingConfig.size.push(20), this.embeddingConfig.symbol.push("diamond"), this.embeddingConfig.strokeWidth.push(2), this.embeddingConfig.opacity.push(1);
    });
  }
  render() {
    this.scatterplot.setData(this.embeddingConfig.coords, {
      color: this.embeddingConfig.color,
      size: this.embeddingConfig.size,
      symbol: this.embeddingConfig.symbol,
      strokeColor: "#000000",
      strokeWidth: this.embeddingConfig.strokeWidth,
      opacity: this.embeddingConfig.opacity
    }), this.scatterplot.render();
  }
  onClick(e, n) {
    console.log(e);
    const i = this.unstList.length ? this.unstList.map((c) => this.origEmb[c]) : this.unstEmb, [r, s] = e;
    let o = Number.MAX_VALUE, a = null;
    i.forEach((c) => {
      const l = Math.hypot(c.x - r, c.y - s);
      l < o && (o = l, a = c.id);
    }), a = o < 2 * n ? a : null, console.log(a), this.externalUpdateUnstList(a ? [a] : []);
  }
}
function ml(t) {
  const e = new sl();
  return { settingsView: e, renderedSetting: e.render(t) };
}
function yl(t, e, n, i) {
  const r = new fl();
  console.log(i.get("checkedUnstables"), "checkedUnstables");
  const s = r.render(
    t,
    e.numUnstables,
    e.percentUnstables,
    () => i.get("checkedUnstables"),
    n
  );
  return { unstableContainerView: r, renderedUnstable: s };
}
async function _l({ model: t, el: e }) {
  const n = document.createElement("div");
  console.log(t.get("embedding_id"), t.get("embedding_set"));
  const { origEmb: i, unstEmb: r, ghostEmb: s, scales: o, legend: a, colors: c, radius: l } = ct(t), h = pe(t, r, i.length), u = (v) => {
    t.set("checkedUnstables", v), t.save_changes();
  };
  t.set("checkedUnstables", []);
  const f = new gl({
    width: t.get("width"),
    height: t.get("height")
  });
  await f.init(u), f.update(i, r, s, o);
  const { legendView: d, renderedLegend: p } = pl(
    a,
    c,
    l,
    o,
    t.get("legend_width"),
    t.get("legend_height")
  ), { settingsView: g, renderedSetting: y } = ml(t), { unstableContainerView: w, renderedUnstable: b } = yl(
    r,
    h,
    u,
    t
  );
  it(
    L` <div
      id="widget-container"
      class="container"
      style=${x(Ua)}
    >
      <div
        class="row"
        style="width:100%;display:flex;flex-direction:row; margin: 20px;"
      >
        <div class="col-md-3 left" style=${x(Pa)}>
          <div class="toolbar">${y}</div>
          <div class="unstable-container">${b}</div>
        </div>
        <div class="col-md-9 scatterplot" style=${x(Ra)}>
          <div style="display: flex; flex-direction: column; ">
            <div
              style="font-size: 2.5em; font-weight: bold; margin-bottom: 10px;"
              id="rd-title"
            >
              (${l}, ${t.get("distance")})-Stable Projection
            </div>

            <div
              style="display: flex; flex-direction: row; justify-content: space-between;"
            >
              <div class="projection" style=${x(Ia)}>
                ${f.canvas}
              </div>
              <div class="legend" style=${x(Da)}>
                ${p}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>`,
    n
  ), Ba(
    t,
    f,
    d,
    g,
    w,
    u
  ), e.appendChild(n);
}
const bl = { render: _l };
export {
  bl as default
};
