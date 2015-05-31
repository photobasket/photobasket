<?php

$app->get('/rest/album/:albumname/:userkey', function ($albumname, $userkey) use ($app) {
	require_once __DIR__ . '/../actions/album_index.php';
	new \PhotoBasket\AlbumIndexAction(
		$app,
		array(
			'album' => $albumname,
			'user'	=> $userkey
		)
	);
});
