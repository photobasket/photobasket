<?php

$app->get('/album/:albumname/:userkey/images', function ($albumname, $userkey) use ($app) {
	require_once __DIR__ . '/../actions/album_info.php';
	new \PhotoBasket\AlbumInfoAction(
		$app,
		array(
			'album' => $albumname,
			'user'	=> $userkey
		)
	);
});
