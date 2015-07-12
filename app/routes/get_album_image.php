<?php

$app->get('/album/:albumname/image/:filename', function ($albumname, $filename) use ($app) {
	require_once __DIR__ . '/../actions/album_image.php';
	new \PhotoBasket\AlbumImageAction(
		$app,
		array(
			'album' 	=> $albumname,
			'filename'	=> $filename
		)
	);
});
