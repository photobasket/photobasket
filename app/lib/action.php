<?php
namespace PhotoBasket;

class Action {
	private $response;
	private $request;
	private $twig;

	public function __construct($app, $parameters) {
		$this->init_templating();

		$this->request	= $app->request;
		$this->response	= $app->response;
		$this->params	= $parameters;

		$this->main();
	}

	public function main() {
		// DO NOTHING
	}

	public function render($template_name, $template_params = array(), $status_code = 200) {
		$template = $this->twig->loadTemplate($template_name);
		$rendered = $template->render($template_params);

		$this->response->setStatus($status_code);
		$this->response->write($rendered);
	}

	protected function set_json_header() {
		$this->response->headers->set('Content-Type', 'application/json');
	}

	protected function deliver_file($file_path, $content_type = 'application/octet-stream') {
		$this->response->setStatus(200);
		$this->response->headers->set('Content-Type', $content_type);
		$this->response->headers->set('Content-Transfer-Encoding', 'binary');
		$this->response->headers->set('Content-Length', filesize($file_path));
		$this->response->finalize();

		readfile($file_path);
	}

	protected function render_json($array) {
		$this->set_json_header();
		$this->response->setStatus(200);
		$this->response->write(json_encode($array, JSON_PRETTY_PRINT));
	}

	protected function render_not_found($message = '404 - not found') {
		$this->response->setStatus(404);
		$this->response->write($message);
	}

	protected function render_error($message = '400 - error', $code = 400) {
		$this->response->setStatus($code);
		$this->response->write($message);
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

	private function init_templating() {
		$loader = new \Twig_Loader_Filesystem(__DIR__ . '/../views/');
		$this->twig = new \Twig_Environment($loader, array(
			'cache'	=> false,	// has to be changed
		));

		$this->twig->addGlobal('base_url', $this->base_url());
	}

	private function base_url() {
		return preg_replace('/\/[^\/]+$/', '', $_SERVER["SCRIPT_NAME"]);
	}

	protected function base_path() {
		return realpath( __DIR__ . '/../../');
	}
}
