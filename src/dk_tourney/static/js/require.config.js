var jam = {
    "packages": [
        {
            "name": "underscore",
            "location": "js/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js/jquery",
            "main": "jquery.js"
        },
        {
            "name": "bootstrap",
            "location": "js/bootstrap"
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
            "location": "js/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js/jquery",
            "main": "jquery.js"
        },
        {
            "name": "bootstrap",
            "location": "js/bootstrap"
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
            "location": "js/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js/jquery",
            "main": "jquery.js"
        },
        {
            "name": "bootstrap",
            "location": "js/bootstrap"
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