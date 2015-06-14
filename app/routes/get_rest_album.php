<?php

$app->get('/rest/album/:albumname/:userkey', function ($albumname, $userkey) use ($app) {
	require_once __DIR__ . '/../actions/album_rest_index.php';
	new \PhotoBasket\AlbumRestIndexAction(
		$app,
		array(
			'album' => $albumname,
			'user'	=> $userkey
		)
	);
});
