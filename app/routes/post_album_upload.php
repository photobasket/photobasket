<?php

$app->post('/album/:albumname/:userkey/upload', function($albumname, $userkey) use ($app) {
	require_once __DIR__ . '/../actions/album_upload.php';
	new \PhotoBasket\AlbumUploadAction(
		$app,
		array(
			'album' 	=> $albumname,
			'user'		=> $userkey
		)
	);
});
