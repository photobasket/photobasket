<?php
namespace PhotoBasket;

use Gregwar\Image\Image;

class AlbumUploadAction extends Action {
	function main() {
		if(!$this->check_existence_of_album($this->params['album'])) {
			return;
		}
		$album = DB::get_album($this->params['album']);

		$user = DB::get_album_user($album['ident'], $this->params['user']);
		if (!$user) {
			return;
		}

		$upload_file = $_FILES['file'];
		if (!$upload_file || $upload_file['error']) {
			$upload_error = $upload_file['error'];
			switch ($upload_file['error']) {
				case UPLOAD_ERR_OK:
					break;
				case UPLOAD_ERR_NO_FILE:
					$upload_error = 'No file sent.';
				case UPLOAD_ERR_INI_SIZE:
				case UPLOAD_ERR_FORM_SIZE:
					$upload_error = 'Exceeded filesize limit.';
				default:
					$upload_error = 'Unknown errors.';
			}

			if ($upload_file['error']) {
				$this->render_error("upload error: {$upload_file['error']} // $upload_error");
			}
			return;
		}

		$albums_basedir = realpath(__DIR__ . '/../../images/');
		$album_dir = realpath($albums_basedir . '/' . $album['ident']);

		if (!is_dir($albums_basedir)) {
			$thhis->render_error("can't find base album dir $albums_basedir");
			return;
		}

		if (!is_dir($album_dir)) {
			mkdir($album_dir);
		}

		if (!is_writable($album_dir)) {
			$this->render_error("can't write to dir $album_dir");
			return;
		}

		if (move_uploaded_file($upload_file['tmp_name'], $album_dir . '/'. $upload_file['name'])) {
			$image_file = $album_dir . '/'. $upload_file['name'];
			$image_size = getimagesize($image_file);

			$thumbnail_file = preg_replace('/\.([a-z]{3,4})$/', '_320.jpg', $image_file);
			Image::open($image_file)->zoomCrop(320, 240)->save($thumbnail_file, 'jpg', 70);

			$new_image = DB::create_album_image($album['ident'], $user['email'], $upload_file['name'], "{$image_size[0]}x{$image_size[1]}");
			$this->render_json($new_image);
		}
		else {
			$this->render_error("error while uploading");
		}
	}
}
