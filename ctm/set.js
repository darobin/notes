
/*
    Implementation of set in JS, that match closely enough the usage of Python in the book.
    This could use Harmony Sets but 1) they don't seem to have all the methods, 2) they're still
    behind a flag, 3) it's more fun to implement stuff.
*/
var _ = require("underscore")
;

function Set (array) {
    this.items = _.uniq((array || []).slice(0));
}
Set.prototype = {
    size:   function () {
        return this.items.length;
    }
,   sum:    function (start) {
        var res = start || 0;
        this.items.forEach(function (it) {
            res += it;
        });
        return res;
    }
,   has:    function (item) {
        return _.contains(this.items, item);
    }
,   add:    function (item) {
        if (!this.has(item)) this.items.push(item);
        return this;
    }
,   remove: function (item) {
        var idx = this.items.indexOf(item);
        if (idx !== -1) this.items.splice(idx, 1);
        return this;
    }
,   union:  function (other) {
        return new Set(_.flatten([this.items, other.items], true));
    }
,   intersection:   function (other) {
        return new Set(_.insersection([this.items, other.items]));
    }
,   update: function (array) {
        this.items = _.uniq(_.flatten([this.items, array], true));
    }
,   comprehension:  function (fun) {
        return new Set(this.items.forEach(fun));
    }
};

exports.Set = Set;
