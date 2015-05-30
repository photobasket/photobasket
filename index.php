<?php
require 'vendor/autoload.php';

$app = new \Slim\Slim(array(
	'mode'	=> 'development',
    'debug' => true
));

require __DIR__ . '/app/routes/routes.php';

$app->run();