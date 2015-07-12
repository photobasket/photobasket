<?php
namespace PhotoBasket;

class AlbumInfoAction extends Action {
	function main() {
		if(!$this->check_existence_of_album($this->params['album'])) {
			return;
		}
		$album = DB::get_album($this->params['album']);

		if (!$this->check_existence_of_album_user($this->params['album'], $this->params['user'])) {
			return;
		}

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

		$this->render_json($data);
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
