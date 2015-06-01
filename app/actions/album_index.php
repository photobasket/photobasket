<?php
namespace PhotoBasket;

class AlbumIndexAction extends Action {
	function main() {
		$album = DB::get_album($this->params['album']);
		if (count($album) <= 0) { $this->renderJSONError('album "' . $this->params['album'] . '" missing', 404); return; }

		$user = DB::get_album_user($this->params['album'], $this->params['user']);
		if (count($user) <= 0) { $this->renderJSONError('user "' . $this->params['user'] . '" has no access to album "' . $this->params['album'] . '"', 401); return; }

		$album_users = DB::get_album_users($this->params['album']);
		$album_user_emails = array_map(function($u) { return $u['email']; }, $album_users);

		$album_images = $this->get_album_images($this->params['album']);

		$data = array(
			'name'			=> $album['name'],
			'soundloud_url'	=> $album['soundcloud_url'],
			'download_url'	=> '/download/dummy.zip',
			'users'			=> $album_user_emails,
			'images'		=> $album_images
		);

		$this->renderJSON($data);
	}

	private function get_album_images($album) {
		$db_images = DB::get_album_images($this->params['album']);
		$album_images = array();

		foreach ($db_images as $db_image) {
			array_push($album_images, array(
				'url'		=> $db_image['path'],
				'thumb320'	=> $db_image['path'],
				'size'		=> $db_image['size'],
				'uploader'	=> $db_image['user_key']
			));
		}

		return $album_images;
	}
}
