<?php

$app->post('/album/:albumname/:userkey/users', function($albumname, $userkey) use ($app) {
	require_once __DIR__ . '/../actions/user_create.php';

	$json = $app->request->getBody();
    $data = json_decode($json, true);

	new \PhotoBasket\UserCreateAction(
		$app,
		array(
			'album' 	=> $albumname,
			'user'		=> $userkey,
			'useremail'	=> $data['useremail']
		)
	);

});
