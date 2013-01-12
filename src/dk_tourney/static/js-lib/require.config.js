var jam = {
    "packages": [
        {
            "name": "underscore",
            "location": "js-lib/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js-lib/jquery",
            "main": "jquery.js"
        },
        {
            "name": "bootstrap",
            "location": "js-lib/bootstrap"
        }
    ],
    "version": "0.2.13",
    "shim": {
        "underscore": {
            "exports": "_"
        }
    }
};

if (typeof require !== "undefined" && require.config) {
    require.config({
    "packages": [
        {
            "name": "underscore",
            "location": "js-lib/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js-lib/jquery",
            "main": "jquery.js"
        },
        {
            "name": "bootstrap",
            "location": "js-lib/bootstrap"
        }
    ],
    "shim": {
        "underscore": {
            "exports": "_"
        }
    }
});
}
else {
    var require = {
    "packages": [
        {
            "name": "underscore",
            "location": "js-lib/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js-lib/jquery",
            "main": "jquery.js"
        },
        {
            "name": "bootstrap",
            "location": "js-lib/bootstrap"
        }
    ],
    "shim": {
        "underscore": {
            "exports": "_"
        }
    }
};
}

if (typeof exports !== "undefined" && typeof module !== "undefined") {
    module.exports = jam;
}