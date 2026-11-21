importScripts('/src/js/idb.js');
importScripts('/src/js/utility.js');

var CACHE_STATIC_NAME = 'static-v9';
var CACHE_DYNAMIC_NAME = 'dynamic-v9';

var STATIC_FILES = [
    '/',
    '/index.html',
    '/offline.html',
    '/src/js/app.js',
    '/src/js/feed.js',
    '/src/js/idb.js',
    '/src/js/utility.js',
    '/src/js/material.min.js',
    '/src/css/app.css',
    '/src/css/feed.css',
    '/src/images/main-image.png',
    'https://fonts.googleapis.com/css?family=Roboto:400,700',
    'https://fonts.googleapis.com/icon?family=Material+Icons',
    'https://cdnjs.cloudflare.com/ajax/libs/material-design-lite/1.3.0/material.indigo-pink.min.css'
];

self.addEventListener('install', function (event) {
    console.log('[Serviceworker] Installing Service Worker', event);
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_STATIC_NAME)
            .then(function (cache) {
                console.log('[Serviceworker] Caching app shell');
                return cache.addAll(STATIC_FILES);
            })
    );
});
self.addEventListener('activate', function (event) {
    console.log('[Serviceworker] Activating Service Worker', event);

    event.waitUntil(
        caches.keys()
            .then(function (keyList) {
                return Promise.all(keyList.map(function (key) {
                    if (key !== CACHE_STATIC_NAME && key !== CACHE_DYNAMIC_NAME) {
                        console.log('[Serviceworker] Removing old cache.', key);
                        return caches.delete(key);
                    }
                }));
            })
    );
    return self.clients.claim();
});

function isInArray(string, array) {
    var cachePath;
    if (string.indexOf(self.origin) === 0) {
        console.log('matched', string);
        cachePath = string.substring(self.origin.length).split('?')[0];
    } else {
        cachePath = string;
    }
    return array.indexOf(cachePath) > -1;
}
self.addEventListener('fetch', function (event) {
    var url = 'https://xmmkfhtidsgyrebpmcij.supabase.co/rest/v1/post';

    if (event.request.url.indexOf(url) > -1 && event.request.method === 'GET') {
        event.respondWith(fetch(event.request)
            .then(function (res) {
                var clonedRes = res.clone();
                clearAllData('posts')
                    .then(function () {
                        return clonedRes.json();
                    })
                    .then(function (data) {
                        for (var key in data) {
                            writeData('posts', data[key]);
                        }
                    });
                return res;
            })
        );
    } else if (isInArray(event.request.url, STATIC_FILES)) {
        event.respondWith(
            caches.match(event.request, { ignoreSearch: true })
        );
    } else {
        event.respondWith(
            caches.match(event.request)
                .then(function (response) {
                    if (response) {
                        return response;
                    } else {
                        return fetch(event.request)
                            .then(function (res) {
                                return caches.open(CACHE_DYNAMIC_NAME)
                                    .then(function (cache) {
                                        if (event.request.url.indexOf('http') === 0) {
                                            cache.put(event.request.url, res.clone());
                                        }
                                        return res;
                                    });
                            })
                            .catch(function (err) {
                                return caches.open(CACHE_STATIC_NAME)
                                    .then(function (cache) {
                                        if (event.request.headers.get('accept').includes('text/html')) {
                                            return cache.match('/offline.html');
                                        }
                                    });
                            });
                    }
                })
        );
    }
});

var SUPABASE_URL = 'https://xmmkfhtidsgyrebpmcij.supabase.co';
var SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhtbWtmaHRpZHNneXJlYnBtY2lqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI3Mjk4MjQsImV4cCI6MjEwODMwNTgyNH0.32sBgQTogMbit9y_Wlr-c-w-2xpVg42RkE41DJ1wQdE';

self.addEventListener('sync', function (event) {
    console.log('[Service Worker] Background syncing', event);
    if (event.tag === 'sync-new-posts') {
        console.log('[Service Worker] Syncing new Posts');
        event.waitUntil(
            readAllData('sync-posts')
                .then(function (data) {
                    for (var dt of data) {
                        (function (post) {
                            fetch(SUPABASE_URL + '/rest/v1/post', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json',
                                    'Accept': 'application/json',
                                    'apikey': SUPABASE_KEY,
                                    'Authorization': 'Bearer ' + SUPABASE_KEY
                                },
                                body: JSON.stringify({
                                    id: post.id,
                                    title: post.title,
                                    location: post.location,
                                    image: 'https://xmmkfhtidsgyrebpmcij.supabase.co/storage/v1/object/public/images/sf-boat.jpg'
                                })
                            })
                                .then(function (res) {
                                    console.log('Sent data', res);
                                    if (res.ok) {
                                        deleteItemFromData('sync-posts', post.id);
                                    }
                                })
                                .catch(function (err) {
                                    console.log('Error while sending data', err);
                                });
                        })(dt);
                    }
                })
        );
    }
});