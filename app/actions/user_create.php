<?php

namespace PhotoBasket;

class UserCreateAction extends Action {
	function main() {
		if(!$this->check_existence_of_album($this->params['album'])) {
			return;
		}
		$album = $this->params['album'];

		if (!$this->check_existence_of_album_user($album, $this->params['user'])) {
			return;
		}

		$create_user_email = strtolower(trim($this->params['useremail']));

		$album_users = DB::get_album_users($album);
		$album_user_emails = array_map(function($u) { return strtolower($u['email']); }, $album_users);
		if(in_array($create_user_email, $album_user_emails)) {
			$this->render_json_error('user with email "' . $create_user_email . '" already existing in album "' . $album_ident . '"', 406);
			return;
		}

		$created_user_key = DB::create_album_user($album, $create_user_email);

		$data = array(
			'success'	=> true,
			'useremail'	=> $create_user_email,
			'userkey'	=> $created_user_key
		);

		$this->render_json($data);
	}
}
