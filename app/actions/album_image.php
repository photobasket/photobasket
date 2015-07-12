<?php
namespace PhotoBasket;

class AlbumImageAction extends Action {
	function main() {
		if(!$this->check_existence_of_album($this->params['album'])) {
			return;
		}
		$album = DB::get_album($this->params['album']);

		$image = DB::get_album_image($this->params['album'], $this->params['filename']);
		if (!$image) {
			$this->render_not_found();
			return;
		}

		$image_path = $this->base_path() . '/images/' . $album['ident'] . '/' . $image['path'];

		if(!file_exists($image_path)) {
			$this->render_not_found();
			return;
		}

		$image_extension = pathinfo($image_path, PATHINFO_EXTENSION);
		$image_content_type = 'application/octet-stream';
		switch($image_extension) {
			case 'jpg': $image_content_type = 'image/jpeg'; break;
			case 'jpeg': $image_content_type = 'image/jpeg'; break;
			case 'gif': $image_content_type = 'image/gif'; break;
			case 'png': $image_content_type = 'image/png'; break;
		}

		$this->set_file_header($image_content_type);
		ob_clean();
		flush();

		readfile($image_path);
	}
}