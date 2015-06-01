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

		$data = array(
			'name'			=> $album['name'],
			'soundloud_url'	=> $album['soundcloud_url'],
			'download_url'	=> '/download/dummy.zip',
			'users'			=> $album_user_emails,
			'images'		=> array(
				array(
					'url'		=> 'image1.jpg',
					'thumb320'	=> 'image1.320.jpg',
					'size'		=> '800x600',
					'uploader'	=> 'uploader@example.com'
				),
				array(
					'url'		=> 'image2.jpg',
					'thumb320'	=> 'image2.320.jpg',
					'size'		=> '800x600',
					'uploader'	=> 'uploader@example.com'
				),
				array(
					'url'		=> 'image3.jpg',
					'thumb320'	=> 'image3.320.jpg',
					'size'		=> '800x600',
					'uploader'	=> 'uploader@example.com'
				)
			)
		);

		$this->renderJSON($data);
	}
}
