<?php

$app->get('/album/:albumname/:userkey/images', function ($albumname, $userkey) use ($app) {
	require_once __DIR__ . '/../actions/album_rest_index.php';
	new \PhotoBasket\AlbumRestIndexAction(
		$app,
		array(
			'album' => $albumname,
			'user'	=> $userkey
		)
	);
});
