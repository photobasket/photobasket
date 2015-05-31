<?php
namespace PhotoBasket;

class AlbumIndexAction extends Action {
	function main() {
		$data = array(
			'name'			=> 'Albumname',
			'soundloud_url'	=> false,
			'download_url'	=> '/download/dummy.zip',
			'users'			=> array(
				'user1@foo.bar',
				'seconduser@lorem.ipsum'
			),
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
