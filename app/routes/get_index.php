<?php

$app->get('/', function () use ($app) {
	require_once __DIR__ . '/../actions/index.php';
	new \PhotoBasket\IndexAction(
		$app,
		array()
	);
});
