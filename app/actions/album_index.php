<?php
namespace PhotoBasket;

class AlbumIndexAction extends Action {
	function main() {
		if(!$this->check_existence_of_album($this->params['album'])) {
			return;
		}
		$album = DB::get_album($this->params['album']);

		if (!$this->check_existence_of_album_user($this->params['album'], $this->params['user'])) {
			return;
		}

		$this->render('album.html');
	}
}
