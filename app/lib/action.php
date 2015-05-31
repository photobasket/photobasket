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

	protected function setJSONHeader() {
		$this->response->headers->set('Content-Type', 'application/json');
	}

	protected function renderJSON($array) {
		$this->setJSONHeader();
		$this->response->write(json_encode($array, JSON_PRETTY_PRINT));
	}

	protected function renderJSONError($message, $status_code = 400) {
		$this->setJSONHeader();
		$this->response->setStatus($status_code);
		$this->response->write(json_encode(array('error' => $message)));
	}
}
