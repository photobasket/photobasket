<?php
namespace PhotoBasket;

class Action {
	private $response;
	private $request;

	public function __construct($app, $parameters) {
		$this->request	= $app->request;
		$this->response	= $app->response;
		$this->params	= $parameters;

		$this->main();
	}

	public function main() {
		// DO NOTHING
	}

	protected function renderJSON($array) {
		$this->response->headers->set('Content-Type', 'application/json');
		$this->response->write(json_encode($array, JSON_PRETTY_PRINT));
	}
}
