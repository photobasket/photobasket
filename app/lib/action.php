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

	protected function set_json_header() {
		$this->response->headers->set('Content-Type', 'application/json');
	}

	protected function render_json($array) {
		$this->set_json_header();
		$this->response->setStatus(200);
		$this->response->write(json_encode($array, JSON_PRETTY_PRINT));
	}

	protected function render_json_error($message, $status_code = 400) {
		$this->set_json_header();
		$this->response->setStatus($status_code);
		$this->response->write(json_encode(array('error' => $message)));
	}

	protected function check_existence_of_album($album_ident) {
		$album = DB::get_album($album_ident);
		if (count($album) <= 0) { $this->render_json_error('album "' . $album_ident . '" missing', 404); return; }
		return true;
	}

	protected function check_existence_of_album_user($album_ident, $user_key) {
		$user = DB::get_album_user($album_ident, $user_key);
		if (count($user) <= 0) { $this->render_json_error('user "' . $user_key . '" has no access to album "' . $album_ident . '"', 401); return; }
		return true;
	}
}
